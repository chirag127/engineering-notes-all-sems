### Joins

- A join is a way of combining data from two or more tables based on a common column or condition.
- A join condition specifies how the tables are related, usually by matching values in one or more columns.
- A join can be either an inner join or an outer join, depending on whether it returns only matching rows or also includes non-matching rows.
- An inner join returns only the rows that have matching values in both tables.
- An outer join returns all the rows from one table, and the matching rows from the other table. If there is no match, the missing values are filled with NULL.
- There are three types of outer joins: left outer join, right outer join, and full outer join.
- A left outer join returns all the rows from the left table, and the matching rows from the right table. If there is no match, the right side is filled with NULL.
- A right outer join returns all the rows from the right table, and the matching rows from the left table. If there is no match, the left side is filled with NULL.
- A full outer join returns all the rows from both tables, and fills the missing values with NULL if there is no match.
- A join can also be a cross join, which returns the Cartesian product of the two tables, meaning every possible combination of rows from both tables.
- A join can also be a self join, which is a join of a table with itself, using different aliases to distinguish the two instances of the table.
- A join can also be a natural join, which is a join based on all the columns that have the same name and data type in both tables.
- A join can also be an equi join, which is a join that uses only the equality operator (=) in the join condition.
- A join can also be a non-equi join, which is a join that uses other operators (such as <, >, !=, etc.) in the join condition.
- A join can also be a theta join, which is a join that uses any condition in the join condition.
- A join can also be an anti join, which is a join that returns the rows from one table that do not have a match in the other table.