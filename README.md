# Phantom Troupe Project 9

## Recommender fairness selection: persistence, uncertainty, coverage and feasibility

**Team:** Phantom Troupe  
**Authors:** Tony Nicholas Panneer Jesuraja and Parvesh Kumar  
**Target journal:** *Expert Systems with Applications*

This repository accompanies an exploratory empirical study of decision instability when recommender systems are assessed using different fairness objectives. It examines what is retained, lost or left unresolved when bootstrap-supported Pareto shortlists replace individual objective winners or point-estimate Pareto sets.

The contribution is an empirical audit of the trade-offs between shortlist size, selection persistence, later dominated selections, frontier recall, abstention and statistical uncertainty. The project does not claim to introduce Pareto optimality, bootstrap resampling or concentration bounds.

## Repository files

Use the following filenames when uploading the final submission. The notebook must be the **combined executed notebook**, including the executed figure-readability update cells and their outputs.

| File | Contents |
| --- | --- |
| `Project9_Final_Executed.ipynb` | Complete executed analysis, saved outputs, figure updates and archive-generation code. |
| `Project9_Final_Results.zip` | Complete final results archive, including the readability-v2 figures, CSV tables, manifests and reference code. |
| `Final_Proposal.docx` | Finalized proposal used to develop the project. |
| `Target_Journal.txt` | Target journal: Expert Systems with Applications. |
| `README.md` | Project overview, execution instructions, interpretation and licensing scope. |
| `LICENSE` | MIT license for original project code and accompanying documentation. |

If files are uploaded under their original downloaded names, identify them clearly in the repository. Renaming a downloaded copy does not change its contents.

The final archived study run is `20261109T180151_afe6d1`. Its readability-v2 ZIP is originally named `Phantom_Troupe_Project9_Full_Results_Readability_v2_20261109T180151_afe6d1.zip`.

## Research questions explored

The notebook preserves the five research questions in the proposal. Their analysis areas are:

1. **RQ1 — Objective disagreement:** how demographic utility gap, genre calibration and item-exposure concentration disagree about candidate rankings and winners.
2. **RQ2 — Uncertainty and later reversals:** what simultaneous uncertainty assessments establish about reranking gains, and how observed gains change sign in later evaluation windows.
3. **RQ3 — Selection trade-offs:** shortlist stability, size, abstention, later dominated selections, frontier recall, threshold sensitivity and matched controls.
4. **RQ4 — Demographic resolution and composition:** how sparse groups, composition changes and training-activity strata affect evaluability and selection behavior.
5. **RQ5 — Histories and profile strategies:** observed profile drift, calibration reversals, profile-strategy shortlist stability and demographic-gap changes.

These descriptions summarize the implemented endpoints; the proposal contains the formal research-question wording.

## Datasets and evaluation protocols

Download the datasets separately from the original providers and retain their README files and terms of use.

