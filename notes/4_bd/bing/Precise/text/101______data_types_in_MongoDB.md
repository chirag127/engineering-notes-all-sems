#### Data Types in MongoDB

MongoDB supports several data types, including:

1. **String**: This is the most commonly used data type to store data. Strings in MongoDB must be UTF-8 valid.
2. **Integer**: This type is used to store a numerical value. Integer can be a 32-bit or 64-bit, depending on the server architecture.
3. **Boolean**: This type is used to store a boolean (true/ false) value.
4. **Double**: This type is used to store floating-point values.
5. **Min/ Max keys**: This type is used to compare a value against the lowest and highest BSON elements, respectively.
6. **Arrays**: This type is used to store arrays or lists.
7. **Timestamp**: This type is used to store a timestamp. This can be handy for recording when a document has been modified or added.
8. **Object**: This type is used to store embedded documents.
9. **Null**: This type is used to store a Null value.
10. **Symbol**: This type is used identically to a string; however, it's generally reserved for languages that use a specific symbol type.
11. **Date**: This type is used to store the current date or time in UNIX time format. You can specify your own date time by creating an object of Date and passing the date time string as a parameter.
12. **Object ID**: This type is used to store the document’s ID.
13. **Binary data**: This type is used to store binary data.
14. **Code**: This type is used to store JavaScript code into the document.
15. **Regular expression**: This type is used to store regular expression.

These are the most commonly used data types in MongoDB. Each data type has its own specific use case and it is important to choose the right data type for the data being stored.