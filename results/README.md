# Revised results

Full Kaggle CPU run on 25 November 2026. Each research question has two CSV tables and two PDF figures. RQ4 also includes two supporting diagnostic CSVs.

## RQ1 · Objective disagreement

How often do the fairness objectives favor different configurations?

- [Validation relevance, eligibility and ties by configuration](tables/RQ1_T1_relevance_and_winners.csv) (CSV)
- [Cross-objective winner agreement with unassessable comparisons marked](figures/RQ1_F1_winner_agreement.pdf) (PDF)
- [Candidate winner support, complete draws and pairwise ordering retention](tables/RQ1_T2_rank_and_winner_support.csv) (CSV)
- [Three highest winner supports per objective, first fitting seed](figures/RQ1_F2_winner_support.pdf) (PDF)

## RQ2 · Uncertainty and abstention

Which contrasts have statistical support, and when does selection abstain?

- [All planned base versus reranker contrasts and simultaneous intervals](tables/RQ2_T1_contrasts_and_intervals.csv) (CSV)
- [Validation evidence and later reversals with explicit denominators](tables/RQ2_T2_evidence_and_reversals.csv) (CSV)
- [Evidence classification across objectives, including unavailable contrasts](figures/RQ2_F1_contrast_evidence.pdf) (PDF)
- [Selection, threshold abstention and estimability failures by cutoff](figures/RQ2_F2_decisions_by_cutoff.pdf) (PDF)

## RQ3 · Shortlist trade-offs

How do the rules compare on size, overlap and later-frontier performance?

- [Selector scorecard with audit, overlap and later quality denominators](tables/RQ3_T1_selector_scorecard.csv) (CSV)
- [Within-audit bootstrap minus comparator differences and interquartile ranges](tables/RQ3_T2_paired_control_differences.csv) (CSV)
- [Stability against shortlist size, one point per fitting seed](figures/RQ3_F1_stability_and_selectivity.pdf) (PDF)
- [Later-frontier coverage and dominated selections in the frozen validation pool](figures/RQ3_F2_later_frontier_tradeoff.pdf) (PDF)

## RQ4 · Coverage and candidate depth

How do demographic definitions and retrieval depth affect the audit?

- [Observed and eligible demographic groups by period, including intersections](tables/RQ4_T1_demographic_coverage.csv) (CSV)
- [RQ1–RQ3 changes against the reference retrieval depth](tables/RQ4_T2_paired_depth_sensitivity.csv) (CSV)
- [Group completeness by demographic definition, with smallest cell counts](figures/RQ4_F1_group_estimability.pdf) (PDF)
- [Candidate recall across depths, with ranges over fitting seeds](figures/RQ4_F2_candidate_recall.pdf) (PDF)
- [Final top-10 list comparison by protocol, fitting seed, period, configuration and depth](diagnostics/top10_depth_comparison.csv) (CSV, 288 rows)
- [Final top-10 list comparison summarized by protocol, period and depth](diagnostics/top10_depth_summary.csv) (CSV, eight rows)

The top-10 audit uses depth 100 as the reference and compares the same users and configurations at depths 50 and 200. Each pair of lists falls into one of three categories. The ordered lists can be identical, contain the same items in a different order, or contain different items. All 46,512 pairs in the archived run were identical.

## RQ5 · Scope of transfer

How do shared calibration and exposure outcomes compare across protocols?

- [Cohort sizes, chronology and admissible fairness objectives](tables/RQ5_T1_protocol_scope.csv) (CSV)
- [Selector outcomes by protocol and objective set, with a common calibration/exposure comparison](tables/RQ5_T2_cross_protocol_selectors.csv) (CSV)
- [Calibration versus exposure winner agreement, with one point per fitting seed](figures/RQ5_F1_shared_objective_agreement.pdf) (PDF)
- [Retrospective set overlap and frontier coverage on shared objectives](figures/RQ5_F2_later_selection_transfer.pdf) (PDF)

## Supporting files

- [Diagnostics](diagnostics/) includes the audit registry, retrieval recall, threshold results and contrast evidence.
- [Run manifest](manifest/) includes the configuration, dataset provenance, tuning records, exhibit inventory, completion status and SHA-256 checksums.
