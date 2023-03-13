#### Data type in Core Java

- A data type is a classification of data that specifies how the data is stored, manipulated, and interpreted by the compiler or the interpreter.
- Data types in Core Java can be divided into two categories: primitive and reference.
- Primitive data types are the basic types of data that are built-in to the Java language. They are predefined and have fixed sizes and ranges. There are eight primitive data types in Java: byte, short, int, long, float, double, char, and boolean.
- Reference data types are the types of data that refer to objects or arrays. They are created by the programmer using class or interface definitions. Reference data types can store null values, which indicate the absence of an object or an array. Reference data types do not have fixed sizes or ranges, and their values depend on the implementation of the class or the interface.
- The following table summarizes the characteristics of the primitive data types in Java:

| Data type | Size (in bits) | Range | Default value |
|-----------|----------------|-------|---------------|
| byte      | 8              | -128 to 127 | 0             |
| short     | 16             | -32768 to 32767 | 0           |
| int       | 32             | -2147483648 to 2147483647 | 0       |
| long      | 64             | -9223372036854775808 to 9223372036854775807 | 0L    |
| float     | 32             | 1.4E-45 to 3.4028235E38 | 0.0f      |
| double    | 64             | 4.9E-324 to 1.7976931348623157E308 | 0.0d    |
| char      | 16             | 0 to 65535 | '\u0000'       |
| boolean   | 1              | true or false | false        |

- The following are some examples of declaring and initializing variables of different primitive data types in Java:

```java
// Declare a byte variable named b and assign it the value 100
byte b = 100;

// Declare a short variable named s and assign it the value 20000
short s = 20000;

// Declare an int variable named i and assign it the value 1000000
int i = 1000000;

// Declare a long variable named l and assign it the value 1000000000000L
long l = 1000000000000L;

// Declare a float variable named f and assign it the value 3.14f
float f = 3.14f;

// Declare a double variable named d and assign it the value 3.14159
double d = 3.14159;

// Declare a char variable named c and assign it the value 'A'
char c = 'A';

// Declare a boolean variable named flag and assign it the value true
boolean flag = true;
```

- The following are some examples of declaring and initializing variables of different reference data types in Java:

```java
// Declare a String variable named str and assign it the value "Hello"
String str = "Hello";

// Declare an Integer variable named num and assign it the value 10
Integer num = 10;

// Declare an ArrayList variable named list and assign it a new empty ArrayList object
ArrayList list = new ArrayList();

// Declare a Scanner variable named sc and assign it a new Scanner object that reads from the standard input
Scanner sc = new Scanner(System.in);

// Declare a Student variable named stu and assign it the value null
Student stu = null;
```

- A mnemonic to remember the order of the primitive data types from smallest to largest size is: **Be Sure It's Long For Double Char Booleans**. (byte, short, int, long, float, double, char, boolean)