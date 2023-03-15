### Relational Algebra

- Relational algebra is a theory that uses algebraic structures for modeling data, and defining queries on it with a well founded semantics.
- Relational algebra is a procedural query language, where the user tells the system to carry out a set of operations to obtain the desired results.
- Relational algebra provides a theoretical foundation for relational databases, particularly query languages for such databases, chief among which is SQL.
- Relational databases store tabular data represented as relations. Queries over relational databases often likewise return tabular data represented as relations.
- Relational algebra operations are designed to do the most common things that we need to do with relations in a database.

#### Basic Relational Algebra Operations

- **SELECT** (σ): The SELECT operation is used for selecting a subset of the tuples according to a given selection condition . For example, σ<sub>age > 20</sub>(Student) selects all the tuples from the Student relation where the age attribute is greater than 20.
- **PROJECT** (π): The PROJECT operation is used for eliminating all attributes of the input relation but those mentioned in the projection list . For example, π<sub>name, age</sub>(Student) returns a relation with only the name and age attributes of the Student relation.
- **UNION** (∪): The UNION operation is used for combining two relations that have the same set of attributes . For example, Student ∪ Teacher returns a relation that contains all the tuples from both Student and Teacher relations. The result relation does not have any duplicate tuples.
- **INTERSECTION** (∩): The INTERSECTION operation is used for finding the common tuples between two relations that have the same set of attributes . For example, Student ∩ Teacher returns a relation that contains only the tuples that are present in both Student and Teacher relations.
- **DIFFERENCE** (-): The DIFFERENCE operation is used for finding the tuples that are present in one relation but not in another relation that have the same set of attributes . For example, Student - Teacher returns a relation that contains only the tuples that are present in Student but not in Teacher relation.
- **CARTESIAN PRODUCT** (×): The CARTESIAN PRODUCT operation is used for combining every tuple of one relation with every tuple of another relation . For example, Student × Course returns a relation that contains all possible pairs of tuples from Student and Course relations. The result relation has the attributes of both the input relations.