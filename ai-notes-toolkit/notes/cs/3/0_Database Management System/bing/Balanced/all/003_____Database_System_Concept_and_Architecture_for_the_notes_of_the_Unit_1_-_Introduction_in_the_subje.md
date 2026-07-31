# Database System Concept and Architecture

- A database system is a software package that manages data stored in a database and provides various operations to access and manipulate the data.
- A database system consists of several components, such as the database, the database management system (DBMS), the database applications, and the users.
- A database is a collection of related data that represents some aspects of the real world. A database can be organized in different ways, such as tables, graphs, documents, etc.
- A DBMS is a software system that provides the functionality to create, maintain, and manipulate databases. A DBMS typically supports a specific data model, such as relational, object-oriented, or XML.
- A database application is a software program that interacts with the DBMS to perform specific tasks, such as querying, updating, or analyzing the data. A database application can be written in various languages, such as SQL, Java, Python, etc.
- A user is a person or a program that uses the database system to access or modify the data. A user can be classified into different types, such as end users, application programmers, database administrators, etc.

- The architecture of a database system defines the logical and physical structure of the system components and their interactions. The architecture can vary depending on the design goals, the data model, the system environment, and the user requirements.
- The architecture of a database system can be classified into three levels: external, conceptual, and internal.
- The external level defines the view of the data that is seen by a specific user or a group of users. An external view can be customized to suit the needs and preferences of the user. An external view can also hide some details of the data that are irrelevant or sensitive to the user.
- The conceptual level defines the logical structure of the data that is stored in the database. The conceptual level describes the data entities, their attributes, and their relationships. The conceptual level is independent of the physical implementation of the data and the user views of the data.
- The internal level defines the physical organization and storage of the data on the disk. The internal level describes the data structures, such as files, records, indexes, etc., that are used to store and access the data. The internal level is dependent on the hardware and software characteristics of the system.

- The architecture of a database system can also be classified into two types: centralized and distributed.
- A centralized database system is a system where the database and the DBMS are located on a single computer or a server. A centralized database system can be accessed by multiple users or applications through a network. A centralized database system has the advantages of simplicity, efficiency, and security, but also has the disadvantages of scalability, reliability, and availability.
- A distributed database system is a system where the database and the DBMS are distributed across multiple computers or servers that are connected by a network. A distributed database system can be accessed by multiple users or applications through the network. A distributed database system has the advantages of scalability, reliability, and availability, but also has the disadvantages of complexity, overhead, and consistency.