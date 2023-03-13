#### Methods & Classes in Core Java

Java is an object-oriented programming language that is based on classes and objects. Methods and classes are the building blocks of any Java program. In this section, we will discuss the methods and classes in Core Java.

##### Classes in Core Java
A class in Java is a blueprint or a template that defines the behavior and properties of objects. It is a user-defined data type that encapsulates data and methods. A class can have the following components:

* Class name
* Fields (variables)
* Methods
* Constructors
* Inner classes
* Interfaces

To create an instance of a class, we need to use the "new" keyword followed by the name of the class and parentheses.

```java
ClassName objectName = new ClassName();
```

##### Methods in Core Java
A method is a block of code that performs a specific task. It is a collection of statements that are executed in sequence. A method can have the following components:

* Method signature (name and parameter list)
* Access modifier (public, private, protected)
* Return type (void, int, String, etc.)
* Method body (code block)

The syntax to define a method in Java is as follows:

```java
access_modifier return_type method_name(parameter_list) {
    // method body
    return return_value;
}
```

###### Access Modifiers in Java
Access modifiers are used to control the visibility of a class, method or variable. There are four access modifiers in Java:

* Public - public methods and variables can be accessed from anywhere in the program.
* Private - private methods and variables can only be accessed within the same class.
* Protected - protected methods and variables can be accessed within the same package and subclasses.
* Default - default methods and variables can be accessed within the same package only.

##### Method Overloading in Core Java
Method overloading is a feature in Java that allows a class to have two or more methods with the same name but different parameters. This is useful when we need to perform the same task with different types of data. The compiler determines which method to call based on the argument types.

##### Method Overriding in Core Java
Method overriding is a feature in Java that allows a subclass to provide its own implementation of a method that is already defined in its superclass. This is useful when we need to change the behavior of a method in a subclass.

##### Mnemonics and Learning Tricks
* To remember the access modifiers, use the acronym "PAD" - Public, Private, Protected, Default.
* To remember method overloading, think of it as having multiple doors to a room. Each door leads to the same room, but they have different locks (parameters).
* To remember method overriding, think of it as a child inheriting traits from their parent. The child can have some traits that are the same as the parent, but also some that are different.

In conclusion, methods and classes are essential components of any Java program. Understanding their syntax, access modifiers, and features like method overloading and overriding is crucial for writing efficient and effective Java code.