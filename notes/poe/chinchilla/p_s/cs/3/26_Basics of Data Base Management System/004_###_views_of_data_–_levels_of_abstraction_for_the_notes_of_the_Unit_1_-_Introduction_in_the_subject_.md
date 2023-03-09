### Views of Data – Levels of Abstraction

A database management system (DBMS) is designed to manage data in a systematic way. It provides a mechanism to store, retrieve and modify data in an efficient and secure manner. The DBMS provides different views of the data, depending on the level of abstraction. 

Here are the different levels of abstraction for views of data:

1. Physical view - This is the lowest level of abstraction, which deals with how data is stored on the physical storage media, such as hard disk or flash memory. The physical view describes the data storage and access methods used by the DBMS. It involves the organization of data into files, pages, and blocks.

2. Logical view - This level of abstraction deals with how data is organized and presented to the user. It describes the relationship between different data elements and how they are related to each other. The logical view consists of the schema, which represents the structure of the database.

3. External view - This is the highest level of abstraction, which deals with how data is presented to the end-users. It describes the portion of the database that is relevant to a particular user or group of users. The external view is created by defining a view of the database that includes only the required data elements.

Advantages of using views of data:

1. Security - Views can be used to provide different levels of access to different users. This ensures that sensitive data is not accessed by unauthorized users.

2. Simplification - Views can be used to simplify complex data structures by presenting only the required data elements to the user.

3. Data independence - Views provide a layer of abstraction that separates the physical storage of data from the logical and external views. This means that changes to the physical storage of data do not affect the logical and external views.

Disadvantages of using views of data:

1. Performance - Creating views can have an impact on database performance, as it involves additional processing overhead.

2. Maintenance - Maintaining views can be a complex task, especially if there are multiple views that need to be updated when changes are made to the database schema.

Examples of using views of data:

1. A bank may use views to provide different levels of access to customer data, based on the role of the user (e.g. teller, manager, etc.).

2. A university may use views to provide students with access to their own records, while restricting access to sensitive data such as grades and disciplinary records.

Applications of using views of data:

1. Security - Views can be used to provide secure access to data, by limiting the amount of data that each user can access.

2. Simplification - Views can be used to simplify complex data structures, by presenting only the required data elements to the user.

In conclusion, views of data help in providing different levels of abstraction that are useful for securing data, simplifying complex data structures, and providing different levels of access to users. It is important to carefully design views to ensure that they are efficient and maintainable.