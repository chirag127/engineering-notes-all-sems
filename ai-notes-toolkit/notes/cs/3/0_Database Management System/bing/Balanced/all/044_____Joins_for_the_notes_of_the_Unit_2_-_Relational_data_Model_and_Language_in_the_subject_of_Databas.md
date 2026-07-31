# Joins

Joins are operations in relational data model that allow queries across multiple database tables. Joins merge data stored in different tables and output it in filtered form in a results table. The principle of SQL join is based on the relational algebra operation of the same name – a combination of Cartesian product and selection.

The prerequisite for joins is that the selected tables are linked to one another using foreign key relationships. The most important join types include the following:

- **Theta (θ) Join**: Theta join combines tuples from different relations provided they satisfy the theta condition. The join condition is denoted by the symbol θ. The theta condition can use any comparison operator, such as =, <, >, <=, >=, or <>.
- **Equijoin**: When theta join uses only equality comparison operator, it is said to be equijoin. Equijoin is a special case of theta join. Equijoin can also be called as inner join.
- **Natural Join ( ⋈)**: Natural join does not use any comparison operator. It combines tuples from different relations by comparing all their common attributes. Natural join eliminates duplicate columns from the result.
- **Outer Joins**: Outer joins are used to retrieve data from two or more tables even if there is no matching data. There are three types of outer joins: left outer join, right outer join, and full outer join.
- **Left Outer Join (R S)**: Left outer join returns all the tuples from the left relation R and only the matching tuples from the right relation S. If there is no match for a tuple in R, then the attributes of S are filled with null values.
- **Right Outer Join (R S)**: Right outer join returns all the tuples from the right relation S and only the matching tuples from the left relation R. If there is no match for a tuple in S, then the attributes of R are filled with null values.
- **Full Outer Join ( R S)**: Full outer join returns all the tuples from both the relations R and S. If there is no match for a tuple in either relation, then the attributes of the other relation are filled with null values.

Here is a diagram that illustrates the different types of joins:

![Joins diagram](https://www.essentialsql.com/wp-content/uploads/2016/04/SQL-Joins-1.png)