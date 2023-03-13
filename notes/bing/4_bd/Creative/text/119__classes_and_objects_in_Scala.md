#### Classes and Objects in Scala

- Classes in Scala are blueprints for creating objects. They can contain methods, values, variables, types, objects, traits, and classes which are collectively called members .
- Objects in Scala are instances of classes. They can be created using the `new` keyword or using companion objects.
- A minimal class definition is simply the keyword `class` and an identifier (name) of the class. For example:

```scala
class Person
```

- A class can have a primary constructor that takes parameters and initializes the fields of the object. The parameters are defined in the class header after the name of the class . For example:

```scala
class Person(firstName: String, lastName: String)
```

- A class can also have methods that define the behavior of the object. Methods are defined using the `def` keyword followed by the name, parameters, return type, and body of the method . For example:

```scala
class Person(firstName: String, lastName: String) {
  def fullName: String = firstName + " " + lastName
}
```

- A class can also have values and variables that store the state of the object. Values are defined using the `val` keyword and are immutable, meaning they cannot be reassigned. Variables are defined using the `var` keyword and are mutable, meaning they can be reassigned . For example:

```scala
class Person(firstName: String, lastName: String) {
  val age: Int = 0 // a value that cannot be changed
  var email: String = "" // a variable that can be changed
}
```

- A class can also have types, objects, traits, and classes as its members, which will be covered later in the tour.
- A companion object is an object that has the same name as a class and is defined in the same file. A companion object can access the private members of the class and can provide a factory method for creating objects without using the `new` keyword. For example:

```scala
class Person(firstName: String, lastName: String) {
  // class definition
}

object Person {
  // companion object definition
  def apply(firstName: String, lastName: String): Person = {
    new Person(firstName, lastName)
  }
}
```

- To create an object of a class, you can use the `new` keyword followed by the name of the class and the arguments for the constructor. Alternatively, you can use the companion object's `apply` method if it is defined . For example:

```scala
val p1 = new Person("John", "Doe") // using the new keyword
val p2 = Person("Jane", "Doe") // using the companion object
```

- To access the members of an object, you can use the dot (`.`) notation followed by the name of the member. For example:

```scala
val name = p1.fullName // accessing the fullName method
p2.email = "jane.doe@example.com" // assigning a new value to the email variable
```