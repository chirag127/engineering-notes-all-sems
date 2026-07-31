# Virtual Base Class

A virtual base class is a special type of base class that is used in multiple inheritance to avoid the duplication of the same base class in the derived class. A virtual base class is declared by using the keyword `virtual` in the inheritance list of the derived class. For example:

```cpp
class A {}; // base class
class B : virtual public A {}; // derived class with virtual base class A
class C : virtual public A {}; // derived class with virtual base class A
class D : public B, public C {}; // derived class with two base classes B and C
```

In this example, class A is a virtual base class for both class B and class C. This means that there is only one instance of class A in the memory when an object of class D is created. This avoids the ambiguity and duplication of class A in class D.

Some important points about virtual base classes are:

- A virtual base class is initialized by the most derived class in the inheritance hierarchy. For example, in the above example, class D is responsible for initializing class A.
- A virtual base class can have constructors and destructors, but they are called only once by the most derived class.
- A virtual base class can have data members and member functions, but they are shared by all the derived classes that inherit from it.
- A virtual base class can have virtual functions, but they are overridden by the most derived class that defines them.
- A virtual base class can have pure virtual functions, but they must be defined by the most derived class that inherits from it.