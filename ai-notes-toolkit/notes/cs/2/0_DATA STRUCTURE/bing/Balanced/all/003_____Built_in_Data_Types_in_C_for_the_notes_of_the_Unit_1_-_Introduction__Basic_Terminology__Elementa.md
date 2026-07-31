Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of Built in Data Types in C:

# Built in Data Types in C

- C is a strongly typed language, which means that every variable must have a specific data type.
- A data type defines the size, range, and format of the data that can be stored in a variable.
- C provides several built in data types, such as int, char, float, double, etc.
- Each built in data type has a corresponding keyword, which is used to declare variables of that type.
- For example, to declare a variable named x of type int, we write:

```c
int x;
```

- The size and range of each built in data type may vary depending on the compiler and the platform, but the following table shows the typical values:

| Data Type | Keyword | Size (in bytes) | Range |
|-----------|---------|-----------------|-------|
| Integer   | int     | 4               | -2,147,483,648 to 2,147,483,647 |
| Character | char    | 1               | -128 to 127 or 0 to 255 |
| Floating point | float | 4 | 3.4E-38 to 3.4E+38 |
| Double precision floating point | double | 8 | 1.7E-308 to 1.7E+308 |

- C also allows the use of modifiers to create derived data types from the built in data types.
- Modifiers are keywords that modify the size or range of the data type.
- The most common modifiers are short, long, unsigned, and signed.
- For example, to declare a variable named y of type long int, we write:

```c
long int y;
```

- The following table shows the effect of modifiers on the size and range of the data types:

| Data Type | Modifier | Size (in bytes) | Range |
|-----------|----------|-----------------|-------|
| Integer   | short    | 2               | -32,768 to 32,767 |
| Integer   | long     | 8               | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |
| Integer   | unsigned | 4               | 0 to 4,294,967,295 |
| Integer   | signed   | 4               | -2,147,483,648 to 2,147,483,647 |
| Character | unsigned | 1               | 0 to 255 |
| Character | signed   | 1               | -128 to 127 |
| Floating point | long  | 8               | 3.4E-38 to 3.4E+38 |
| Double precision floating point | long | 16 | 1.7E-308 to 1.7E+308 |

- C also supports the use of constants, which are fixed values that cannot be changed during the execution of the program.
- Constants can be of any data type, and are declared using the const keyword.
- For example, to declare a constant named PI of type double, we write:

```c
const double PI = 3.14;
```

- C also provides some special data types, such as void, enum, and struct, which will be discussed later in the course.