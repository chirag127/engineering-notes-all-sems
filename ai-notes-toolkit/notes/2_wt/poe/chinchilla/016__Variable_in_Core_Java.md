#### Variable in Core Java

In Java, a variable is a container that can store a value or a reference to an object. A variable is a named memory location that can hold data of a particular type. Java variables can be classified into two types: primitive data types and reference data types.

##### Primitive Data Types

Primitive data types are the basic data types in Java. They are predefined by the Java language and include the following:

1. byte - an 8-bit signed integer
2. short - a 16-bit signed integer
3. int - a 32-bit signed integer
4. long - a 64-bit signed integer
5. float - a 32-bit floating-point number
6. double - a 64-bit floating-point number
7. boolean - a true/false value
8. char - a single Unicode character

##### Reference Data Types

Reference data types are used to store objects. They include classes, interfaces, arrays, and enumerated types. Reference variables hold a reference to an object in memory rather than the object itself.

##### Variable Declaration

To declare a variable in Java, we need to specify its data type and name. The syntax for declaring a variable is:

```
datatype variableName;
```

For example, to declare an integer variable named "age", we would use the following code:

```
int age;
```

##### Variable Initialization

Variable initialization is the process of assigning a value to a variable. In Java, variables can be initialized at the time of declaration or later in the program. The syntax for initializing a variable is:

```
datatype variableName = value;
```

For example, to declare and initialize an integer variable named "count" with a value of 10, we would use the following code:

```
int count = 10;
```

##### Variable Scope

The scope of a variable is the region of the program where the variable is accessible. In Java, the scope of a variable depends on where it is declared. Variables declared inside a method or block are only accessible within that method or block. Variables declared outside a method or block but within a class are accessible to all methods in the class.

##### Final Variables

A final variable is a variable that cannot be changed once it has been initialized. In Java, final variables are declared using the "final" keyword. Once a final variable has been initialized, it cannot be reassigned.

##### Static Variables

A static variable is a variable that belongs to a class rather than an instance of the class. Static variables are declared using the "static" keyword. They are accessible to all instances of the class and can be accessed using the class name.

##### Conclusion

Variables are an essential part of any programming language. In Java, variables provide a way to store and manipulate data. Understanding how to declare, initialize, and use variables is critical to writing effective Java programs.