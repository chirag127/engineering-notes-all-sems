# Implementing inheritance for the notes of the Unit 3 - Object Oriented Analysis in the subject of Object Oriented System Design

- Inheritance is the mechanism of basing an object or class upon another object or class, retaining similar implementation.
- Inheritance enables you to create new classes that reuse, extend, and modify the behavior defined in other classes.
- The class whose members are inherited is called the base class, and the class that inherits those members is called the derived class.
- Inheritance provides code re-usability, as you can avoid writing the same code, again and again, by inheriting the properties of one class into the other.
- Inheritance also supports the concept of polymorphism, which allows you to use a derived class object as if it were a base class object.
- To implement inheritance in object oriented analysis, you need to follow these steps:
  - Identify the common attributes and methods of the classes that you want to model.
  - Create a base class that contains these common attributes and methods, and make it abstract if it does not have a concrete implementation.
  - Create derived classes that inherit from the base class and add their own specific attributes and methods.
  - Use the keyword `extends` in Java or `:` in C++ to indicate the inheritance relationship between the classes.
  - Use the keyword `super` in Java or the base class name in C++ to access the members of the base class from the derived class.
  - Use the keyword `override` in Java or `virtual` in C++ to indicate that a method in the derived class is redefining the behavior of a method in the base class.
  - Use the keyword `final` in Java or `const` in C++ to indicate that a method or a class cannot be overridden or inherited further.
- Here is an example of implementing inheritance in Java:

```java
// A base class that represents a person
abstract class Person {
  // A common attribute of all persons
  protected String name;

  // A constructor that initializes the name
  public Person(String name) {
    this.name = name;
  }

  // A common method of all persons
  public String getName() {
    return name;
  }

  // An abstract method that must be implemented by the derived classes
  public abstract String getOccupation();
}

// A derived class that represents a student
class Student extends Person {
  // A specific attribute of a student
  private String major;

  // A constructor that initializes the name and the major
  public Student(String name, String major) {
    // Calling the base class constructor
    super(name);
    this.major = major;
  }

  // A specific method of a student
  public String getMajor() {
    return major;
  }

  // Overriding the abstract method of the base class
  @Override
  public String getOccupation() {
    return "Student";
  }
}

// A derived class that represents an employee
class Employee extends Person {
  // A specific attribute of an employee
  private double salary;

  // A constructor that initializes the name and the salary
  public Employee(String name, double salary) {
    // Calling the base class constructor
    super(name);
    this.salary = salary;
  }

  // A specific method of an employee
  public double getSalary() {
    return salary;
  }

  // Overriding the abstract method of the base class
  @Override
  public String getOccupation() {
    return "Employee";
  }
}

// A test class that creates and uses objects of the derived classes
class Test {
  public static void main(String[] args) {
    // Creating a student object
    Student s = new Student("Alice", "Computer Science");
    // Calling the methods of the student object
    System.out.println(s.getName()); // Alice
    System.out.println(s.getMajor()); // Computer Science
    System.out.println(s.getOccupation()); // Student

    // Creating an employee object
    Employee e = new Employee("Bob", 50000);
    // Calling the methods of the employee object
    System.out.println(e.getName()); // Bob
    System.out.println(e.getSalary()); // 50000.0
    System.out.println(e.getOccupation()); // Employee

    // Using polymorphism to treat a student object as a person object
    Person p = s;
    // Calling the methods of the person object
    System.out.println(p.getName()); // Alice
    // System.out.println(p