### Protected Members

- Protected members are class members that have the access specifier `protected`.
- Protected members are accessible within the same class and its subclasses, but not outside the class.
- Protected members are useful for creating class members that are private to the class, but that can still be inherited and accessed by the derived classes.
- Protected members can be accessed by the derived classes in two ways:
  - Using the `this` pointer or the object of the same type as the derived class.
  - Using a friend class or a friend function of the derived class.
- Protected members can also be inherited by the derived classes in different ways, depending on the type of inheritance:
  - Public inheritance: The public and protected members of the base class are inherited as public and protected members of the derived class, respectively. The private members of the base class are inaccessible to the derived class.
  - Protected inheritance: The public and protected members of the base class are inherited as protected members of the derived class. The private members of the base class are inaccessible to the derived class.
  - Private inheritance: The public and protected members of the base class are inherited as private members of the derived class. The private members of the base class are inaccessible to the derived class.

- Here is an example of using protected members in inheritance:

```cpp
// A base class with a protected member
class Base {
protected:
  int x; // a protected member
public:
  Base(int a) : x(a) {} // a constructor to initialize x
  void show() {
    cout << "x = " << x << endl; // a public member function to access x
  }
};

// A derived class that inherits from Base
class Derived : public Base {
public:
  Derived(int b) : Base(b) {} // a constructor to initialize x using Base constructor
  void access() {
    x++; // a derived class member function that can access x
    show(); // a derived class member function that can access show()
  }
};

int main() {
  Derived d(10); // an object of derived class
  d.access(); // calling access() function
  return 0;
}
```

- The output of the above program is:

```
x = 11
```

- In the above program, the derived class `Derived` inherits from the base class `Base` using public inheritance. The protected member `x` of the base class is accessible to the derived class using the `this` pointer or the object of the same type as the derived class. The public member function `show()` of the base class is also accessible to the derived class. The derived class can also access the constructor of the base class using the member initializer list.