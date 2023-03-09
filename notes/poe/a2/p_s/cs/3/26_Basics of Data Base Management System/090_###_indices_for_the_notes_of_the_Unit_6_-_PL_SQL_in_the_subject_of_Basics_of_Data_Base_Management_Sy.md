 Here is the content in Markdown format for the topic ### indices for the notes of the Unit 6 - PL/SQL in the subject of Basics of Data Base Management System:

**Indices**

- Indices are special data structures associated with tables/views which aid in fast retrieval of rows.
- They contain ordered lists of row pointers pointing to table rows, sorted based on the index column values.
- Query processing can navigate through the index to locate rows quickly instead of scanning the entire table, hence improving performance.
- Types:
  - Unique index: Ensures uniqueness of values in indexed columns. Only one row can have a given value in unique index column(s).
  - Non-unique index: Does not enforce uniqueness. Multiple rows can have the same value in indexed column(s).
  - B-tree index: Most common type. Maintained by database automatically. Balanced tree structure.
- Advantages:
  - Faster queries due to reduced I/O.
  - Enforces uniqueness for unique indices.
  - Useful for sorting data and implementing primary/foreign key constraints.
- Disadvantages:
  - Extra I/O required to update index when table data changes.
  - Extra storage space required to store index data.
- When to create:
  - On columns used frequently in WHERE clauses for faster lookups.
  - On columns having unique/primary key constraints.
  - Consider clustered indices on primary keys for maximum performance.
- Examples:

**Code:**
CREATE INDEX index_name
ON table_name (column_name)

**Markdown Table:**

Index Type | Ensures Uniqueness | Extra I/O for Updates | Useful For
