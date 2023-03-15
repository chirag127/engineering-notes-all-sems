# Keys Constraints

- A key is a set of one or more attributes that uniquely identifies a tuple in a relation.
- A key constraint is a rule that specifies that no two tuples in a relation can have the same values for the key attributes.
- A key constraint ensures the integrity and consistency of the data in a relation.
- There are different types of keys in a relational data model, such as:

  - **Superkey**: A superkey is a set of attributes that contains a key. A superkey may have additional attributes that are not necessary for uniqueness.
  - **Candidate key**: A candidate key is a minimal superkey, that is, a superkey that does not have any redundant attributes. A relation may have more than one candidate key.
  - **Primary key**: A primary key is a designated candidate key that is chosen by the database designer to identify tuples in a relation. A relation can have only one primary key.
  - **Foreign key**: A foreign key is a set of attributes in a relation that references the primary key of another relation. A foreign key establishes a relationship between two relations and enforces referential integrity.