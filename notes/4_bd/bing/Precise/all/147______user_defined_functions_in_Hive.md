#### User Defined Functions in Hive

Hive is a data warehousing and SQL-like query language for Hadoop, which enables users to perform data analysis on large datasets. One of the powerful features of Hive is the ability to create custom functions, known as User Defined Functions (UDFs), to perform complex data manipulations.

Here are some key points to know about User Defined Functions in Hive:

1. UDFs can be written in Java or other JVM languages such as Scala or Groovy.
2. UDFs can be used to perform operations that are not easily achievable using built-in Hive functions.
3. UDFs can be used in Hive queries just like built-in functions.
4. UDFs can be either temporary or permanent. Temporary UDFs are available only for the current session, while permanent UDFs are stored in the Hive metastore and can be used across sessions.
5. UDFs can be created using the `CREATE FUNCTION` statement in HiveQL.
6. UDFs can be shared and reused by other users.

In summary, User Defined Functions in Hive provide a powerful way to extend the functionality of Hive and perform complex data manipulations. They can be written in a variety of JVM languages, and can be either temporary or permanent. UDFs can be easily used in Hive queries and shared with other users.