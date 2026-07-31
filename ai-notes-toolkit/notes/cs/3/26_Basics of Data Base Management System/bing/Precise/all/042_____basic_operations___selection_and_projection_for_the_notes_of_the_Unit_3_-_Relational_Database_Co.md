# Basic Operations – Selection and Projection

Selection and projection are two basic operations in the relational database model. These operations are used to manipulate and retrieve data from a database.

## Selection

Selection is the operation of choosing a subset of rows from a relation that satisfies a given condition. The condition is specified using a selection predicate, which is a Boolean expression that evaluates to true or false for each row in the relation.

The selection operation is denoted by the sigma (σ) symbol. The general form of the selection operation is:

σ<sub>selection predicate</sub>(R)

where R is the relation on which the selection operation is performed.

For example, consider a relation `Employee` with the following attributes: `EmpID`, `Name`, `Age`, `Salary`. To select all employees with a salary greater than 50000, the selection operation would be:

σ<sub>Salary > 50000</sub>(Employee)

## Projection

Projection is the operation of choosing a subset of columns from a relation. The projection operation is denoted by the pi (π) symbol. The general form of the projection operation is:

π<sub>attribute list</sub>(R)

where R is the relation on which the projection operation is performed and the attribute list is a comma-separated list of attributes to be included in the result.

For example, consider the `Employee` relation mentioned above. To project only the `Name` and `Age` attributes of the relation, the projection operation would be:

π<sub>Name, Age</sub>(Employee)

These two operations, selection and projection, can be combined to form more complex queries. For example, to select all employees with a salary greater than 50000 and project only their `Name` and `Age` attributes, the combined operation would be:

π<sub>Name, Age</sub>(σ<sub>Salary > 50000</sub>(Employee))

These are the basic concepts of selection and projection operations in the relational database model. They are essential for manipulating and retrieving data from a database.