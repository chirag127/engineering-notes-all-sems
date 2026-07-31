### Constructors and their types

- A constructor is a special method that is used to initialize an object of a class.
- A constructor has the same name as the class and does not have a return type.
- A constructor is invoked automatically when an object of the class is created using the `new` operator.
- A constructor can perform tasks such as setting the initial values of the object's attributes, allocating memory for the object, or calling other methods of the class or its superclass.
- There are two types of constructors: parameterized and default.

#### Parameterized constructors

- A parameterized constructor is a constructor that takes one or more parameters as input.
- A parameterized constructor can be used to assign different values to the object's attributes based on the input parameters.
- A parameterized constructor can also be used to invoke another constructor of the same class or its superclass using the `this` or `super` keywords.
- A parameterized constructor can be overloaded, which means that a class can have more than one parameterized constructor with different parameter lists.
- A parameterized constructor can be defined as follows:

```java
// A parameterized constructor of the class Student
public Student(String name, int age, double marks) {
  // Assign the input parameters to the object's attributes
  this.name = name;
  this.age = age;
  this.marks = marks;
  // Call another constructor of the same class
  this("Unknown", 0, 0.0);
  // Call a constructor of the superclass
  super(name, age);
}
```

#### Default constructors

- A default constructor is a constructor that does not take any parameters as input.
- A default constructor can be used to assign default values to the object's attributes, such as `null`, `0`, or `false`.
- A default constructor can also be used to invoke another constructor of the same class or its superclass using the `this` or `super` keywords.
- A default constructor is implicitly provided by the compiler if no other constructor is defined in the class.
- A default constructor can be defined as follows:

```java
// A default constructor of the class Student
public Student() {
  // Assign default values to the object's attributes
  this.name = null;
  this.age = 0;
  this.marks = 0.0;
  // Call another constructor of the same class
  this("Unknown", 0, 0.0);
  // Call a constructor of the superclass
  super();
}
```