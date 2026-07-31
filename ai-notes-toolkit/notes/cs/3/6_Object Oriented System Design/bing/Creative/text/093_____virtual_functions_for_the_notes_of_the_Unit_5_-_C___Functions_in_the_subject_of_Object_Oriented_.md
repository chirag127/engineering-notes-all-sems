### Virtual Functions in C++

- A virtual function is a member function of a class that can be overridden in a derived class using the `virtual` keyword  .
- Virtual functions are used to achieve runtime polymorphism or dynamic binding, which means the function call is resolved at runtime based on the type of the object pointed by the base class pointer   .
- Virtual functions ensure that the correct function is called for an object, regardless of the type of reference (or pointer) used to access it .
- The syntax of declaring a virtual function is:

```cpp
class Base {
    public:
    virtual void print() {
        // some code
    }
};
```

- The `virtual` keyword is only required in the base class declaration. The derived class can use the `override` keyword to explicitly indicate that the function is overriding a virtual function from the base class .
- The syntax of overriding a virtual function is:

```cpp
class Derived : public Base {
    public:
    void print() override {
        // some code
    }
};
```

- A virtual function can be pure virtual, which means it has no definition in the base class and must be overridden in the derived class. A pure virtual function is declared with `= 0` after the function prototype   .
- The syntax of declaring a pure virtual function is:

```cpp
class Base {
    public:
    virtual void print() = 0; // pure virtual function
};
```

- A class that contains at least one pure virtual function is called an abstract class. An abstract class cannot be instantiated, but it can have pointers and references   .
- The syntax of creating a pointer or reference to an abstract class is:

```cpp
Base *ptr; // pointer to an abstract class
Base &ref; // reference to an abstract class
```

- A virtual function can also be called using the scope resolution operator `::` with the class name. This is useful to avoid the virtual function mechanism and call a specific version of the function   .
- The syntax of calling a virtual function using the scope resolution operator is:

```cpp
ptr->Base::print(); // calls the print function of the Base class
ptr->Derived::print(); // calls the print function of the Derived class
```

- A virtual function can also be inherited from another base class. In this case, the derived class must override the virtual function or declare it as pure virtual again   .
- The syntax of inheriting a virtual function from another base class is:

```cpp
class Base1 {
    public:
    virtual void print() {
        // some code
    }
};

class Base2 : public Base1 {
    public:
    void print() override {
        // some code
    }
};

class Derived : public Base2 {
    public:
    void print() override {
        // some code
    }
};
```

- A virtual function can also be a constructor or a destructor. However, a constructor cannot be virtual because it is invoked before the object is created. A destructor can be virtual to ensure that the correct destructor is called when deleting a pointer to a base class object   .
- The syntax of declaring a virtual destructor is:

```cpp
class Base {
    public:
    virtual ~Base() {
        // some code
    }
};
```

- A virtual function can also be a friend function of a class. However, a friend function cannot be virtual because it is not a member function of the class. A friend function can access the private and protected members of the class, but it cannot be overridden in the derived class   .
- The syntax of declaring a friend function is:

```cpp
class Base {
    friend void print(Base &obj); // friend function declaration
};

void print(Base &obj) {
    // some code
}
```