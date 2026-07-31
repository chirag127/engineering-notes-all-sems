### Keys Constraints

- A key is a set of one or more attributes that uniquely identifies a tuple in a relation.
- A key constraint is a rule that specifies that the values of a key must be distinct for every tuple in a relation.
- There are different types of keys and constraints in the relational data model, such as:

  - **Superkey**: A superkey is a set of attributes that contains a key. A superkey may have additional attributes that are not necessary for unique identification.
  - **Candidate key**: A candidate key is a minimal superkey, that is, a superkey that does not contain any redundant attribute. A relation may have more than one candidate key.
  - **Primary key**: A primary key is a designated candidate key that is used to identify tuples in a relation. A relation can have only one primary key. A primary key cannot have null values.
  - **Foreign key**: A foreign key is a set of attributes in a relation that references the primary key of another relation. A foreign key establishes a referential integrity constraint between the two relations.
  - **Alternate key**: An alternate key is a candidate key that is not chosen as the primary key. An alternate key can be used as a secondary means of identification.
  - **Composite key**: A composite key is a key that consists of two or more attributes. A composite key can be a superkey, a candidate key, a primary key, or a foreign key.