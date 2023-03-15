### Unit 10 - SCALA: Classes and Objects

- **Classes** in Scala are blueprints for creating objects. They can contain methods, values, variables, types, objects, traits, and classes which are collectively called members.

- A **class** is defined using the `class` keyword, followed by its name and constructor parameters.

```scala
class MyClass(param1: Type1, param2: Type2) {
  // Class body
}
```

- The **constructor** of a class is executed when an object is created from the class using the `new` keyword.

```scala
val myObject = new MyClass(arg1, arg2)
```

- **Objects** in Scala are single instances of their own definitions. They are defined using the `object` keyword.

```scala
object MyObject {
  // Object body
}
```

- Objects can have the same members as classes, but they cannot have constructor parameters.

- Objects are often used to hold single instances of a class, or to define singleton objects that provide utility methods.

- In Scala, classes and objects can be defined in the same file, and they can have the same name. When this is done, the object is called a **companion object**.

- A companion object is often used to define factory methods for creating instances of the class, or to define methods and values that are shared by all instances of the class.

- In summary, classes and objects in Scala provide a way to define and create instances of custom data types, with their own methods and properties. They are fundamental building blocks of object-oriented programming in Scala.