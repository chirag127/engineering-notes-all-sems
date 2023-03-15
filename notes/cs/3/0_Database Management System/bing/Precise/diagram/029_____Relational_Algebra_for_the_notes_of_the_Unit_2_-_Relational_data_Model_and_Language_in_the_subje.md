### Relational Algebra

Relational algebra is a procedural query language, which takes instances of relations as input and yields instances of relations as output. It uses operators to perform queries. An operator can be either unary or binary. They accept relations as their input and return relations as their output. Relational algebra is performed recursively on a relation, and intermediate results are also considered relations.

The fundamental operations of relational algebra are as follows:

1. **Select** - The select operation selects tuples that satisfy a given predicate. We use the lowercase Greek letter sigma (σ) to denote selection. The predicate appears as a subscript to the sigma.

2. **Project** - The project operation is used to select a subset of the attributes of a relation by specifying the names of the required attributes. We use the Greek letter pi (π) to denote projection.

3. **Union** - The union operation is used to combine the tuples of two relations that are union-compatible. Two relations are union-compatible if they have the same number of attributes and the domains of the corresponding attributes are the same.

4. **Set difference** - The set difference operation is used to find the tuples that are in one relation but not in another. The two relations must be union-compatible.

5. **Cartesian product** - The Cartesian product operation is used to combine tuples from two relations. The result is a new relation that contains all possible combinations of tuples from the two input relations.

6. **Rename** - The rename operation is used to rename the attributes of a relation.

These are the basic operations of relational algebra. Other operations, such as intersection, division, join, and assignment, can be derived from these basic operations. These operations allow us to manipulate the data stored in relations to extract the information we need.