"""Verify the archived revised-run artifacts without executing the notebook."""

import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def verify_notebooks(provenance):
    reference_path = ROOT / "notebooks/project9_revised_executed.ipynb"
    require(sha256(reference_path) == provenance["executed_notebook_sha256"],
            "Executed notebook checksum mismatch")
    reference = read_json(reference_path)["cells"]
    clean = read_json(ROOT / "notebooks/project9_revised.ipynb")["cells"]
    require(len(reference) == len(clean), "Notebook cell counts differ")
    streams = [
        "".join(output.get("text", ""))
        for cell in reference for output in cell.get("outputs", [])
        if output["output_type"] == "stream"
    ]
    require(any(provenance["source_results_zip"] in stream for stream in streams),
            "Executed notebook does not report the supplied results ZIP")
    for index, (saved, rerun) in enumerate(zip(reference, clean), start=1):
        require((saved["cell_type"], saved["source"]) == (rerun["cell_type"], rerun["source"]),
                f"Notebook source mismatch in cell {index}")
        if saved["cell_type"] == "code":
            compile("".join(saved["source"]), f"notebook cell {index}", "exec")
            require(saved["execution_count"] is not None and
                    all(output["output_type"] != "error" for output in saved["outputs"]),
                    f"Missing execution or saved error in cell {index}")
            require(rerun["execution_count"] is None and rerun["outputs"] == [],
                    f"Rerun notebook contains saved execution in cell {index}")


def verify_results():
    status = read_json(RESULTS / "manifest/run_status.json")
    require(status["completed"] is True and status["mode"] == "full",
            "Archived run did not record successful full execution")
    records = read_json(RESULTS / "manifest/checksums.json")
    expected_paths = {row["path"] for row in records}
    actual_paths = {
        str(path.relative_to(RESULTS).as_posix())
        for folder in ("figures", "tables", "diagnostics", "manifest")
        for path in (RESULTS / folder).rglob("*")
        if path.is_file()
    }
    require(len(records) == len(expected_paths) == 56, "Unexpected checksum count")
    require(expected_paths | {"manifest/checksums.json"} == actual_paths,
            "Results tree does not match the checksum manifest")
    for row in records:
        require(sha256(RESULTS / row["path"]) == row["sha256"],
                f"Checksum mismatch for {row['path']}")

    exhibits = read_csv(RESULTS / "manifest/exhibit_inventory.csv")
    require(Counter(row["format"] for row in exhibits) == {"CSV": 10, "PDF": 10},
            "Expected 10 CSV and 10 PDF exhibits")
    require(len({row["id"] for row in exhibits}) == len({row["path"] for row in exhibits}) == 20,
            "Expected 20 unique exhibit IDs and paths")
    require(all(row["path"] in expected_paths for row in exhibits),
            "Exhibit missing from checksum manifest")
    print(f"Verified {len(records)} output checksums and {len(exhibits)} exhibits.")
    return status


def verify_top10_audit(status):
    detail_path = "diagnostics/top10_depth_comparison.csv"
    summary_path = "diagnostics/top10_depth_summary.csv"
    require(status["top10_depth_outputs"] == [detail_path, summary_path],
            "Unexpected top-10 output paths in run status")
    detail = read_csv(RESULTS / detail_path)
    summary = read_csv(RESULTS / summary_path)
    require(len(detail) == status["top10_depth_comparison_rows"] == 288,
            "Unexpected detailed top-10 row count")
    require(len(summary) == status["top10_depth_summary_rows"] == 8,
            "Unexpected top-10 summary row count")

    group_columns = ("protocol", "window", "depth", "reference_depth")
    categories = ("unchanged_top10", "order_only_changed", "items_changed")
    counts = defaultdict(Counter)
    detail_keys = set()
    for row in detail:
        key = tuple(row[column] for column in group_columns)
        detail_key = (*key, row["seed"], row["candidate"])
        require(detail_key not in detail_keys, f"Duplicate top-10 comparison: {detail_key}")
        detail_keys.add(detail_key)
        values = {column: int(row[column]) for column in categories}
        users = int(row["users"])
        changed = int(row["any_change"])
        require(users > 0 and all(value >= 0 for value in values.values()) and
                users == sum(values.values()) and changed == users - values["unchanged_top10"],
                f"Invalid top-10 comparison counts: {detail_key}")
        require(abs(float(row["any_change_rate"]) - changed / users) < 1e-12,
                f"Invalid top-10 comparison rate: {detail_key}")
        counts[key].update(values)
        counts[key].update(comparison_cells=1, user_list_pairs=users, any_change=changed)

    expected_groups = {(protocol, window, depth, "100")
                       for protocol in ("100k", "1m")
                       for window in ("val", "test") for depth in ("50", "200")}
    summary_keys = set()
    for row in summary:
        key = tuple(row[column] for column in group_columns)
        require(key in counts and key not in summary_keys, f"Unexpected top-10 summary group: {key}")
        summary_keys.add(key)
        totals = counts[key]
        require(totals["comparison_cells"] == 36 and
                all(int(row[column]) == value for column, value in totals.items()),
                f"Top-10 summary disagrees with detail: {key}")
        require(abs(float(row["any_change_rate"]) -
                    totals["any_change"] / totals["user_list_pairs"]) < 1e-12,
                f"Invalid top-10 summary rate: {key}")
    require(summary_keys == set(counts) == expected_groups,
            "Top-10 audit does not cover the expected protocols, periods and depths")
    pairs = sum(group["user_list_pairs"] for group in counts.values())
    changes = sum(group["any_change"] for group in counts.values())
    print(f"Verified top-10 depth audit: {pairs:,} paired lists, {changes:,} changed.")


if __name__ == "__main__":
    verify_notebooks(read_json(ROOT / "docs/artifact-provenance.json"))
    verify_top10_audit(verify_results())
    print("Verified the executed notebook and clean rerun copy.")
