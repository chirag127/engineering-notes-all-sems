#### User defined functions in Hive

User defined functions (UDFs) are custom functions that can be developed in Java, integrated with Hive, and built on top of a Hadoop cluster to allow for efficient and complex computation that would not otherwise be possible with simple SQL. They can be useful and very powerful, and yet online documentation is pretty weak.

Some of the features of UDFs in Hive are:

- UDFs can be written in Java for specific modules.
- UDFs can read and return primitive types, such as int, string, boolean, etc., or complex types, such as arrays, maps, structs, etc.
- UDFs can be registered in Hive using the CREATE FUNCTION command or the ADD JAR command .
- UDFs can be categorized into three types: scalar, generic, and table.
- Scalar UDFs take one or more input values and return a single output value.
- Generic UDFs can handle complex types and null values, and can also implement type inference and variable argument length.
- Table UDFs take one or more input values and return a table of values, such as explode, lateral view, etc.

Some of the examples of UDFs in Hive are:

- datediff: returns the number of days between two dates.
- date_add: returns the date after adding a number of days to a given date.
- decode: returns a string decoded from a binary input using a specified character set.
- concat: returns a string that is the concatenation of two or more input strings.
- upper: returns a string that is the uppercase version of the input string.
- sqrt: returns the square root of the input double value.