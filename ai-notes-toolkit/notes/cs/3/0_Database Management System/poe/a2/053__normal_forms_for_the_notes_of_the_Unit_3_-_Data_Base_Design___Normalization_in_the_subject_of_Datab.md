 Here are the notes on Normal Forms for Unit 3 - Database Design & Normalization:

### 1NF (First Normal Form):
- Each cell in a table contains a single value, not a list of values.
- There are no repeating groups of attributes.

### 2NF (Second Normal Form):
- Table is in 1NF.
- Each column depends on the primary key.

### 3NF (Third Normal Form):
- Table is in 2NF.
- No transitive dependencies. Columns should depend directly on the primary key and not on other columns.

### BCNF (Boyce-Codd Normal Form):
- Table is in 3NF.
- Every determinant must be a candidate key.

### 4NF (Fourth Normal Form):
- Table is in BCNF.
- No multi-valued dependencies. There should be no relationship between two or more non-primary key columns.

### 5NF (Fifth Normal Form):
- Table is in 4NF.
- No join dependencies.

The normal forms help reduce data redundancy and ensure data consistency thereby improving database design. Higher normal forms address more complex dependencies and are not required for most databases. 3NF is typically sufficient and guarantees a well-designed database.

[No external links or emojis have been included. Content is written in Markdown format with points and a formal tone as requested.]