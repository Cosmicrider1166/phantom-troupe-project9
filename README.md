# Selecting Recommender Systems When Fairness Rankings Are Unstable

**Phantom Troupe · Project 9 · v1.1.0**

Tony Nicholas Panneer Jesuraja and Parvesh Kumar · University of Europe for Applied Sciences

This study asks which recommender configurations remain worth shortlisting when demographic utility, calibration, and item exposure favor different choices. It compares selection rules on chronological MovieLens and Last.fm evaluations and reports how often subgroup sparsity or uncertainty makes it difficult to issue a shortlist.

**Start here** · [Executed notebook](notebooks/project9_revised_executed.ipynb) · [Run instructions](docs/REPRODUCING.md) · [Results by research question](results/README.md) · [Release notes](docs/RELEASE_NOTES.md)

## Top-10 retrieval-depth audit

The 25 November 2026 run compares the final ordered top-10 lists at retrieval depths 50 and 200 against depth 100. Across 46,512 paired lists from the global MovieLens 100K and 1M protocols, all ten items and their positions were identical in every comparison. These comparisons span validation and test, three fitting seeds and 12 candidate configurations. The count refers to paired lists, with users appearing in multiple comparisons. Candidate recall still improved with deeper retrieval in the evaluated protocols.

[Depth audit summary](results/diagnostics/top10_depth_summary.csv) · [Detailed counts](results/diagnostics/top10_depth_comparison.csv) · [Candidate recall](results/figures/RQ4_F2_candidate_recall.pdf)

## Main result

In the revised global MovieLens 1M audit at retrieval depth 100, bootstrap-supported Pareto selection produced smaller shortlists with a lower share of later-dominated choices. It also retained fewer candidates from the later Pareto frontier. The table compares selection rules within the same validation-screened candidate pools.

| Measure | Bootstrap-supported Pareto | Point-estimate Pareto |
| --- | ---: | ---: |
| Mean shortlist size | 1.25 | 2.71 |
| Later-dominated share among issued shortlists | 6.5% | 40.3% |
| Later-frontier recall | 74.3% | 89.6% |
| Across-audit overlap, union Jaccard | 0.298 | 0.280 |

[Source table and denominators](results/tables/RQ3_T1_selector_scorecard.csv) · [Later-frontier figure](results/figures/RQ3_F2_later_frontier_tradeoff.pdf)

The overlap ordering differs from the earlier archived protocol. In MovieLens 100K, bootstrap Pareto returned an empty shortlist in 23 of 24 audits per fitting seed. Last.fm compares calibration and exposure, and its full validation cohort had one relevance-eligible configuration. The revised protocol was developed after inspection of earlier results, so the findings are exploratory.

## Repository map

| Path | Contents |
| --- | --- |
| [notebooks/](notebooks/) | Original executed Kaggle export and clean rerun copy with identical cell sources. |
| [results/](results/) | All 10 figures, 10 exhibit tables, 17 diagnostic CSVs and run manifests from 25 November 2026. |
| [docs/](docs/) | Dataset sources, reproduction instructions, and artifact provenance. |
| [scripts/verify_release.py](scripts/verify_release.py) | Verifies archived files, notebook source parity and consistency of the top-10 diagnostics. |
| [CITATION.cff](CITATION.cff) · [CHANGELOG.md](CHANGELOG.md) | Citation metadata and version history. |

## Verify the bundled results

Run from the repository root using Python 3.10 or later. The verification uses only the standard library and checks the archived artifacts. See the reproduction guide to recompute them.

```bash
python scripts/verify_release.py
```

## Cite and reuse

Cite the GitHub release or commit you use. The DOI [10.5281/zenodo.24093518](https://doi.org/10.5281/zenodo.24093518) identifies the **earlier v1.0.0 archive**, which contains the earlier protocol, proposal, notebook and results. The earlier [GitHub release](https://github.com/Cosmicrider1166/phantom-troupe-project9/releases/tag/v1.0.0) also provides those materials.

Project source code is available under the [MIT License](LICENSE). Dataset terms and citations are listed in the [dataset guide](docs/DATA.md).
