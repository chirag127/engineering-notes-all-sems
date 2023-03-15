# Data Types for the Notes of the Unit 8 - MongoDB in the Subject of Big Data

- MongoDB is a document-oriented database that stores data in BSON format, which is a binary representation of JSON.
- BSON supports various data types, some of which are common to JSON and some of which are specific to MongoDB .
- The following are some of the common data types in MongoDB   :

  - **String**: This is the most commonly used data type to store text. Strings in MongoDB must be UTF-8 valid .
  - **Integer**: This is the data type to store numerical values. MongoDB supports 32-bit or 64-bit integers, depending on the server .
  - **Double**: This is the data type to store floating-point numbers. MongoDB uses 64-bit IEEE 754 floating point to store doubles  .
  - **Boolean**: This is the data type to store true or false values .
  - **Array**: This is the data type to store a list of values in a single field. Arrays can contain values of any data type, including nested arrays  .
  - **Object**: This is the data type to store a document or a subdocument in a field. Objects can contain fields of any data type, including nested objects  .
  - **Date**: This is the data type to store date and time values. MongoDB stores dates as 64-bit integers that represent the number of milliseconds since the Unix epoch (Jan 1, 1970)  .
  - **Timestamp**: This is the data type to store a 64-bit value that consists of a 32-bit seconds field and a 32-bit increment field. Timestamps are used internally by MongoDB for replication and sharding  .
  - **ObjectId**: This is the data type to store a 12-byte value that uniquely identifies a document in a collection. ObjectId consists of a 4-byte timestamp, a 5-byte random value, and a 3-byte incrementing counter  .
  - **Binary**: This is the data type to store binary data, such as images, audio, or video. MongoDB supports various binary subtypes, such as generic binary, UUID, MD5, or user-defined  .
  - **Null**: This is the data type to store a null value, which represents the absence of a value .
  - **Symbol**: This is the data type to store a string that is intended to be used as a symbol. Symbols are similar to strings, but are not indexed and can only be used in certain contexts  .
  - **Code**: This is the data type to store JavaScript code that can be executed by MongoDB. Code can be stored as a string or as a code with scope, which is an object that contains the code and an associated scope  .
  - **Regular Expression**: This is the data type to store a regular expression that can be used to match patterns in strings. MongoDB uses the Perl Compatible Regular Expression (PCRE) library to implement regular expressions  .
  - **MinKey**: This is the data type to store a value that compares less than any other value in BSON  .
  - **MaxKey**: This is the data type to store a value that compares greater than any other value in BSON  .

- To specify the data type of a field in MongoDB, you can use the `$type` operator in queries or the `typeof` operator in JavaScript .
- To convert a value from one data type to another, you can use the `$convert` aggregation operator or the `Number()`, `String()`, `Boolean()`, `Date()`, `ObjectId()`,