A variable in core Java is a data container that stores the data values during Java program execution. Every variable is assigned a data type that designates the type and quantity of value it can hold. A variable is a name given to a memory location. It is the basic unit of storage in a program .

Variables in Java can be defined anywhere in the code (inside a class, inside a method, or as a method argument) and can have different modifiers. Depending on these conditions variables in Java can be divided into four categories:

- Instance Variable: These are non-static variables that are declared inside a class but outside a method. They are also called object variables or fields. They are initialized when an object of the class is created and can be accessed by all the methods of the class.
- Static Variable: These are also known as class variables. They are declared inside a class but outside a method with the static keyword. They are initialized only once at the start of the program execution and can be accessed by all the methods of the class and other classes.
- Local Variable: These are variables that are declared inside a method or a block of code. They are also called method variables. They are created when the method is invoked and destroyed when the method is completed. They are only visible within the method or block of code where they are declared.
- Parameter Variable: These are variables that are declared as part of the method signature. They are also called method parameters or arguments. They are used to pass values to the method when it is invoked. They are only visible within the method where they are declared.

A possible ASCII diagram for variable in core Java is:

#### Variable in Core Java
```
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|    Instance     |     Static      |     Local       |    Parameter    |
|    Variable     |    Variable     |    Variable     |    Variable     |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
```