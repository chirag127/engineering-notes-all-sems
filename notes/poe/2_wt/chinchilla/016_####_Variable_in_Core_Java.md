#### Variable in Core Java

In Java, a variable is a container that holds a value or a reference to an object. It is a named memory location that stores data that can be modified during program execution. Variables are used to store values that can be used later in the program, passed between methods, or used in calculations.

Java supports different types of variables, including primitive variables and reference variables. Primitive variables hold simple data types such as integers, booleans, and characters, while reference variables hold references to objects.

##### Primitive Variables

Java has eight primitive data types, which can be used to declare primitive variables. These data types include:

1. byte: used to store small whole numbers from -128 to 127
2. short: used to store larger whole numbers from -32,768 to 32,767
3. int: used to store whole numbers from -2,147,483,648 to 2,147,483,647
4. long: used to store very large whole numbers from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
5. float: used to store decimal numbers with single precision
6. double: used to store decimal numbers with double precision
7. char: used to store single characters
8. boolean: used to store true or false values

##### Reference Variables

Reference variables hold references to objects. When an object is created, a reference to that object is returned, which can be stored in a reference variable. Reference variables are declared with the class name of the object they reference, followed by the variable name.

##### Variable Declaration and Initialization

In Java, variables must be declared before they can be used. Variable declaration specifies the variable's data type and name. Initialization assigns a value to the variable. Variables can be initialized at the time of declaration or later in the program.

##### Naming Conventions

Java has naming conventions for variables, which help to make code more readable and maintainable. Variable names should start with a lowercase letter and use camel case. Variable names should be descriptive and indicate the purpose of the variable.

##### Advantages of Variables in Java

1. Variables provide a way to store data that can be used later in the program.
2. They allow values to be passed between methods.
3. They provide a way to store references to objects.
4. They help to organize code and make it more readable.

##### Disadvantages of Variables in Java

1. Variables can be misused, leading to errors in the program.
2. They can take up memory, which can be a concern in large programs.

##### Example

```java
int x = 5;
String name = "John";
double price = 3.99;
```

In this example, three variables are declared and initialized. The variable "x" holds the value 5, the variable "name" holds the string "John", and the variable "price" holds the value 3.99.

##### Mnemonic

One mnemonic for remembering the different primitive data types in Java is:

**B**yte **S**hort **I**nteger **L**ong **F**loat **D**ouble **C**haracter **B**oolean

This mnemonic uses the first letter of each primitive data type to form a word.