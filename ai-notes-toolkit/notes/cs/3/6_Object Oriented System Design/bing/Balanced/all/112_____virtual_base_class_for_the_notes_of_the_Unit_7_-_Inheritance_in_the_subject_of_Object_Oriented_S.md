# Virtual Base Class

- A virtual base class is a special kind of base class that is used to avoid the **diamond problem** in multiple inheritance.
- The diamond problem occurs when a class inherits from two classes that have a common base class, resulting in two copies of the base class's members in the derived class.
- To avoid this problem, the common base class can be declared as virtual, which means that only one copy of its members will be inherited by the derived class.
- To declare a base class as virtual, the keyword `virtual` is used before the base class name in the derived class declaration.
- For example, consider the following classes:

```c++
// A common base class
class A {
public:
    int x;
};

// Two classes that inherit from A
class B: public A {
public:
    int y;
};

class C: public A {
public:
    int z;
};

// A class that inherits from B and C
class D: public B, public C {
public:
    int w;
};
```

- In this case, the class D will have two copies of the member x, one from B and one from C, which can cause ambiguity and inconsistency.
- To solve this problem, the class A can be declared as virtual in the classes B and C, as follows:

```c++
// A common base class
class A {
public:
    int x;
};

// Two classes that inherit from A virtually
class B: virtual public A {
public:
    int y;
};

class C: virtual public A {
public:
    int z;
};

// A class that inherits from B and C
class D: public B, public C {
public:
    int w;
};
```

- Now, the class D will have only one copy of the member x, which will be shared by B and C.
- To access the members of a virtual base class, the derived class can use the scope resolution operator (::) with the base class name, or use a pointer or a reference to the base class.
- For example, to access the member x of A in D, the following syntax can be used:

```c++
D d;
d.A::x = 10; // using scope resolution operator
A* p = &d; // using a pointer to A
p->x = 10;
A& r = d; // using a reference to A
r.x = 10;
```

- A virtual base class is initialized by the most derived class in the inheritance hierarchy, not by the intermediate classes.
- This means that the constructor of the virtual base class must be called explicitly by the constructor of the most derived class, using the member initializer list.
- For example, to initialize the member x of A in D, the following syntax can be used:

```c++
// Constructor of A
A(int a) {
    x = a;
}

// Constructor of D
D(int a, int b, int c, int d): A(a), B(b), C(c) {
    w = d;
}
```

- Note that the constructor of A is called by the constructor of D, not by the constructors of B and C.
- This ensures that the member x of A is initialized only once by the most derived class.
- A virtual base class can also have virtual functions, which can be overridden by the derived classes.
- This allows for dynamic polymorphism, where the appropriate function is called based on the type of the object at run time.
- For example, consider the following classes:

```c++
// A virtual base class with a virtual function
class A {
public:
    virtual void show() {
        cout << "A\n";
    }
};

// Two classes that inherit from A virtually and override the virtual function
class B: virtual public A {
public:
    void show() override {
        cout << "B\n";
    }
};

class C: virtual public A {
public:
    void show() override {
        cout << "C\n";
    }
};

// A class that inherits from B and C and overrides the virtual function
class D: public B, public C {
public:
    void show() override {
        cout << "D\n";
    }
};
```

- In this case, the virtual function show() of A can be overridden by the derived classes B, C, and D.
- To call the appropriate function based on