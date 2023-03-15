# Domain Constraints for the Notes of the Unit 3 - Relational Database Concepts in the Subject of Basics of Data Base Management System

- Domain constraints are a type of user-defined column that helps us to arrange the data we have entered according to the datatype.
- A domain integrity constraint is a set of rules that restricts the kind of attributes or values a column or relation can hold in the database table.
- The domain means a range of values. In mathematics, the concept of Domain means the allowed values for a function. Similarly, in DBMS, the Domain Constraint specifies the domain or set of values.
- There are two types of constraints that come under domain constraint and they are:
  - Domain Constraints – Not Null: Null values are the values that are unassigned or we can also say that which are unknown. The not null constraint is used to specify that the column must not accept null values.
  - Domain Constraints – Check: It defines a condition that each row must satisfy which means it checks the validity of the data entered into the column.
- Domain constraints can be defined using the CREATE TABLE or ALTER TABLE statements in SQL. For example:
```sql
CREATE TABLE Student
(
  Roll_no int NOT NULL,
  Name varchar(50) NOT NULL,
  Age int CHECK (Age>=18),
  Gender char(1) CHECK (Gender IN ('M','F')),
  PRIMARY KEY (Roll_no)
);
```
- Domain constraints can also be defined using rules in SQL Server. A rule is a named object that contains a condition for the data in a column. For example:
```sql
CREATE RULE AgeRule
AS
@Age >= 18
GO
CREATE TABLE Student
(
  Roll_no int NOT NULL,
  Name varchar(50) NOT NULL,
  Age int,
  Gender char(1) CHECK (Gender IN ('M','F')),
  PRIMARY KEY (Roll_no)
);
GO
EXEC sp_bindrule 'AgeRule', 'Student.Age'
GO
```
- Domain constraints are important to ensure the data quality and integrity in the database. They prevent the insertion of invalid or inconsistent data that may cause errors or anomalies in the database operations.