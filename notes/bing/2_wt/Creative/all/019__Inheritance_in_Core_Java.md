#### Inheritance in Core Java

- Inheritance is one of the fundamental concepts of object-oriented programming (OOP) in Java.
- Inheritance allows a class to acquire the properties and methods of another class, called the superclass or parent class.
- The class that inherits from the superclass is called the subclass or child class.
- Inheritance enables code reuse, polymorphism, and abstraction.
- In Java, inheritance is achieved by using the `extends` keyword.
- A subclass can inherit from only one superclass in Java, which means Java does not support multiple inheritance directly.
- However, a subclass can implement multiple interfaces, which can provide a form of multiple inheritance.
- A subclass inherits all the public and protected members of the superclass, but not the private members.
- A subclass can access the inherited members directly, or override them to provide a different implementation.
- A subclass can also define its own members, which are not inherited by any other class.
- A subclass can invoke the constructor of the superclass by using the `super` keyword, which must be the first statement in the subclass constructor.
- A subclass can also use the `super` keyword to access the inherited members of the superclass that are hidden or overridden by the subclass.
- A subclass can be further subclassed, forming an inheritance hierarchy.
- The `Object` class is the root of the inheritance hierarchy in Java, and every class is a subclass of `Object` either directly or indirectly.
- The `Object` class provides some common methods that are inherited by all classes, such as `toString()`, `equals()`, `hashCode()`, etc.

Here is an example of inheritance in Java:

```java
// A superclass that represents a person
class Person {
  // A private instance variable
  private String name;

  // A public constructor
  public Person(String name) {
    this.name = name;
  }

  // A public getter method
  public String getName() {
    return name;
  }

  // A public method that returns a string representation of the object
  public String toString() {
    return "Person[name=" + name + "]";
  }
}

// A subclass that represents a student, which inherits from Person
class Student extends Person {
  // A private instance variable
  private String major;

  // A public constructor that invokes the superclass constructor
  public Student(String name, String major) {
    super(name); // Call the Person constructor
    this.major = major;
  }

  // A public getter method
  public String getMajor() {
    return major;
  }

  // A public method that overrides the superclass method
  public String toString() {
    return "Student[name=" + getName() + ",major=" + major + "]"; // Use the inherited getName() method
  }
}

// A test class that creates and prints some objects
class Test {
  public static void main(String[] args) {
    // Create a Person object
    Person p = new Person("Alice");
    // Print the object
    System.out.println(p); // Invoke the toString() method
    // Output: Person[name=Alice]

    // Create a Student object
    Student s = new Student("Bob", "Computer Science");
    // Print the object
    System.out.println(s); // Invoke the toString() method
    // Output: Student[name=Bob,major=Computer Science]
  }
}
```

Here is a possible mnemonic to remember the concept of inheritance:

- Inheritance is like a family tree, where the children inherit the traits of their parents, and the parents inherit the traits of their grandparents, and so on.
- The superclass is like the parent, and the subclass is like the child.
- The `extends` keyword is like saying "is a", as in "a student is a person".
- The `super` keyword is like saying "from the parent", as in "a student gets the name from the parent".
- The `Object` class is like the ancestor of all classes, and provides some common traits for all classes.