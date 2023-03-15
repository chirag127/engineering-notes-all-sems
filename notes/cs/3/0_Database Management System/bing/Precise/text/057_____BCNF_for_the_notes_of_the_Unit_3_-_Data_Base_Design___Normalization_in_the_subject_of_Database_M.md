### BCNF (Boyce-Codd Normal Form)

BCNF is a higher form of normalization that is used to reduce redundancy in relational databases. It is a stricter version of the Third Normal Form (3NF). A relation is in BCNF if, for every non-trivial functional dependency X → Y, X is a superkey.

- **Superkey**: A superkey is a set of attributes that uniquely identifies a tuple in a relation. A superkey may contain extraneous attributes, meaning attributes that are not necessary for unique identification.

- **BCNF Decomposition**: If a relation is not in BCNF, it can be decomposed into multiple relations that are in BCNF. This is done by identifying a determinant that is not a superkey and splitting the relation into two relations, one containing the determinant and the dependent attributes, and the other containing the determinant and the remaining attributes.

- **Lossless Join Property**: A decomposition is lossless if the natural join of the decomposed relations results in the original relation. This property ensures that no information is lost during the decomposition process.

- **Dependency Preservation Property**: A decomposition is dependency preserving if the functional dependencies of the original relation can be derived from the functional dependencies of the decomposed relations. This property ensures that the constraints of the original relation are preserved in the decomposed relations.

BCNF is an important concept in database design and normalization, as it helps to reduce redundancy and improve the efficiency of the database. It is important to note that not all relations can be decomposed into BCNF while preserving both the lossless join and dependency preservation properties. In such cases, a trade-off must be made between the two properties.