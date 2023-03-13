Inheritance in Java is one of the core concepts of Object-Oriented Programming. It enables a class to inherit the properties and methods of another class. The class that inherits is called the subclass or child class, and the class that is inherited from is called the superclass or parent class. The subclass can access the members of the superclass, and also add its own members. The subclass can also override the methods of the superclass, to provide a different implementation. Inheritance in Java is implemented using the extends keyword.

The following diagram illustrates the basic concept of inheritance in Java using ASCII art:

#### Inheritance in Java

<pre>
    +-----------------+
    |    Superclass   |
    |-----------------|
    | + field1        |
    | + field2        |
    |-----------------|
    | + method1()     |
    | + method2()     |
    +-----------------+
            ^
            |
            |
            |
    +-----------------+
    |    Subclass     |
    |-----------------|
    | + field3        |
    |-----------------|
    | + method1()     |  // overriding method1 of superclass
    | + method3()     |
    +-----------------+
</pre>