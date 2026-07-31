### Virtual Base Class

- A virtual base class is a special type of base class that is used to avoid the **diamond problem** in multiple inheritance.
- The diamond problem occurs when a class inherits from two classes that have a common base class, resulting in two copies of the base class members in the derived class.
- To avoid this ambiguity, the common base class can be declared as virtual, which means that only one copy of its members will be inherited by the derived class.
- A virtual base class can be declared by using the keyword `virtual` before the base class name in the inheritance list.
- For example, consider the following class hierarchy:

```c++
class A {
public:
    int x;
};

class B : virtual public A {
public:
    int y;
};

class C : virtual public A {
public:
    int z;
};

class D : public B, public C {
public:
    int w;
};
```

- In this example, class A is a virtual base class for classes B and C, which are in turn base classes for class D.
- This means that class D will inherit only one copy of the member x from class A, and not two copies as in the case of non-virtual inheritance.
- To access the members of a virtual base class, the derived class can use the scope resolution operator (::) with the base class name, or use a pointer or reference to the base class type.
- For example, to access x from class D, we can write:

```c++
D d;
d.x = 10; // direct access
d.A::x = 10; // using scope resolution operator
A* p = &d; // using pointer to base class
p->x = 10;
A& r = d; // using reference to base class
r.x = 10;
```