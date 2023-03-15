### Basic Operations – Selection and Projection

Selection and projection are two basic operations in the relational database model. These operations are used to manipulate the data stored in the database.

#### Selection

Selection is the operation of choosing a subset of rows from a relation that satisfies a given condition. The condition is specified using a selection predicate, which is a boolean expression that evaluates to true or false for each row in the relation. The result of the selection operation is a new relation that contains only the rows for which the selection predicate is true.

The selection operation is denoted by the sigma (σ) symbol. The selection predicate is written as a subscript to the sigma symbol. For example, the expression σ<sub>age > 30</sub>(Employee) represents the selection of all rows from the Employee relation where the value of the age attribute is greater than 30.

#### Projection

Projection is the operation of choosing a subset of columns from a relation. The result of the projection operation is a new relation that contains only the specified columns.

The projection operation is denoted by the pi (π) symbol. The list of columns to be included in the result is written as a subscript to the pi symbol. For example, the expression π<sub>name, salary</sub>(Employee) represents the projection of the name and salary columns from the Employee relation.

These two operations, selection and projection, are fundamental to the manipulation of data in a relational database. They are used to extract and present data in a way that is meaningful to the user.