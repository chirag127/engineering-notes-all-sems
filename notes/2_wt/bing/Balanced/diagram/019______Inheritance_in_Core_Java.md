Inheritance in Java is one of the core concepts of Object-Oriented Programming. It enables a class to inherit the properties and methods of another class. The class that inherits is called the subclass or child class, and the class that is inherited from is called the superclass or parent class. The keyword `extends` is used to indicate inheritance in Java.

A simple example of inheritance in Java is:

```java
// Superclass
class Animal {
  // properties
  String name;
  int age;

  // methods
  public void eat() {
    System.out.println(name + " is eating.");
  }

  public void sleep() {
    System.out.println(name + " is sleeping.");
  }
}

// Subclass
class Dog extends Animal {
  // additional property
  String breed;

  // additional method
  public void bark() {
    System.out.println(name + " is barking.");
  }
}
```

In this example, the class `Dog` inherits the properties and methods of the class `Animal`. The class `Dog` can also have its own additional properties and methods, such as `breed` and `bark()`.

A diagram of inheritance in Java can be drawn using ASCII characters, such as:

#### Inheritance in Core Java

```
+-----------------+
|    Animal       |
+-----------------+
| - name: String  |
| - age: int      |
+-----------------+
| + eat(): void   |
| + sleep(): void |
+-----------------+
        ^
        |
        |
+-----------------+
|    Dog          |
+-----------------+
| - breed: String |
+-----------------+
| + bark(): void  |
+-----------------+
```

The symbol `+` indicates public access, the symbol `-` indicates private access, and the symbol `^` indicates inheritance. The diagram shows that the class `Dog` inherits from the class `Animal`, and has access to its public properties and methods. The class `Dog` also has its own private property `breed` and public method `bark()`.