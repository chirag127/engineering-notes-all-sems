## Data Types in MongoDB

MongoDB is a document-oriented NoSQL database that stores data in JSON-like documents. MongoDB supports a variety of data types that can be used to store data in the documents. These data types include:

### 1. String

The String data type is used to store character strings or text. Strings are enclosed in double quotes " " or single quotes ' '. Example: "Hello World".

### 2. Integer

The Integer data type is used to store whole numbers. Example: 123.

### 3. Double

The Double data type is used to store floating-point numbers. Example: 3.14.

### 4. Boolean

The Boolean data type is used to store true or false values. Example: true.

### 5. Date

The Date data type is used to store dates and times in a specific format. Dates are represented in ISODate format. Example: ISODate("2022-03-07T14:30:00.000Z").

### 6. Object ID

The Object ID data type is used to store a unique identifier for each document in a MongoDB collection. Object IDs are 12-byte hexadecimal values, with the first 4 bytes representing the timestamp, the next 3 bytes representing the machine identifier, the next 2 bytes representing the process identifier, and the last 3 bytes representing a random value.

### 7. Array

The Array data type is used to store a list of values in a single field. Arrays can store values of any data type, including other arrays. Example: ["apple", "banana", "orange"].

### 8. Embedded Document

The Embedded Document data type is used to store a document within another document. Embedded documents can contain fields of any data type, including other embedded documents and arrays. Example: {name: "John", address: {city: "New York", state: "NY"}}.

### 9. Binary Data

The Binary Data data type is used to store binary data such as images or files. Binary data is represented as a byte array.

### 10. Regular Expression

The Regular Expression data type is used to store regular expressions. Regular expressions are used to match patterns in strings. Example: /^Hello/.


MongoDB's flexible schema design allows for dynamic and complex data structures to be stored in a document-oriented database. However, it is important to carefully choose the appropriate data type for each field to ensure efficient querying and indexing of the data.