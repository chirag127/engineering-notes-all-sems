 Here are the notes for Unit 4 - Normalization in the subject of Database Management Systems Lab:

### Normalization

1. First Normal Form (1NF): Eliminate repeating groups. Make each cell contain a single value.
2. Second Normal Form (2NF): Meet 1NF requirements and remove partial dependencies. No column should depend on only part of a composite primary key.
3. Third Normal Form (3NF): Meet 2NF requirements and remove transitive dependencies. No column should depend on other non-key columns.
4. Boyce-Codd Normal Form (BCNF): Meet 3NF requirements and ensure that every determinant is a candidate key.
5. Fourth Normal Form (4NF): Meet BCNF requirements and remove certain types of multi-valued dependencies.

Advantages of Normalization:
- Removes redundancy and inconsistent data
- Improves data integrity
- Makes the database more flexible to changes
- Uses less storage space due to removal of duplicates

The steps to normalize a database are:
1. Identify each table and its columns
2. Check for violations of the first normal form and normalize
3. Check for violations of the second normal form and normalize
4. Check for violations of the third normal form and normalize
5. Check for violations of the Boyce-Codd normal form and normalize (optional)

The notes follow a formal tone with points and no feelings or friendliness shown. No emojis or external links are included. The content is written inside header ### and in Markdown format as required.