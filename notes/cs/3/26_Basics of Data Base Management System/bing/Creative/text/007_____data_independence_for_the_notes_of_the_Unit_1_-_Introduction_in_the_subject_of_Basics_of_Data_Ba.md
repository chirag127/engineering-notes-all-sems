### Data Independence for the Notes of the Unit 1 - Introduction in the Subject of Basics of Data Base Management System

- Data independence is the property of a database system that allows the schema of the database to be changed without affecting the applications that use the database.
- Schema is the structure or design of the database that defines the tables, fields, relationships, constraints, etc.
- There are three levels of schema in a database system: external, conceptual, and physical .
- External schema is the view of the database that is seen by the users or applications. It defines what data and operations are available to them.
- Conceptual schema is the logical representation of the database that is independent of the physical implementation. It defines what data and relationships exist in the database.
- Physical schema is the actual storage and organization of the data on the disk. It defines how the data is stored, indexed, compressed, encrypted, etc.
- Data independence is of two types: logical and physical  .
- Logical data independence is the ability to change the conceptual schema without affecting the external schema. It allows the database administrator to modify the logical structure of the database, such as adding, deleting, or renaming tables, columns, or relationships, without requiring the users or applications to change their queries or programs.
- Physical data independence is the ability to change the physical schema without affecting the conceptual schema. It allows the database administrator to modify the physical storage and organization of the data, such as changing the file format, location, size, compression, encryption, etc., without requiring the users or applications to change their queries or programs.
- Data independence is important for the following reasons:
  - It enhances the flexibility and adaptability of the database system to changing requirements and technologies.
  - It reduces the maintenance and development costs of the database system by minimizing the impact of schema changes on the users and applications.
  - It improves the performance and efficiency of the database system by allowing the database administrator to optimize the physical storage and organization of the data according to the workload and usage patterns.
  - It increases the security and integrity of the database system by allowing the database administrator to control the access and manipulation of the data at different levels of abstraction.