| Dataset | Official download | Role in this study |
| --- | --- | --- |
| MovieLens 100K | [ml-100k.zip](https://files.grouplens.org/datasets/movielens/ml-100k.zip) | Original global-chronological protocol; sparse-group feasibility is explicitly reported. |
| MovieLens 1M | [ml-1m.zip](https://files.grouplens.org/datasets/movielens/ml-1m.zip) | Original bounded-user global-chronological protocol and a separate full-release within-user chronological sensitivity analysis. |
| HetRec 2011 Last.fm 2K | [hetrec2011-lastfm-2k.zip](https://files.grouplens.org/datasets/hetrec2011/hetrec2011-lastfm-2k.zip) | Independent partial-domain replication for tag calibration and item exposure. |

Provider documentation: [MovieLens](https://grouplens.org/datasets/movielens/) and [HetRec 2011](https://grouplens.org/datasets/hetrec-2011/).

**Last.fm task definition:** the notebook uses the first observed user–artist tagging-interaction timestamp. It does not reconstruct chronological listening histories. Tags are not asserted to be movie genres, and demographic attributes are not inferred or synthesized.

The full-1M within-user chronology changes the evaluation target. It is a related-data sensitivity analysis, not an independent global-time deployment replication. Last.fm evaluates only the objectives supported by its available information.

## Methods and reproducibility

- CPU baselines: popularity, item-based nearest neighbours and explicit-rating matrix factorization.
- Genre/tag-aware reranking at weights `0.0`, `0.1`, `0.3` and `0.5`.
- Main evaluation at top 10, with configured top-5/top-20 sensitivity outputs.
- NDCG relevance screens; demographic utility ranges; Jensen–Shannon calibration divergence; catalogue-exposure Gini.
- Prespecified fitting seeds: `20261101`, `20261102` and `20261103`.
- Stable hashed user roles separate hyperparameter-tuning users from audit users.
- Main nested audits: 50 outer resamples and 1,000 inner bootstrap draws; post-review dense/profile analyses use their separately recorded settings.
- Size-matched random and relevance-ranked controls, explicit missingness/abstention accounting, and later-frontier configuration recall.
- Conservative simultaneous bounded-mean coordinate envelopes for primary contrast assessment; legacy bootstrap intervals remain secondary exploratory diagnostics.
- Full 27-contrast simulation diagnostics with tied extrema, sparse groups, coverage uncertainty and interval width.

The authoritative configuration and runtime package versions are in `manifest/protocol.json` and `manifest/environment.json` inside the results ZIP. Private checkpoints and prediction caches are kept outside the public results folder.

### DPFR comparator boundary

The reported comparator is **FeasibilityAdaptedDPFR**, derived from the pinned WWW 2025 [DPFR author repository](https://github.com/theresiavr/DPFR-recsys-evaluation), commit `d5ca1dfbcbe67f587d55493381d5601fbcd21c61`.

The adaptation adds explicit pandas copies and guards for proposed replacements with no eligible user. It can search feasible frequency-improving swaps and label a constrained one-swap local optimum. It is not claimed to reproduce the original algorithm end to end, reproduce the separate 2026 extension, or obtain an unconstrained global oracle.

Strict-original diagnostics, metric-equivalence fixtures, source hashes, adapted reference status and modification records are retained in the archive. Failed executions are unavailable observations, not zero-recall operational abstentions. Matched comparisons use the supported NDCG/unweighted-Gini pair.

## Running on Kaggle

1. Create a Kaggle notebook and import `Project9_Final_Executed.ipynb`.
2. Attach MovieLens 100K, MovieLens 1M and HetRec 2011 Last.fm 2K as inputs. Official ZIPs or the supported extracted files can be used.
3. Use a CPU session. Internet is unnecessary when all required inputs are attached; otherwise the Last.fm loader can attempt the official download.
4. Run cells from top to bottom. Saved outputs show the archived execution; rerunning creates a new run and new results.
5. Let long cells finish and follow the progress messages. Section 25 saves private completed-stage and partial-regression checkpoints. Rerunning that cell in the same live session can resume these checkpoints; a fresh kernel still needs the earlier project state.
6. Run the appended readability-update cells after the complete scientific analysis. They read saved CSVs, redraw the figures and package a separate complete results copy.
7. Run the final archive cell. It verifies file hashes and ZIP integrity and prints the full archive path.
8. Save a Kaggle version to persist the outputs, then download the final ZIP from that saved version's Output files.

The reference run took approximately 2 hours and 4 minutes; Section 25 took 14.1 minutes. These are observations from one environment, not runtime guarantees.

Principal dependencies are Python, NumPy, pandas, SciPy, scikit-learn, Numba, Matplotlib, seaborn, threadpoolctl and IPython. Consult the recorded environment rather than assuming identical versions on another machine.

## Results archive

The final archive contains:

| Folder | Contents |
| --- | --- |
| `figures/` | 18 PDF figures, including the final readability updates. |
| `tables/` | 91 CSV files: 90 scientific result tables and one display-output inventory. |
| `manifest/` | Configuration, dataset provenance, environment details, validation reports, figure-update records and file checksums. |
| `reference_code/` | Pinned reference sources, the disclosed feasibility adaptation, helper code and retained third-party licenses. |
| `logs/` | Run-log directory where populated by the analysis. |

The readability update preserves the scientific CSVs and plotted coordinates. It improves labels, layout and print sizing, separates fitting seeds into panels where appropriate, and uses concentric outlines for coincident points. Display-inventory captions are presentation metadata and are updated accordingly.

Figures are exported at **180 mm width**. Use them at that width, or check effective text size after resizing in the manuscript. Final Word/LaTeX page layout still requires a visual proof check.

## Findings and interpretation

In the original MovieLens 1M global protocol, bootstrap-supported shortlists contain fewer candidates and have fewer later dominated selections than point Pareto sets, while retaining fewer later-frontier alternatives and showing lower union-overlap stability. Other protocols show different patterns; universal stability improvement is not supported.

The final run completed its recorded technical checks, including all 308 feasibility-adapted reference evaluations. Successful checks establish only their stated conditions; they do not certify originality, journal acceptance or correctness under every possible data-generating process.

Important limitations:

- Analyses follow inspection of earlier project results and are exploratory, not preregistered confirmation.
- Conservative primary bounds support no positive contrasts in this run and can retain the entire relevance-eligible pool.
- The dense-profile comparisons do not establish noninferiority at the declared margin; lack of detected worsening is not proof of no harm.
- Some original 100K demographic endpoints are not estimable. Missing groups are not silently removed or imputed as equal utility.
- Fitting seeds and user resamples are not independent datasets. Fixed-model user resampling does not cover all retraining uncertainty.
- This is an observational evaluation, not evidence of causal discrimination or a universal fairness guarantee.

## License and third-party material

Original project code and accompanying documentation are offered under the **MIT License**; see the repository's `LICENSE` file. Retain the copyright and permission notices when reusing that material.

Third-party code remains subject to its own retained notices. The bundled DPFR sources carry an MIT notice for `theresiavr` (2025), and the bundled RecBole sources carry an MIT notice for `RUCAIBox` (2020). Their original notices are included under `reference_code/` in the results archive.

**The project license does not relicense the datasets.** MovieLens releases have their own research-use conditions, including restrictions on redistribution and commercial use. HetRec Last.fm data is provided for non-commercial use. Obtain the data from the official links and follow the terms in each release's README. Do not add the raw dataset ZIPs to this repository under the project's MIT license.

This software-code license statement does not assign a separate Creative Commons license to the proposal or dataset-derived outputs. Consult their applicable notices before redistribution or reuse beyond the stated code/documentation scope.

## References and citation

- Harper, F. M., and Konstan, J. A. (2015). *The MovieLens Datasets: History and Context.* ACM Transactions on Interactive Intelligent Systems. [DOI: 10.1145/2827872](https://doi.org/10.1145/2827872).
- Cantador, I., Brusilovsky, P., and Kuflik, T. (2011). *2nd Workshop on Information Heterogeneity and Fusion in Recommender Systems (HetRec 2011).* Proceedings of ACM RecSys. See the dataset README for acknowledgements and citation details; acknowledge [Last.fm](https://www.last.fm/).
- Rampisela and colleagues (2025). *Joint Evaluation of Fairness and Relevance in Recommender Systems with Pareto Frontier.* [DOI: 10.1145/3696410.3714589](https://doi.org/10.1145/3696410.3714589).

## Archived notebook and results

The final executed notebook, complete results ZIP, finalized proposal, and supporting documentation are archived on Zenodo.

- **Version:** 1.0.0
- **DOI:** [10.5281/zenodo.24093518](https://doi.org/10.5281/zenodo.24093518)
- **GitHub repository:** [phantom-troupe-project9](https://github.com/Cosmicrider1166/phantom-troupe-project9)

Please cite the version-specific Zenodo DOI above when referring to the archived code and results.
