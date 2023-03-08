 Here is the content in markdown format on the topic ### constructors and their types for the notes of the Unit 6 - Objects and Classes in the subject of Object Oriented System Design:

### Constructors

- Constructors are special methods that are used to initialize objects.
- They are called whenever a new object is created.
- Constructors have the same name as the class and they do not have a return type.
- The main purpose of constructors is to set the initial state of an object.

Types of Constructors:

- Default Constructor: This is a constructor without any parameters. It is automatically created by the compiler if there is no other constructor defined.
- Parametrized Constructor: This is a constructor with parameters (arguments). It is used to provide different values to the object upon creation.
- Copy Constructor: This is a constructor that creates an object by copying the values from another object of the same class. It is mainly used to perform a deep copy of objects.

Advantages of Using Constructors:

- They ensure that all objects are initialized properly.
- They can be used to overload objects with different states.
- They increase the readability of code.

Disadvantages of Using Constructors:

- If not implemented properly, they can lead to creation of inconsistent objects.
- Having many constructors can make the code complex and hard to maintain.

Examples of Constructors:

```java
class Student {
  String name;
  int age;
  
  // Default Constructor
  Student() {
    name = "Unknown";
    age = 0;
  }
  
  // Parametrized Constructor
  Student(String name, int age) {
    this.name = name;
    this.age = age;
  }
  
  // Copy Constructor
  Student(Student s) {
    this.name = s.name;
    this.age = s.age;
  }
}
```

Applications of Constructors:

- Constructors are commonly used to instantiate objects in a certain known state as required.
- They are useful in object serialization and cloning to create exact copies of objects.
- They are widely used in object-relational mapping (ORM) tools to map class states to database rows.