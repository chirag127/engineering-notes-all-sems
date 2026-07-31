

### Lossless Join Decompositions

* Lossless join decompositions are a type of data decomposition used in database design and normalization.
* This type of decomposition allows for the retrieval of the original relation when the decomposed relations are joined together.
* In order to ensure that the original relation can be retrieved, the following conditions must be met:
  * All attributes in the original relation must appear in at least one of the decomposed relations.
  * The join condition must involve all attributes that appear in more than one of the decomposed relations.
  * The join condition must be a conjunction of equalities.
* Lossless join decompositions are useful for improving the performance of query processing as well as for reducing the amount of data redundancy in a database.