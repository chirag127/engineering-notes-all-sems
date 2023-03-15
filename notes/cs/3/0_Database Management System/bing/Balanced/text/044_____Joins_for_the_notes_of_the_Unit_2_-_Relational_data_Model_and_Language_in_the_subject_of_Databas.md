### Joins for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Joins are operations in relational databases that allow queries across multiple database tables.
- Joins merge data stored in different tables and output it in filtered form in a results table.
- Joins are based on the relational algebra operation of the same name – a combination of Cartesian product and selection.
- The prerequisite for joins is that the selected tables are linked to one another using foreign key relationships.
- The most important join types include the following:
  - Theta (θ) join: Theta join combines tuples from different relations provided they satisfy the theta condition. The join condition is denoted by the symbol θ.
  - Equijoin: When theta join uses only equality comparison operator, it is said to be equijoin.
  - Natural join (⋈): Natural join does not use any comparison operator. It automatically matches the columns with the same name and data type from both the tables.
  - Outer join: Outer join returns all the tuples from one relation and only the matching tuples from the other relation.
  - Left outer join (R S): Left outer join returns all the tuples from the left relation R and only the matching tuples from the right relation S.
  - Right outer join (R S): Right outer join returns all the tuples from the right relation S and only the matching tuples from the left relation R.
  - Full outer join (R S): Full outer join returns all the tuples from both the relations R and S, regardless of whether they match or not.
- Joins are used to stitch the database back together to make it easy to read and use. They match rows between tables. In most cases, we’re matching a column value from one table with another.
- Joins can be expressed using SQL syntax, such as SELECT, FROM, WHERE, ON, USING, etc .
- Joins can also be represented using Venn diagrams or relational diagrams to visualize the relationships between tables.
- Joins are essential for data modeling, which is the process of identifying entities and their relationships.
- Joins can improve the performance, flexibility, and scalability of the database system.