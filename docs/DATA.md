# Datasets

| Input | Official source | Role in the revised protocol |
| --- | --- | --- |
| `ml-100k.zip` | [MovieLens 100K](https://grouplens.org/datasets/movielens/100k/) | Global chronological movie evaluation. |
| `ml-1m.zip` | [MovieLens 1M](https://grouplens.org/datasets/movielens/1m/) | Fixed 3,000-user sample for global evaluation and the full release for within-user chronology. |
| `hetrec2011-lastfm-2k.zip` | [HetRec 2011 datasets](https://grouplens.org/datasets/hetrec-2011/) | Tag calibration and item exposure using user–artist tagging events. |

Use the official releases and follow the terms in their README files. Raw ratings, user records, and tagging inputs are downloaded from the providers. Input names, provenance and digests from the completed run appear in [results/manifest/](../results/manifest/). Digests for extracted MovieLens folders use the notebook's directory digest scheme.

### Dataset references

- Harper, F. M., & Konstan, J. A. (2015). The MovieLens Datasets: History and Context. *ACM Transactions on Interactive Intelligent Systems, 5*(4), Article 19. [DOI](https://doi.org/10.1145/2827872)
- Cantador, I., Brusilovsky, P., & Kuflik, T. (2011). Second Workshop on Information Heterogeneity and Fusion in Recommender Systems (HetRec 2011). *Proceedings of the Fifth ACM Conference on Recommender Systems*. [DOI](https://doi.org/10.1145/2043932.2044016)
