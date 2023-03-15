# Data Independence

Data independence is the property of a database management system (DBMS) that allows the database schema to be changed without affecting the user applications that access the data. Data independence is important for maintaining data consistency, security, and integrity, as well as for facilitating data abstraction and modularity.

Data independence is of two types:

- **Physical data independence**: This is the ability to modify the physical schema of the database without affecting the logical schema or the external schema. The physical schema defines how the data is stored, organized, and accessed at the lowest level of abstraction. For example, changing the file structure, indexing method, or storage device of the data does not affect the user queries or programs that use the data.

- **Logical data independence**: This is the ability to modify the logical schema of the database without affecting the external schema or the user views. The logical schema defines the structure and relationships of the data at the conceptual level of abstraction. For example, adding, deleting, or modifying a table, attribute, or relationship does not affect the user queries or programs that use the data, as long as the external schema remains unchanged.

Some examples of data independence are:

- If the DBMS supports physical data independence, then the database administrator can change the storage structure or access method of the data without affecting the user applications. For instance, the DBA can compress the data, partition the data, or use a different hashing function to improve the performance or storage efficiency of the database.

- If the DBMS supports logical data independence, then the database designer can change the logical schema of the data without affecting the user applications. For instance, the designer can add a new attribute to a table, merge two tables into one, or split a table into two, to improve the data quality or functionality of the database.