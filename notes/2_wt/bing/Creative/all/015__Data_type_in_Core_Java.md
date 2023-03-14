#### Data type in Core Java

- A data type is a classification of data that specifies how the data is stored, manipulated, and interpreted by the compiler or the interpreter.
- Data types in Core Java can be divided into two categories: primitive and reference.
- Primitive data types are the basic types of data that are built-in to the Java language. They are predefined and have fixed sizes and ranges. There are eight primitive data types in Java: byte, short, int, long, float, double, char, and boolean.
- Reference data types are the types of data that are defined by the programmer or by the Java API. They are not predefined and can have variable sizes and ranges. Reference data types store the address or reference of an object, not the object itself. Examples of reference data types are classes, interfaces, arrays, and strings.
- The following table summarizes the characteristics of the primitive data types in Java:

| Data type | Size (in bits) | Range | Default value | Example |
|-----------|----------------|-------|---------------|---------|
| byte      | 8              | -128 to 127 | 0 | byte b = 10; |
| short     | 16             | -32768 to 32767 | 0 | short s = 100; |
| int       | 32             | -2147483648 to 2147483647 | 0 | int i = 1000; |
| long      | 64             | -9223372036854775808 to 9223372036854775807 | 0L | long l = 100000L; |
| float     | 32             | 1.4E-45 to 3.4E38 | 0.0f | float f = 10.5f; |
| double    | 64             | 4.9E-324 to 1.7E308 | 0.0d | double d = 10.5d; |
| char      | 16             | 0 to 65535 | '\u0000' | char c = 'A'; |
| boolean   | 1              | true or false | false | boolean b = true; |

- The following are some points to remember about data types in Core Java:
  - Primitive data types are faster and more efficient than reference data types, as they do not involve any memory allocation or garbage collection.
  - Reference data types are more flexible and powerful than primitive data types, as they can store complex data structures and support inheritance, polymorphism, and abstraction.
  - Primitive data types can be converted to reference data types by using wrapper classes, such as Integer, Double, Character, and Boolean. Wrapper classes provide methods and fields to manipulate the primitive values as objects.
  - Reference data types can be converted to primitive data types by using the unboxing operation, which extracts the primitive value from the wrapper object.
  - Java supports type casting, which is the conversion of one data type to another. Type casting can be either implicit or explicit. Implicit type casting is done automatically by the compiler when there is no loss of information or precision. Explicit type casting is done by the programmer using the cast operator ( ) when there is a possibility of loss of information or precision.
  - Java also supports type inference, which is the ability of the compiler to determine the data type of a variable based on the value assigned to it. Type inference can be used with the var keyword, which declares a local variable without specifying its data type. The compiler will infer the data type of the variable based on the value assigned to it. For example, var x = 10; will declare a variable x of type int. Type inference can only be used with local variables, not with fields, parameters, or return types.