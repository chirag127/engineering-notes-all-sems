# Data Independence and Database Language and Interfaces

- Data independence is a property of DBMS that allows the database schema to be changed without affecting the applications that use the data.
- Database schema is the structure and organization of the data in the database, which can be divided into three levels: external, conceptual, and internal.
- External schema is the view of the data that is seen by the end-users or applications. It can be different for different users or applications, depending on their needs and preferences.
- Conceptual schema is the logical view of the data that is shared by all the users or applications. It describes the entities, attributes, relationships, and constraints of the data, without specifying the physical details of storage or implementation.
- Internal schema is the physical view of the data that is seen by the DBMS. It describes how the data is stored, organized, indexed, and accessed by the DBMS.
- Data independence can be classified into two types: logical data independence and physical data independence.
- Logical data independence is the ability to change the conceptual schema without affecting the external schema or the applications. It allows the DBMS to adapt to the changing requirements of the data, such as adding, deleting, or modifying entities, attributes, or relationships.
- Physical data independence is the ability to change the internal schema without affecting the conceptual schema or the applications. It allows the DBMS to optimize the performance, efficiency, and security of the data, such as changing the storage structure, access method, or indexing strategy.
- Data independence is achieved by using a three-schema architecture and a data definition language (DDL) and a data manipulation language (DML) to separate the data from the applications .
- A DDL is a language that is used to define the database schema at each level. It allows the DBMS to create, modify, or delete the schema objects, such as tables, views, indexes, or constraints.
- A DML is a language that is used to manipulate the data in the database. It allows the applications to insert, update, delete, or query the data, without knowing the details of the schema or the storage.
- A database language is a combination of a DDL and a DML, which can be either procedural or non-procedural.
- A procedural database language requires the applications to specify both what data to access and how to access it. It gives more control and flexibility to the applications, but also more complexity and responsibility.
- A non-procedural database language requires the applications to specify only what data to access, and leaves the how to the DBMS. It gives more simplicity and abstraction to the applications, but also less control and efficiency.
- A database interface is a software component that allows the applications to communicate with the DBMS using a database language. It can be either embedded or interactive.
- An embedded database interface integrates the database language with a host programming language, such as C, Java, or Python. It allows the applications to use the features and functions of both languages, but also requires more coding and compilation.
- An interactive database interface provides a separate environment for the database language, such as SQL*Plus, MySQL, or MongoDB. It allows the applications to use the database language directly, but also requires more switching and typing.