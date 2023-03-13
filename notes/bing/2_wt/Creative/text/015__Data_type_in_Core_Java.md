#### Data type in Core Java

- A data type is a classification of data that specifies how the data is stored, manipulated, and interpreted by the compiler or the interpreter.
- Data types can be divided into two categories: primitive and reference.
- Primitive data types are the basic types of data that are built-in to the Java language. They are predefined and have fixed sizes and ranges. There are eight primitive data types in Java: byte, short, int, long, float, double, char, and boolean.
- Reference data types are the types of data that refer to objects or arrays. They are created by the programmer using class or interface definitions. Reference data types can store null values, which indicate the absence of an object or array. Reference data types can also be generic, which means they can hold values of different types depending on the type parameter specified.
- The following table summarizes the characteristics of the primitive data types in Java:

| Data type | Size (in bits) | Range | Default value |
|-----------|----------------|-------|---------------|
| byte      | 8              | -128 to 127 | 0             |
| short     | 16             | -32768 to 32767 | 0           |
| int       | 32             | -2147483648 to 2147483647 | 0       |
| long      | 64             | -9223372036854775808 to 9223372036854775807 | 0L    |
| float     | 32             | 1.4E-45 to 3.4028235E38 | 0.0f       |
| double    | 64             | 4.9E-324 to 1.7976931348623157E308 | 0.0d    |
| char      | 16             | 0 to 65535 | '\u0000'        |
| boolean   | 1              | true or false | false        |

- The following table summarizes the characteristics of the reference data types in Java:

| Data type | Size (in bytes) | Default value | Example |
|-----------|-----------------|---------------|---------|
| Class     | Varies          | null          | String, Integer, Scanner, etc. |
| Interface | Varies          | null          | List, Set, Map, etc. |
| Array     | Varies          | null          | int[], String[], Object[], etc. |
| Generic   | Varies          | null          | List<String>, Map<Integer, String>, etc. |