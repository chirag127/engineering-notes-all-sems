### Destructors

In Object Oriented System Design, a destructor is a special member function that is called automatically when an object of a class is destroyed. It is used to release any resources that were allocated by the object during its lifetime.

#### Syntax of Destructor

The syntax of a destructor is similar to that of a constructor, but it is preceded by a tilde (~) symbol.

```
class ClassName {
   public:
      ClassName(); // constructor
      ~ClassName(); // destructor
};
```

#### How Destructors Work

When an object of a class is destroyed, the destructor is called automatically. The order of destruction is the reverse of the order of construction. That is, the destructor of the last object created is called first, and the destructor of the first object created is called last. This is known as the "reverse order of construction" rule.

#### Advantages of Destructors

- Destructors provide a way to automatically release resources that were allocated by an object.
- They simplify the code by eliminating the need to manually release resources.
- They ensure that resources are released even if an exception is thrown.

#### Disadvantages of Destructors

- Destructors can be difficult to write correctly because they must handle all possible scenarios.
- They can be a source of bugs if they are not written properly.

#### Example of Destructors

```
#include <iostream>
using namespace std;

class Example {
   public:
      Example(); // constructor
      ~Example(); // destructor
};

Example::Example() {
   cout << "Constructor called" << endl;
}

Example::~Example() {
   cout << "Destructor called" << endl;
}

int main() {
   Example obj; // create object
   return 0;
}
```

Output:
```
Constructor called
Destructor called
```

#### Applications of Destructors

- Destructors are used to release resources such as memory, file handles, and database connections.
- They are used in smart pointers to automatically release memory when it is no longer needed.

In summary, destructors are an important concept in Object Oriented System Design that provide a way to automatically release resources that were allocated by an object. They simplify the code and ensure that resources are released even if an exception is thrown.