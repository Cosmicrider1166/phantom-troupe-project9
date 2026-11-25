# Reproduce the revised study

Start with [the clean notebook](../notebooks/project9_revised.ipynb). The [executed export](../notebooks/project9_revised_executed.ipynb) records the completed Kaggle run. Both contain the same code and markdown.

## Kaggle

1. Import the clean notebook and attach the three official inputs listed in [DATA.md](DATA.md). MovieLens inputs may be official ZIPs or extracted releases. For Last.fm, use the official ZIP or attach the extracted dataset under Kaggle's input directory.
2. Set the accelerator to **None (CPU)**. The notebook defaults to full mode. Internet access is only needed if the notebook must download the Last.fm ZIP.
3. Use **Save Version → Save & Run All**. The last cell verifies and packages 10 figures and 10 exhibit tables with diagnostics, configuration and checksums. The RQ4 section previews the top-10 depth summary and links to both CSVs. Download the generated `Project9_full_*.zip` from the run output.

## Local CPU

Use Python 3.13 for the recorded analysis dependency versions. See [configuration.json](../results/manifest/configuration.json) for the actual Kaggle versions. The requirements file pins the recorded analysis libraries and lists the additional notebook tooling.

From the repository root, create a virtual environment, activate it, and install the dependencies.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
mkdir -p upload
```

Put the three official ZIPs in `upload/`. Execute from the repository root so that the notebook sees the expected working directory.

```bash
python - <<'PY'
import os
from pathlib import Path
import nbformat
from nbclient import NotebookClient

mode = os.environ.setdefault("PROJECT9_MODE", "full")
source = Path("notebooks/project9_revised.ipynb")
notebook = nbformat.read(source, as_version=4)
NotebookClient(
    notebook, timeout=3600, kernel_name="python3",
    resources={"metadata": {"path": str(Path.cwd())}},
).execute()
run = max(Path.cwd().glob(f"Project9_{mode}_*/manifest/run_status.json"),
          key=lambda path: path.stat().st_mtime_ns).parents[1]
nbformat.write(notebook, run.with_suffix(".ipynb"))
print(run.with_suffix(".zip"))
PY
```

For a synthetic smoke run, set `PROJECT9_MODE=smoke` in your shell before running the command. It requires no datasets. Synthetic results are for checking the pipeline. To compare a fresh full run with the reference, consult the configuration and compare CSV values. ZIP filenames, timing, paths, and some rendered-file metadata can vary between runs.

## Audit the supplied run

Run `python scripts/verify_release.py` from the root. It checks notebook source parity, 56 output checksums, the 20-exhibit inventory and the reconciliation of the top-10 diagnostics. The executed notebook and original Kaggle ZIP hashes are recorded in [artifact-provenance.json](artifact-provenance.json).
