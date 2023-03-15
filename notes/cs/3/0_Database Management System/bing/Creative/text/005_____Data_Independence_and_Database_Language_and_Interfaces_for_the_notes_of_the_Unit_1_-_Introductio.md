### Data Independence and Database Language and Interfaces

- Data independence is the property of a database system that allows the data and the applications to be changed independently of each other.
- Data independence can be classified into two types: logical data independence and physical data independence.
- Logical data independence is the ability to change the logical structure of the database (such as the schema, tables, views, etc.) without affecting the existing applications that access the data.
- Physical data independence is the ability to change the physical structure of the database (such as the storage devices, file organization, indexes, etc.) without affecting the logical structure or the applications that access the data.
- Data independence is achieved by using a three-level architecture for the database system, which consists of the external level, the conceptual level, and the internal level.
- The external level defines the views of the data for different users or applications, which are tailored to their specific needs and requirements.
- The conceptual level defines the logical structure of the data for the entire database, which is independent of the physical implementation or the user views.
- The internal level defines the physical structure of the data, which is how the data is stored and organized on the storage devices.
- The three levels are connected by two mappings: the external-conceptual mapping and the conceptual-internal mapping, which define how the data is transformed from one level to another.
- The database language and interfaces are the means of communication between the users or applications and the database system.
- The database language and interfaces can be classified into two types: data definition language (DDL) and data manipulation language (DML).
- Data definition language (DDL) is the language that is used to define the structure of the data at the different levels of the database system, such as the schema, tables, views, constraints, etc.
- Data manipulation language (DML) is the language that is used to manipulate the data in the database, such as inserting, updating, deleting, querying, etc.
- The database language and interfaces can also be classified into two types: procedural and non-procedural.
- Procedural language and interface require the user or application to specify both what data is needed and how to retrieve or manipulate it, such as SQL or QBE.
- Non-procedural language and interface require the user or application to specify only what data is needed, and the database system determines how to retrieve or manipulate it, such as natural language or graphical user interface.