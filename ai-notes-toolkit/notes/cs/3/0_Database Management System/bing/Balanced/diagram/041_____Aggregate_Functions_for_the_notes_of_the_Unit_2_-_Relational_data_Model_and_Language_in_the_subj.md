### Aggregate Functions for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Aggregate functions are functions that take a collection of values as input and return a single value as output.
- Aggregate functions are used to perform calculations or selections on a set of values, such as finding the average, minimum, maximum, sum, or count of values.
- Aggregate functions can be applied to a relation or a subset of a relation defined by a condition or a grouping attribute.
- Aggregate functions can provide useful summary statistics or insights from data analysis that can inform future decision-making.
- Some examples of aggregate functions are:

  - `avg`: returns the average value of a numeric column or expression.
  - `min`: returns the minimum value of a column or expression.
  - `max`: returns the maximum value of a column or expression.
  - `sum`: returns the sum of values of a numeric column or expression.
  - `count`: returns the number of values or rows in a column or relation.

- Aggregate functions can be used in conjunction with other relational algebra operations, such as selection, projection, join, union, intersection, difference, and division.
- Aggregate functions can also be used in conjunction with the `group by` and `having` clauses to perform aggregation on subsets of data based on some criteria.
- The syntax for using aggregate functions in relational algebra is:

  - `F(R)`: applies the aggregate function `F` to the relation `R` and returns a single value.
  - `F(R, A)`: applies the aggregate function `F` to the attribute `A` of the relation `R` and returns a single value.
  - `F(R, A, B)`: applies the aggregate function `F` to the attribute `A` of the relation `R` and groups the results by the attribute `B`, returning a relation with two attributes: `B` and `F(A)`.
  - `F(R, A, B, C)`: applies the aggregate function `F` to the attribute `A` of the relation `R` and groups the results by the attribute `B`, then selects only the groups that satisfy the condition `C`, returning a relation with two attributes: `B` and `F(A)`.

- Some examples of using aggregate functions in relational algebra are:

  - `avg(Student, GPA)`: returns the average GPA of all students.
  - `max(Student, GPA, Department)`: returns the maximum GPA of each department.
  - `count(Enroll, StudentID, CourseID, Grade > 90)`: returns the number of students who got more than 90 in each course.
  - `sum(Project, Budget, Manager, Budget > 100000)`: returns the total budget of the projects managed by each manager with a budget greater than 100000.