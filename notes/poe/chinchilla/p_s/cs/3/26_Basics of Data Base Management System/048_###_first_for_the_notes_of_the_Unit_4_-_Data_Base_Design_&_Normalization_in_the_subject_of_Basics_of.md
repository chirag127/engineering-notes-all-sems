### Unit 4 - Data Base Design & Normalization

Database design is the process of creating a detailed data model of a database. Normalization is a technique to eliminate data redundancy and minimize data dependencies. In this unit, we will learn about database design and normalization in detail.

#### Database Design

The following are some key points to keep in mind while designing a database:

- Identify the entities and their attributes: Entities are the objects that we want to store in our database. Attributes define the characteristics of an entity.
- Define relationships between entities: Relationships define how entities are related to each other. There are three types of relationships: one-to-one, one-to-many, and many-to-many.
- Normalize the database: Normalization is the process of organizing data in a database to reduce redundancy and dependency.

#### Normalization

Normalization is a technique to minimize data redundancy and dependency. There are several levels of normalization, each with its own set of rules. The following are the different levels of normalization:

- First Normal Form (1NF): A table is in 1NF if it has no repeating groups or multivalued attributes.
- Second Normal Form (2NF): A table is in 2NF if it is in 1NF and all non-key attributes are dependent on the primary key.
- Third Normal Form (3NF): A table is in 3NF if it is in 2NF and all non-key attributes are independent of each other.

Advantages of normalization:

- Eliminates data redundancy
- Reduces data dependency
- Ensures data consistency

Disadvantages of normalization:

- Increases the number of tables in the database
- May require more complex queries to retrieve data

Normalization Example:

Consider a table that stores information about students and their courses. The table has the following columns: Student ID, Student Name, Course 1, Course 2, Course 3.

This table is not in 1NF because it has repeating groups (Course 1, Course 2, Course 3). To normalize the table, we can create two tables: one for students and one for courses. The student table would have the columns Student ID and Student Name, while the course table would have the columns Course ID and Course Name. We can then create a third table to store the relationship between students and courses, with columns for Student ID and Course ID.

Applications of normalization:

Normalization is used in various applications, including:

- Relational databases
- Data warehouses
- Online transaction processing (OLTP) systems

In conclusion, database design and normalization are crucial for creating an efficient and effective database. By following the rules of normalization, we can minimize data redundancy and dependency, ensuring data consistency and making it easier to retrieve and manipulate data.