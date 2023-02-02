### Persisting data using SQLite for the notes of the Unit 4 - Technology I – ANDROID of Design & Development Of Applications ( KCS075) in the subject of Design & Development Of Applications ( KCS075)
SQLite is a software library that provides a relational database management system. It can be used to persist data in Android applications.

To use SQLite in an Android app, you can use the SQLiteOpenHelper class, which provides a convenient way to manage the SQLite database.

Here are the steps to persist data using SQLite in an Android app:

1. Create a new class that extends SQLiteOpenHelper.
2. Override the onCreate() and onUpgrade() methods to create and upgrade the database.
3. In the onCreate() method, use the SQLiteDatabase object to create tables and insert data into the database.
4. In the onUpgrade() method, upgrade the database by adding or modifying tables and data.
5. In your activity, use the SQLiteOpenHelper object to open and close the database connection.
6. Use the SQLiteDatabase object to perform CRUD (Create, Read, Update, Delete) operations on the database.

This is a basic example of how to persist data using SQLite in an Android app. There are many other advanced features that you can use, such as transactions, cursors, and raw SQL queries.
