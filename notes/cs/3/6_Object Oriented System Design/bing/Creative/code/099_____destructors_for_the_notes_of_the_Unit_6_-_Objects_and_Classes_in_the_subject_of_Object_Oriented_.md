Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of destructors for the notes of the Unit 6 - Objects and Classes in the subject of Object Oriented System Design.

### Destructors

- A destructor is a special member function of a class that is executed whenever an object of that class goes out of scope or is explicitly destroyed by a call to `delete`.
- A destructor has the same name as the class, preceded by a tilde (`~`). For example, the destructor of the class `Student` is `~Student()`.
- A destructor takes no arguments and has no return type. It cannot be overloaded or inherited.
- The purpose of a destructor is to release any resources that the object has acquired during its lifetime, such as memory, files, sockets, etc.
- A destructor is automatically invoked by the compiler when the object is destroyed. The programmer does not need to call the destructor explicitly, unless using dynamic memory allocation with `new` and `delete`.
- A destructor can be defined either inside or outside the class definition, using the same syntax as a constructor. For example:

```cpp
// Destructor defined inside the class
class Student {
  private:
    int id;
    char* name;
  public:
    Student(int i, const char* n); // Constructor
    ~Student() { // Destructor
      delete[] name; // Release dynamic memory
      cout << "Student object destroyed." << endl;
    }
};

// Destructor defined outside the class
class Student {
  private:
    int id;
    char* name;
  public:
    Student(int i, const char* n); // Constructor
    ~Student(); // Destructor declaration
};

Student::~Student() { // Destructor definition
  delete[] name; // Release dynamic memory
  cout << "Student object destroyed." << endl;
}
```

- A destructor can also be declared as virtual, which means that it will be called according to the actual type of the object, not the declared type. This is useful when dealing with polymorphism and inheritance, where a base class pointer can point to a derived class object. For example:

```cpp
// Virtual destructor
class Shape {
  public:
    Shape() { cout << "Shape constructor." << endl; }
    virtual ~Shape() { cout << "Shape destructor." << endl; } // Virtual destructor
    virtual void draw() = 0; // Pure virtual function
};

class Circle : public Shape {
  private:
    int radius;
  public:
    Circle(int r) : radius(r) { cout << "Circle constructor." << endl; }
    ~Circle() { cout << "Circle destructor." << endl; } // Destructor
    void draw() { cout << "Drawing a circle." << endl; } // Override draw function
};

int main() {
  Shape* s = new Circle(10); // Base class pointer to derived class object
  s->draw(); // Polymorphic call
  delete s; // Delete the object
  return 0;
}

// Output:
// Shape constructor.
// Circle constructor.
// Drawing a circle.
// Circle destructor.
// Shape destructor.
```

- If the destructor of the base class is not declared as virtual, then only the base class destructor will be called, which may lead to memory leaks or undefined behavior. For example:

```cpp
// Non-virtual destructor
class Shape {
  public:
    Shape() { cout << "Shape constructor." << endl; }
    ~Shape() { cout << "Shape destructor." << endl; } // Non-virtual destructor
    virtual void draw() = 0; // Pure virtual function
};

class Circle : public Shape {
  private:
    int radius;
  public:
    Circle(int r) : radius(r) { cout << "Circle constructor." << endl; }
    ~Circle() { cout << "Circle destructor." << endl; } // Destructor
    void draw() { cout << "Drawing a circle." << endl; } // Override draw function
};

int main() {
  Shape* s = new Circle(10); // Base class pointer to derived class object
  s->draw(); // Polymorphic call
  delete s; // Delete the object
  return 0;
}

// Output:
// Shape constructor.
// Circle constructor.
// Drawing a circle.
// Shape destructor.
```

- Notice that the destructor of the derived class `Circle` is not called, which means that the memory allocated for the `radius` member is not released. This is a memory leak and can cause problems in the program. Therefore, it is a good practice to always declare the destructor of a base class as virtual,