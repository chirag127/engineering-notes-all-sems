A variable in Core Java is a name given to a memory location that can store a value of a specific data type. Variables can be declared using the following syntax:

`type variableName = value;`

where `type` is one of the Java's data types, such as `int`, `String`, `float`, etc., `variableName` is the name of the variable, and `value` is the initial value assigned to the variable.

There are different types of variables in Core Java, such as:

- Local variables: These are variables that are declared and used within a block, method, or constructor. They are created when the block is entered and destroyed when the block is exited. They have a local scope and must be initialized before use.
- Instance variables: These are variables that are declared in a class, outside of any method, constructor, or block. They are created when an object of the class is created and destroyed when the object is destroyed. They have a global scope and can be accessed by any method of the class. They have a default value depending on their data type, such as 0 for numeric types, false for boolean types, and null for reference types.
- Static variables: These are variables that are declared in a class, outside of any method, constructor, or block, with the `static` keyword. They are created when the class is loaded and destroyed when the class is unloaded. They have a global scope and can be accessed by any method of the class or by the class name itself. They have a default value depending on their data type, such as 0 for numeric types, false for boolean types, and null for reference types. They are also known as class variables, as they are common to all the instances of the class.
- Final variables: These are variables that are declared with the `final` keyword, which means they cannot be changed once assigned. They can be local, instance, or static variables, but they must be initialized at the time of declaration or in the constructor. They are also known as constant variables, as they have a fixed value throughout the program.

The following diagram illustrates the basic architecture of a variable in Core Java:

```
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|  Local variable | Instance variable| Static variable | Final variable  |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|  type name = value;              | static type name = value;         |
|                 |                 |                 |                 |
|  Scope: within the block,        | Scope: within the class,          |
|  method, or constructor          | accessible by class name          |
|  where it is declared            | or object reference               |
|                 |                 |                 |                 |
|  Lifetime: from the time         | Lifetime: from the time           |
|  the block is entered            | the class is loaded               |
|  to the time the block is exited | to the time the class is unloaded |
|                 |                 |                 |                 |
|  Default value: N/A              | Default value: depends on type    |
|                 |                 |                 |                 |
|  Example:                       | Example:                         |
|                 |                 |                 |                 |
|  public void add(int a, int b) { | public class Student {           |
|    int sum = a + b;              |   static int count = 0;          |
|    System.out.println(sum);      |   String name;                   |
|  }                               |   int age;                       |
|                 |                 |                 |                 |
|  sum is a local variable        |  count is a static variable      |
|                 |                 |  name and age are instance variables
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|  final type name = value;        |                 |                 |
|                 |                 |                 |                 |
|  Scope: depends on where         |                 |                 |
|  it is declared                  |                 |                 |
|                 |                 |                 |                 |
|  Lifetime: depends on where      |                 |                 |
|  it is declared                  |                 |                 |
|                 |                 |                 |                 |
|  Default value: N/A              |                 |                 |
|                 |                 |                 |                 |
|  Example