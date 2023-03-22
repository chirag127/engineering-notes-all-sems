 Here is the content in Markdown format without any emojis or external links:

### Classes and Objects for Unit 10 - Scala Notes

1. A class is a blueprint that defines the structure and behavior of a type of object.
2. An object is an instance of a class. When a class is defined, no memory is allocated but when an object is created/instantiated, memory is allocated.
3. Defining a class:
```scala
class ClassName {
// class body
}
```
4. Instantiating a class:
```scala
val obj = new ClassName
```
5. Adding parameters to classes:
```scala
class Person(name: String) {
  // body
}

val p = new Person("John")
```
6. Adding methods to classes:
```scala
class Person(name: String) {
  def greet(): Unit = println(s"Hello, my name is $name")
}

val p = new Person("John")
p.greet() // Hello, my name is John
```
7. Using constructor overloading: Having multiple constructors for a class.
8. Using default and named arguments.
9. Case classes: Immutable classes mainly used for pattern matching. Defined using `case class` and have some additional features like decompiler-friendly toString, extractors, etc.

The content is written in points in Markdown format without any emojis or external links as formal study material. Please let me know if you would like me to modify or add any other points.