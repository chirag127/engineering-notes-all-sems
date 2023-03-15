### Joins for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- A join is an operation in relational databases that allows queries across multiple database tables.
- Joins merge data stored in different tables and output it in filtered form in a results table.
- The principle of SQL join is based on the relational algebra operation of the same name – a combination of Cartesian product and selection.
- The prerequisite for a join is that the selected tables are linked to one another using foreign key relationships.
- The most important join types include the following  :
  - Theta (θ) join: Theta join combines tuples from different relations provided they satisfy the theta condition. The join condition is denoted by the symbol θ. The theta condition can use any comparison operator, such as =, <, >, <=, >=, or <>.
  - Equijoin: When theta join uses only equality comparison operator, it is said to be equijoin. Equijoin matches rows from different tables based on the equality of a common column. Equijoin can also be called inner join or simple join.
  - Natural join: Natural join does not use any comparison operator. Natural join matches rows from different tables based on the equality of all common columns. Natural join eliminates duplicate columns from the result table.
  - Outer join: Outer join retains the unmatched rows from one or both tables. Outer join can be left, right, or full, depending on which table's rows are preserved.
    - Left outer join: Left outer join preserves the unmatched rows from the left table, filling in NULL values for the right table columns.
    - Right outer join: Right outer join preserves the unmatched rows from the right table, filling in NULL values for the left table columns.
    - Full outer join: Full outer join preserves the unmatched rows from both tables, filling in NULL values for the missing columns.
  - Cross join: Cross join produces the Cartesian product of the two tables, meaning that every row of the first table is paired with every row of the second table. Cross join does not have any join condition.
  - Self join: Self join is a special case of join where a table is joined to itself, meaning that each row of the table is combined with itself and every other row of the table. Self join is useful for comparing values within a table.