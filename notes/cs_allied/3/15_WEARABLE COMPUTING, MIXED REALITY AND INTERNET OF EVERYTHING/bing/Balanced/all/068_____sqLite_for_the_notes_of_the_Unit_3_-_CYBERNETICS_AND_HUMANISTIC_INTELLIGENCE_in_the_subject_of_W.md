# SQLite for the notes of the Unit 3 - CYBERNETICS AND HUMANISTIC INTELLIGENCE in the subject of WEARABLE COMPUTING, MIXED REALITY AND INTERNET OF EVERYTHING

SQLite is a software library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine. SQLite is the most widely deployed SQL database engine in the world. The source code for SQLite is in the public domain.

Some of the main features of SQLite are:

- It is embedded into the application that uses it, so there is no need for a separate database server or process.
- It supports most of the standard SQL syntax and features, such as data types, constraints, indexes, views, triggers, transactions, etc.
- It is portable and cross-platform, as it does not depend on any external libraries or operating systems.
- It is lightweight and efficient, as it uses a single file to store the entire database and has a small memory footprint.
- It is reliable and robust, as it uses atomic commit and rollback to ensure data integrity and durability.

SQLite can be used for various applications that require structured data management, such as:

- Wearable computing devices, such as smartwatches, fitness trackers, etc., that need to store and process sensor data, user preferences, etc.
- Mixed reality applications, such as augmented reality, virtual reality, etc., that need to store and render 3D models, images, sounds, etc.
- Internet of everything applications, such as smart home, smart city, smart grid, etc., that need to store and communicate data from various devices, sensors, actuators, etc.

To use SQLite in your application, you need to:

- Download and install the SQLite library or use a precompiled binary for your platform.
- Include the SQLite header file in your source code and link with the SQLite library.
- Use the SQLite API functions to open, create, query, and manipulate the database.
- Close the database connection when you are done.

Some of the basic SQLite API functions are:

- `sqlite3_open()` - opens or creates a database file and returns a database connection object.
- `sqlite3_exec()` - executes a SQL statement on the database and optionally invokes a callback function for each row of the result set.
- `sqlite3_prepare()` - prepares a SQL statement for execution and returns a statement object.
- `sqlite3_step()` - executes a prepared statement and returns a status code indicating the result.
- `sqlite3_column_*()` - returns the value of a column in the current row of the result set of a prepared statement.
- `sqlite3_finalize()` - finalizes a prepared statement and frees the associated resources.
- `sqlite3_close()` - closes a database connection and frees the associated resources.

For more details and examples of SQLite, you can refer to the following sources   .

: SQLite Database Tutorial for Beginners: Learn with Examples - Guru99
: SQLite Tutorial - Learn SQLite basic to advanced concepts
: SQLite Tutorial - An Easy Way to Master SQLite Fast
: Getting Started with SQLite Quickly - SQLite Tutorial
: SQLite Tutorial - Tutorialspoint