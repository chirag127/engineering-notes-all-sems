According to the web search results, MongoDB supports many data types that are stored in BSON format, which is the binary encoded format of JSON. Some of the common data types are:

- String: This is the most commonly used data type to store the data. String in MongoDB must be UTF-8 valid.
- Integer: This type is used to store a numerical value. 32 bit or 64-bit integers are supported, which depends on the server.
- Double: This type is used to store floating-point values.
- Boolean: This type is used to store a boolean (true or false) value.
- Date: This type is used to store the current date and time as a UNIX timestamp.
- ObjectId: This type is used to store a 12-byte hexadecimal value that is unique for every document in a collection.
- Array: This type is used to store an array or list of values under a single key.
- Object: This type is used to store an embedded document, which is a document within another document.
- Null: This type is used to store a null value.
- Symbol: This type is used to store a string that is reserved for languages that have a specific symbol type.
- MinKey: This type is used to compare a value against the lowest possible BSON value.
- MaxKey: This type is used to compare a value against the highest possible BSON value.
- Decimal128: This type is used to store a 128-bit decimal-based floating-point number that supports 34 decimal digits and an exponent range of −6143 to +6144.
- Timestamp: This type is used to store a 64-bit value that represents the number of seconds since the UNIX epoch and an incrementing ordinal for operations within a single second.
- Binary: This type is used to store binary data.
- Code: This type is used to store JavaScript code that can be executed by MongoDB.

The following diagram illustrates the basic architecture of a MongoDB document with different data types:

```
+------------------------+
| MongoDB Document       |
+------------------------+
| _id: ObjectId          |
| name: String           |
| age: Integer           |
| score: Double          |
| active: Boolean        |
| joined: Date           |
| hobbies: Array         |
| address: Object        |
| email: Null            |
| role: Symbol           |
| min: MinKey            |
| max: MaxKey            |
| salary: Decimal128     |
| updated: Timestamp     |
| image: Binary          |
| validate: Code         |
+------------------------+
```