A variable in Core Java is a data container that saves the data values during Java program execution. Every variable is assigned a data type that designates the type and quantity of value it can hold. A variable is a name given to a memory location. It is the basic unit of storage in a program.

Variables in Java can be defined anywhere in the code (inside a class, inside a method, or as a method argument) and can have different modifiers. Depending on these conditions variables in Java can be divided into four categories:

- Instance Variable: A variable that is declared inside a class but outside a method is known as an instance variable. It is not declared as static. It is called instance variable because its value is instance specific and is not shared among instances.
- Static Variable: A variable that is declared as static is known as static variable. It cannot be local. You can create a single copy of static variable and share among all the instances of the class. Memory allocation for static variable happens only once when the class is loaded in the memory.
- Local Variable: A variable that is declared inside the method is called local variable. You can use this variable only within that method and the other methods in the class aren't even aware that the variable exists. A local variable cannot be defined with static keyword.
- Parameter Variable: A variable that is declared inside the parenthesis of the method is called parameter variable. It is used to pass the value to the method.

The following diagram illustrates the basic architecture of a variable in Core Java:

#### Variable in Core Java

```
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|  Class Name     |  Instance       |  Static         |  Local          |
|                 |  Variable       |  Variable       |  Variable       |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|  class Example  |  int x;         |  static int y;  |  void method()  |
|                 |                 |                 |  {              |
|                 |                 |                 |    int z;       |
|                 |                 |                 |  }              |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|  Memory         |  Heap Memory    |  Static Memory  |  Stack Memory   |
|  Allocation     |                 |                 |                 |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|  Value          |  Instance       |  Shared         |  Method         |
|  Sharing        |  Specific       |  Among All      |  Specific       |
|                 |                 |  Instances      |                 |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
```