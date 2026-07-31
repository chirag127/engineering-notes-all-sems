# Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

## Introduction

- Server-side applications are programs that run on a web server and interact with clients through web browsers or other web protocols.
- Server-side applications can perform various tasks, such as processing user input, accessing databases, generating dynamic web pages, sending emails, etc.
- Server-side applications can be written in different programming languages, such as Java, PHP, Python, etc.
- Server-side applications can use various technologies and frameworks to simplify and enhance their development, such as JDDC, ODBC, and session tracking API.

## JDDC

- JDDC stands for Java Database Driver Connectivity, which is a technology that allows Java applications to connect to various types of databases using a standard interface.
- JDDC consists of four components: drivers, driver manager, connection, and statement.
- Drivers are software modules that implement the JDDC interface for a specific database. For example, there are drivers for MySQL, Oracle, PostgreSQL, etc.
- Driver manager is a class that manages the loading and registration of drivers. It also provides methods to obtain a connection to a database using a driver.
- Connection is an interface that represents a session with a database. It provides methods to create and execute statements, manage transactions, etc.
- Statement is an interface that represents a SQL command to be executed on a database. It provides methods to execute queries, update data, retrieve results, etc.

## ODBC

- ODBC stands for Open Database Connectivity, which is a standard that allows applications to access data from various types of databases using a common interface.
- ODBC consists of three components: drivers, driver manager, and data source.
- Drivers are software modules that implement the ODBC interface for a specific database. For example, there are drivers for MySQL, Oracle, PostgreSQL, etc.
- Driver manager is a software component that manages the loading and registration of drivers. It also provides functions to obtain a connection to a database using a driver.
- Data source is a logical name that identifies a database and its connection parameters. It can be defined in a configuration file or in the system registry.

## Session tracking API

- Session tracking API is a technology that allows server-side applications to maintain state information across multiple requests from the same client.
- Session tracking API consists of two components: session and session context.
- Session is an interface that represents a unique identifier and a collection of attributes associated with a client. It provides methods to get and set attributes, invalidate the session, etc.
- Session context is an interface that manages the creation and retrieval of sessions. It provides methods to get a session by its identifier, create a new session, etc.

## Notes for users

- The notes for this unit are password-protected and can be accessed by the following users and passwords:

| User | Password |
|------|----------|
| user1 | pwd1 |
| user2 | pwd2 |
| user3 | pwd3 |
| user4 | pwd4 |

- To access the notes, the users need to enter their username and password in a web form and submit it to a server-side application that validates their credentials and displays the notes if they are correct.
- The server-side application can use JDDC or ODBC to connect to a database that stores the user information and the notes.
- The server-side application can also use session tracking API to remember the user's login status and prevent unauthorized access to the notes.