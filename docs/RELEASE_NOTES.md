# Project 9 v1.1.0 release notes

**Release title** · Revised fairness audit with direct top-10 depth comparisons

This release packages the completed 25 November 2026 Kaggle run of the revised five-question study. It adds a direct comparison of final ranked top-10 lists at retrieval depths 50 and 200 against the depth-100 reference. The comparison covers both global MovieLens protocols, validation and test, three fitting seeds and 12 recommender configurations. All 46,512 paired lists matched in both items and order. The counts describe the evaluated configurations and protocols.

- [Executed notebook](../notebooks/project9_revised_executed.ipynb) and [clean rerun notebook](../notebooks/project9_revised.ipynb)
- [Results index](../results/README.md) with 10 PDF figures and 10 CSV exhibit tables
- [Detailed depth comparisons](../results/diagnostics/top10_depth_comparison.csv) and [summary](../results/diagnostics/top10_depth_summary.csv)
- [Reproduction guide](REPRODUCING.md) and [artifact provenance](artifact-provenance.json)

## Publish in the existing repository

1. Extract the ZIP into a separate folder. Use the **contents** of `phantom-troupe-project9/` as the release tree, including the hidden GitHub workflow and Git configuration files.
2. In a clean checkout of `Cosmicrider1166/phantom-troupe-project9`, create a release branch and copy in the release tree. Replace the previously tracked Project 9 notebook and result paths with the new `notebooks/` and `results/` trees. Review the staged changes and retain any unrelated repository files. The repository's existing history and prior release provide access to earlier artifacts.
3. From the repository root, run `python scripts/verify_release.py`. Commit the update and merge it through the repository's normal workflow. Review the GitHub Actions verification result.
4. Confirm that `v1.1.0` is available, then create a release with that tag from the verified commit. Use the title and summary above. The ZIP can also be attached as a release asset.

The earlier [Zenodo DOI](https://doi.org/10.5281/zenodo.24093518) identifies version 1.0.0. Cite the GitHub release or commit for this version.
