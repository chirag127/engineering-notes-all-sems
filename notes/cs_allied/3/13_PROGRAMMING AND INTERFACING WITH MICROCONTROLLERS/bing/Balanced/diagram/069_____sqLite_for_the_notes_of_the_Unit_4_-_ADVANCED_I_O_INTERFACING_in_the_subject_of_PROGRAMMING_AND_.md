# SQLite

SQLite is a database engine written in the C programming language. It is not a standalone app; rather, it is a library that software developers embed in their apps. As such, it belongs to the family of embedded databases.

SQLite was designed to allow the program to be operated without installing a database management system or requiring a database administrator. Unlike client–server database management systems, the SQLite engine has no standalone processes with which the application program communicates.

SQLite is an in-process library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine. It is a popular choice as an embedded database for local/client storage in application software such as web browsers. It is also used in many other applications that need a lightweight, embedded database.

SQLite is the most used database engine in the world. SQLite is built into all mobile phones and most computers and comes bundled inside countless other applications that people use every day.

SQLite reads and writes directly to ordinary disk files. A complete SQL database with multiple tables, indices, triggers, and views, is contained in a single disk file.

Some of the features of SQLite are:

- It supports most of the SQL standard, including transactions, views, subqueries, triggers, and foreign keys.
- It is cross-platform and can run on various operating systems, such as Windows, Linux, macOS, Android, iOS, etc.
- It is self-contained and does not require any external dependencies or configuration files.
- It is small and fast, with a low memory footprint and high performance.
- It is reliable and resilient, with built-in mechanisms for data integrity and error detection.
- It is extensible and customizable, with various options and interfaces for different languages and applications.

Some of the limitations of SQLite are:

- It does not support some advanced SQL features, such as stored procedures, user-defined functions, or full-text search.
- It does not support concurrent write operations, meaning that only one process can modify the database at a time.
- It does not scale well for large or complex databases, or for high concurrency or network access.
- It does not provide any security or encryption features, meaning that the database file can be read or modified by anyone who has access to it.

SQLite can be used for various purposes, such as:

- Prototyping and testing of applications that use SQL databases.
- Developing and deploying small to medium-sized applications that do not require high scalability or concurrency.
- Storing and querying local or offline data that does not need to be synchronized with a central server.
- Embedding a database engine in applications that need a lightweight, self-contained, and portable data storage solution.

SQLite can be interfaced with various programming languages, such as C, C++, Java, Python, Ruby, etc. There are also various tools and libraries that can help with creating, managing, and accessing SQLite databases, such as SQLite Studio, DB Browser for SQLite, SQLite3, etc.

To use SQLite in a C program, the following steps are required:

- Include the sqlite3.h header file in the source code.
- Link the sqlite3 library with the program.
- Call the sqlite3_open() function to create or open a database file.
- Call the sqlite3_exec() function to execute SQL statements on the database.
- Call the sqlite3_close() function to close the database connection.

The following is an example of a C program that creates a table and inserts some data into a SQLite database:

```c
#include <stdio.h>
#include <sqlite3.h>

int main()
{
    sqlite3 *db; // database handle
    char *err_msg; // error message
    int rc; // return code

    // create or open a database file
    rc = sqlite3_open("test.db", &db);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "Cannot open database: %s\n", sqlite3_errmsg(db));
        sqlite3_close(db);
        return 1;
    }

    // create a table
    char *sql = "CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER);";

    // execute the SQL statement
    rc = sqlite3_exec(db, sql, NULL, NULL, &err_msg);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "SQL error: %s\n", err_msg);
        sqlite3_free(err_msg);
        sqlite3_close(db);
        return 1;
    }

    // insert some data
    sql = "INSERT INTO students (name, age) VALUES ('Alice', 20

```
