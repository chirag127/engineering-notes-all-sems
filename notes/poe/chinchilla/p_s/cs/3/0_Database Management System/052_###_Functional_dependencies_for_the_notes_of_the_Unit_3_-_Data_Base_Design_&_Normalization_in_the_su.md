### Functional dependencies for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System

Functional dependencies are a critical aspect of database design and normalization. They play a significant role in ensuring that the data is organized and stored efficiently in a database. Here are some important points to understand about functional dependencies:

- A functional dependency is a relationship between two attributes in a table, where one attribute's value determines the value of another attribute.
- In other words, if we know the value of one attribute, we can determine the value of another attribute with 100% accuracy.
- For example, if we have a table of employees with attributes such as employee id, name, and department, the department attribute is functionally dependent on the employee id attribute. Knowing the employee id, we can determine the department of the employee.
- Functional dependencies are denoted by an arrow symbol (→), where the left-hand side represents the determining attribute, and the right-hand side represents the determined attribute.
- Functional dependencies can be either trivial or non-trivial. A non-trivial functional dependency is one where the determined attribute is not already a part of the determining attribute. Trivial functional dependencies are those where the determined attribute is already a part of the determining attribute.

Advantages of functional dependencies:

- They help in identifying redundancy in the data and eliminate it through normalization.
- They ensure data integrity by preventing inconsistencies and errors in the data.
- They improve the performance of the database by reducing the size of the database and making it easier to retrieve data.

Disadvantages of functional dependencies:

- Over-normalization can lead to performance issues as well as increased complexity in querying the data.
- It can be challenging to identify and manage functional dependencies in larger databases with multiple tables.

Examples of functional dependencies:

- In a table of students with attributes such as student id, name, and course id, the course id is functionally dependent on the student id.
- In a table of orders with attributes such as order id, product id, and customer id, the customer id is functionally dependent on the order id.

Applications of functional dependencies:

- Functional dependencies are used extensively in database normalization, which is essential for efficient and effective database design.
- They are also used in query optimization to improve the performance of database queries.

In conclusion, understanding functional dependencies is crucial for effective database design and normalization. It helps in organizing data efficiently, improving data integrity, and enhancing database performance.