# Changelog

## v1.1.0 · top-10 depth audit · run dated 2026-11-25

- Added a direct, paired comparison of ordered top-10 recommendations at retrieval depths 50 and 200 against depth 100 in both global MovieLens protocols.
- Exported 288 detailed comparison rows and eight summary rows. All 46,512 paired top-10 lists in this run were identical at the audited depths.
- Updated both notebook copies and the complete results tree to match the 25 November run. The 26 shared results CSVs match the 23 November run byte for byte.
- Extended verification to reconcile the detailed and summary audit counts.

## Intermediate revision · run dated 2026-11-23

- Updated the notebook and results for the five revised research questions.
- Added a paired retrieval-depth comparison at 50, 100, and 200, a demographic estimability diagnostic, and a shared calibration/exposure comparison across four protocols.
- Used 24 outer audits and 300 inner draws for the revised selector comparisons. The earlier global analysis used 50 and 1,000, respectively.
- Packaged an executed notebook, an output-free rerun copy and a browsable results tree with a checksum verifier.

## v1.0.0 · earlier archived protocol

The earlier [GitHub release](https://github.com/Cosmicrider1166/phantom-troupe-project9/releases/tag/v1.0.0) and [Zenodo record](https://doi.org/10.5281/zenodo.24093518) include the original proposal and outputs. Preference drift, profile-strategy comparisons, and the feasibility-adapted DPFR analysis belong to that version.
