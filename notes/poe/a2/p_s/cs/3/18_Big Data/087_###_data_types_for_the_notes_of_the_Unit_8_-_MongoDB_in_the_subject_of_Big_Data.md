 Here are the data types for MongoDB in markdown format for the notes of Unit 8 - MongoDB in the subject of Big Data:

### Data Types

The following are the data types supported by MongoDB:

1. String
- Used to store text data.
- Stores values in UTF-8 encoding.
- Has a limit of 1024 bytes.

2. Integer
- Used to store whole numbers.
- Supports 32-bit/64-bit integers.
- Has a limit of ±2^31-1 or ±2^63-1 values based on 32-bit or 64-bit respectively.

3. Boolean
- Stores true or false values.
- Occupy only 1 byte of space.

4. Double
- Used to store floating point values.
- Represented in IEEE 754 64-bit format.
- Has a limit of ±2^53 values with precision of 15-17 decimal digits.

5. Min/Max keys
- Special data types to compare and sort values.
- Do not store user data.
- Used to specify inclusive/exclusive bounds for a range query.

6. Arrays
- Used to store ordered lists of values.
- Elements can be of any data type including other arrays.
- Has a limit of 65536 elements per array.

7. Embedded documents
- Complex data structures can be modeled using documents which are stored as values in a single document.
- Embedded documents have a limit of 16 MB.

8. Object IDs
- Special data type used to represent a unique ID for documents.
- Composed of a 12-byte value consisting of:
-- 4-byte value representing seconds since the Unix epoch,
-- 3-byte machine identifier,
-- 2-byte process id, and
-- 3-byte counter.
- Useful for creating relationships between documents and in sharding.