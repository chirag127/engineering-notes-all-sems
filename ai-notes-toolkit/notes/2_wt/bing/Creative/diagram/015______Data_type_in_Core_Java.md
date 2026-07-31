#### Data type in Core Java

A data type is a classification of data that specifies the type of value a variable can store or the type of an expression. Java is a strongly typed language, which means that every variable and expression has a fixed data type that cannot be changed.

There are two types of data types in Java:

- **Primitive data types**: These are the basic data types that are built-in to the Java language. They are also called simple or atomic data types. There are eight primitive data types in Java: `byte`, `short`, `int`, `long`, `char`, `float`, `double`, and `boolean`. They can store numeric, character, or boolean values.

- **Non-primitive data types**: These are the data types that are defined by the programmer or the Java library. They are also called reference or complex data types. They can store objects, arrays, strings, or any other type of data. Non-primitive data types are derived from primitive data types or other non-primitive data types.

Some characteristics of data types in Java are:

- Each data type has a fixed size and range of values that it can store.
- Each data type has a default value that is assigned to a variable if it is not initialized by the programmer.
- Each data type has a corresponding wrapper class that provides methods and constants for manipulating the data type.
- Each data type can be converted to another data type, either implicitly or explicitly, by using casting or conversion methods.

The following table summarizes the eight primitive data types in Java:

| Data type | Size (in bits) | Range of values | Default value | Wrapper class |
|-----------|----------------|-----------------|---------------|---------------|
| byte      | 8              | -128 to 127     | 0             | Byte          |
| short     | 16             | -32768 to 32767 | 0             | Short         |
| int       | 32             | -2^31 to 2^31-1 | 0             | Integer       |
| long      | 64             | -2^63 to 2^63-1 | 0L            | Long          |
| char      | 16             | 0 to 65535      | '\u0000'      | Character     |
| float     | 32             | 1.4E-45 to 3.4E38 | 0.0f        | Float         |
| double    | 64             | 4.9E-324 to 1.7E308 | 0.0d       | Double        |
| boolean   | 1              | true or false   | false         | Boolean       |