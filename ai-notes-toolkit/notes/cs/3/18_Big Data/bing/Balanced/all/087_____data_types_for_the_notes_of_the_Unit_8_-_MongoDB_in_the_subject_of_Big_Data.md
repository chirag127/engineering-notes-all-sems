# Data Types for the Notes of the Unit 8 - MongoDB in the Subject of Big Data

- MongoDB is a document-oriented database that stores data in JSON-like format.
- MongoDB supports various data types, such as strings, numbers, booleans, arrays, objects, dates, null, and binary data.
- Strings are sequences of UTF-8 characters enclosed in double quotes. For example, `"Hello world"`.
- Numbers can be either 64-bit floating point values or 64-bit integer values. For example, `3.14` or `42`.
- Booleans are either `true` or `false`.
- Arrays are ordered collections of values enclosed in square brackets. For example, `[1, 2, 3]` or `["red", "green", "blue"]`.
- Objects are unordered collections of key-value pairs enclosed in curly braces. For example, `{"name": "Alice", "age": 25}` or `{"_id": ObjectId("507f191e810c19729de860ea"), "title": "MongoDB Tutorial"}`.
- Dates are represented as ISODate objects that store the number of milliseconds since the Unix epoch. For example, `ISODate("2021-12-15T20:51:46Z")`.
- Null is a special value that represents the absence of a value. For example, `null`.
- Binary data is a sequence of bytes that can store any kind of data, such as images, audio, or video. For example, `BinData(0, "5q2+7w==")`.