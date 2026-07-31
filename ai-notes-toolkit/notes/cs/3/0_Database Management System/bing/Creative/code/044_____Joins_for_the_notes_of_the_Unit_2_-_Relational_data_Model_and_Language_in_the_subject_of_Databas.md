### Joins for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- A join is an operation in relational databases that allows queries across multiple database tables.
- Joins merge data stored in different tables and output it in filtered form in a results table.
- The principle of SQL join is based on the relational algebra operation of the same name – a combination of Cartesian product and selection.
- The prerequisite for a join is that the selected tables are linked to one another using foreign key relationships.
- The most important join types include the following  :
  - Theta (θ) join: Theta join combines tuples from different relations provided they satisfy the theta condition. The join condition is denoted by the symbol θ. The theta condition can use any comparison operator, such as =, <, >, <=, >=, or <>.
  - Equijoin: When theta join uses only equality comparison operator, it is said to be equijoin. Equijoin matches rows from different tables based on the equality of a common column. Equijoin can also be called inner join or simple join.
  - Natural join: Natural join does not use any comparison operator. Natural join joins two or more tables based on the same attribute name and data type in the tables. Natural join eliminates duplicate columns from the result table.
  - Outer join: Outer join returns all rows that satisfy the join condition and also returns some or all of those rows from one table for which no rows from the other satisfy the join condition. Outer join can be left, right, or full.
    - Left outer join: Left outer join returns all rows from the left table, even if there are no matches in the right table. Left outer join is denoted by the symbol R S.
    - Right outer join: Right outer join returns all rows from the right table, even if there are no matches in the left table. Right outer join is denoted by the symbol R S.
    - Full outer join: Full outer join returns all rows from both tables, regardless of whether there is a match or not. Full outer join is denoted by the symbol R S.
- Relationships exist within a data model—one that you explicitly create, or one that Excel automatically creates on your behalf when you simultaneously import multiple tables. You can also use the Power Pivot add-in to create or manage the model.
- Relationships are used to stitch the database back together to make it easy to read and use. They match rows between tables. In most cases we’re matching a column value from one table with another.