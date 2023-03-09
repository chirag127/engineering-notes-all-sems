### Functional Dependencies for the Notes of Unit 4 - Database Design & Normalization in the subject of Basics of Database Management System

Functional dependencies are the foundation of database normalization. A functional dependency is a constraint between two sets of attributes in a relation from a database. It is an important concept in database design that ensures the integrity and consistency of the data.

Here are some of the key points to remember about functional dependencies:

1. Definition - A functional dependency is a relationship between two or more attributes in a relation such that one attribute determines the value of another attribute.

2. Notation - Functional dependencies are denoted by an arrow (→) between two sets of attributes. The left-hand side (LHS) of the arrow represents the determining attributes, while the right-hand side (RHS) represents the determined attributes.

3. Example - Consider a relation called "Employees" with attributes such as EmployeeID, FirstName, LastName, Department, and Salary. The functional dependency between EmployeeID and FirstName can be denoted as EmployeeID → FirstName. This means that the value of the FirstName attribute is determined by the value of the EmployeeID attribute.

4. Keys - A key is a set of attributes that uniquely identifies each tuple in a relation. A superkey is a set of attributes that includes a key and other attributes. In a relation, a functional dependency is said to be a trivial dependency if the RHS is a subset of the LHS. Non-trivial dependencies are those where the RHS is not a subset of the LHS.

5. Normal Forms - Functional dependencies play a crucial role in the normalization process of a database. Normalization aims to reduce data redundancy and improve data integrity by organizing data into tables with specific rules. There are various normal forms, including first normal form (1NF), second normal form (2NF), and third normal form (3NF).

6. Advantages - Functional dependencies help to ensure data consistency, reduce data redundancy, and improve database performance. They also provide a framework for the normalization process, which helps to ensure that the database is well-organized and efficient.

7. Disadvantages - The main disadvantage of functional dependencies is that they can be complex and difficult to manage. Additionally, they rely on the accuracy of the data, which can be impacted by human error or other external factors.

In conclusion, functional dependencies are an essential concept in database design and normalization. Understanding the concept of functional dependencies is crucial for creating an efficient and well-organized database.