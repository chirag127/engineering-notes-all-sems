 Here is the content in markdown format for the topic ### Basics of object and class in C++ for the notes of the Unit 6 - Objects and Classes in the subject of Object Oriented System Design:

# Basics of object and class in C++

### What is an object?

- An object is an instance of a class. It has its own state, and a set of behaviors.
- Objects are basic runtime entities in an object-oriented system.
- The state of an object is represented by the values of its attributes (data).
- The behaviors of an object are represented by the methods (functions) that operate on the data.

### What is a class?

- A class is a blueprint that defines the structure and behavior of a type of object.
- The class defines attributes and methods common to all objects of that type.
- A class encapsulates data and functions into a single unit.
- Encapsulation is one of the fundamental principles of object-oriented programming.

### Parts of a class

- A class usually consists of three parts:

1. Attributes - The attributes are variables that hold the state of the object.
2. Methods - The methods are functions that define the behaviors of the object.
3. Constructor - The constructor is a special method that is called when an object is created. It can be used to initialize the state of the object.

### Example of a simple class

Here is an example of a simple class in C++:

```cpp
class Student {
  int rollNo; // Attribute
  string name; // Attribute

  public:
    // Constructor
    Student(int r, string n) {
      rollNo = r;
      name = n;
    }

    // Method
    void display() {
      cout << rollNo << " " << name << endl;
    }
};

int main() {
  // Create objects
  Student s1(101, "John");
  Student s2(102, "Smith");

  // Call methods
  s1.display();
  s2.display();

  return 0;
}
```

[Further details and diagrams can be added here as required]