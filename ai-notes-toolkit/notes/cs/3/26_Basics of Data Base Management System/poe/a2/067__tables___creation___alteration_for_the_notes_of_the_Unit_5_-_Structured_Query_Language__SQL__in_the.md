 Here is the formal content in Markdown format without any emojis or external links for the topic `tables – creation & alteration` for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System:

### Tables – Creation & Alteration

#### Table Creation

- CREATE TABLE statement is used to create a new table in a database.
- Specify the table name and column names along with their data types and sizes.
- Columns can have constraints like NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY, etc.
- Table can have constraints like PRIMARY KEY, FOREIGN KEY, etc.

```sql
CREATE TABLE table_name (
    column1 datatype constraints,
    column2 datatype constraints,
    ...
);
```

#### Table Alteration

- ALTER TABLE statement is used to modify an existing table.
- Can be used to add, delete or modify columns or constraints in a table.
- Adding new columns or constraints will not change the existing data, it will only apply to new data.
- Some common alterations:

- Add a new column: `ALTER TABLE table_name ADD column_name datatype;`
- Drop a column: `ALTER TABLE table_name DROP column_name;`
- Add a constraint: `ALTER TABLE table_name ADD CONSTRAINT constraint_name constraint_type;`
- Drop a constraint: `ALTER TABLE table_name DROP CONSTRAINT constraint_name;`

The content is written in a formal tone with points and without any emojis or external links as instructed. Let me know if you would like me to modify or expand the answer.