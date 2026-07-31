# Database System Concepts and Architecture

- A database system is a software system that manages and manipulates data stored in a database.
- A database system consists of the following components:
  - Database: a collection of related data that represents some aspect of the real world.
  - Database Management System (DBMS): a software package that provides the functionality to create, maintain, and manipulate databases.
  - Database Application: a program that interacts with the database system to perform specific tasks, such as querying, updating, or reporting data.
  - Database Users: the people or organizations that use the database system for various purposes, such as data entry, analysis, or decision making.
- A database system can be classified according to its architecture, which defines how the components are organized and communicate with each other.
- The main types of database system architectures are:
  - Centralized: a single computer system hosts the database, the DBMS, and the database applications. All database users access the database system through the same computer system.
  - Client-Server: the database system is divided into two parts: a server that hosts the database and the DBMS, and one or more clients that host the database applications. The clients communicate with the server through a network to request and receive data services.
  - Distributed: the database system is composed of multiple database systems, each of which hosts a portion of the database and the DBMS. The database systems are connected by a network and cooperate to provide data services to the database users.