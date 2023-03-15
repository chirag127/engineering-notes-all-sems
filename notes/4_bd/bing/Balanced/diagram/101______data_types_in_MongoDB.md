#### Data Types in MongoDB

- MongoDB is a document-oriented database that stores data in BSON format, which is a binary-encoded version of JSON.
- BSON supports various data types, some of which are similar to JSON and some of which are specific to MongoDB.
- The following are some of the common data types in MongoDB:

  - String: This is the most commonly used data type to store text data. Strings must be UTF-8 valid and have a maximum size of 16 MB.
  - Integer: This is used to store numerical values that can be either 32-bit or 64-bit, depending on the server. Integers can represent values from -2^31 to 2^31-1 for 32-bit and from -2^63 to 2^63-1 for 64-bit.
  - Double: This is used to store floating-point values that follow the IEEE 754 standard. Doubles can represent values from approximately -10^308 to 10^308 with 15-17 digits of precision.
  - Boolean: This is used to store a logical value that can be either true or false.
  - Object: This is used to store an embedded document that can contain one or more key-value pairs. Objects can be nested within other objects or arrays, forming a hierarchical structure.
  - Array: This is used to store an ordered list of values that can be of any data type. Arrays can also contain other arrays or objects, forming a multidimensional structure.
  - Date: This is used to store a specific point in time as a 64-bit integer that represents the number of milliseconds since the Unix epoch (Jan 1, 1970). Dates can be manipulated using various methods in MongoDB.
  - ObjectId: This is used to store a unique identifier for a document that is generated automatically by MongoDB. ObjectIds consist of 12 bytes that encode the timestamp, machine identifier, process identifier, and a random value.
  - Binary: This is used to store binary data such as images, audio, video, etc. Binary data can have a subtype that indicates the type of data stored. Binary data has a maximum size of 16 MB.
  - JavaScript: This is used to store a JavaScript function that can be executed by MongoDB. JavaScript functions can be used in queries, aggregations, map-reduce, etc.
  - JavaScript with scope: This is similar to JavaScript, but with an additional object that specifies the scope or environment in which the function is executed. This allows the function to access variables and functions defined in the scope object.
  - Null: This is used to represent a missing or unknown value.
  - Symbol: This is similar to String, but is intended for languages that use a specific symbol type, such as Ruby. Symbols are deprecated and should not be used in new applications.
  - Regular expression: This is used to store a regular expression pattern that can be used to match or search for strings. Regular expressions follow the Perl Compatible Regular Expression (PCRE) syntax.
  - Timestamp: This is a special type of date that is used internally by MongoDB for replication and sharding. Timestamps consist of a 32-bit integer that represents the seconds since the Unix epoch and a 32-bit incrementing ordinal for operations within a given second.
  - Min key: This is a special type that compares lower than all other types. Min key is used internally by MongoDB for sharding and indexing.
  - Max key: This is a special type that compares higher than all other types. Max key is used internally by MongoDB for sharding and indexing.

- To check the data type of a value in MongoDB, you can use the `typeof` operator or the `instanceof` operator. For example:

  ```js
  // Check the type of a string
  typeof "Hello" // returns "string"

  // Check the type of an object
  typeof {name: "Alice"} // returns "object"

  // Check the type of an array
  typeof [1, 2, 3] // returns "object"

  // Check the type of a date
  typeof new Date() // returns "object"

  // Check the type of an ObjectId
  typeof ObjectId() // returns "object"

  // Check the type of a binary
  typeof BinData(0, "AQID") // returns "object"

  // Check the type of a JavaScript function
  typeof function() {} // returns "function"

  // Check the type of a null
  typeof null // returns "object"

  // Check the type of a regular expression
  typeof