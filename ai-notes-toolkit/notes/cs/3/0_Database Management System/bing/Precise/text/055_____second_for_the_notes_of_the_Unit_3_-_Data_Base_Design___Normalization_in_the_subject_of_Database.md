### Unit 3 - Data Base Design & Normalization

1. Database design is the process of producing a detailed data model of a database. This data model contains all the needed logical and physical design choices and physical storage parameters needed to generate a design in a data definition language, which can then be used to create a database.

2. Normalization is the process of organizing a database in a way that reduces redundancy and dependency. It is a technique used to design a database so that it meets certain requirements, such as minimizing duplicate data and ensuring that data is stored in the most appropriate way.

3. Normalization involves dividing a database into two or more tables and defining relationships between the tables. The objective is to isolate data so that additions, deletions, and modifications of a field can be made in just one table and then propagated through the rest of the database via the defined relationships.

4. There are several levels of normalization, including first normal form (1NF), second normal form (2NF), third normal form (3NF), and so on. Each level has its own set of rules and requirements that must be met in order to achieve that level of normalization.

5. Normalization is an important part of database design because it helps to minimize data redundancy and improve data integrity. By organizing data in a normalized manner, it is easier to maintain and update the database, and it can also improve the performance of queries and other database operations.

6. However, normalization is not always the best approach for every situation. In some cases, denormalization, or the process of intentionally introducing redundancy into a database, can improve performance by reducing the number of joins required to retrieve data. It is important to carefully consider the trade-offs between normalization and denormalization when designing a database.