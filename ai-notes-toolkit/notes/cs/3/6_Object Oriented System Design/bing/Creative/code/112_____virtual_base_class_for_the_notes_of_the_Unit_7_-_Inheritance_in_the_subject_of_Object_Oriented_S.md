### Virtual base class

A virtual base class is a special kind of base class that is used to avoid the duplication of data members in multiple inheritance. A virtual base class is declared by using the `virtual` keyword in the inheritance list of the derived class. For example:

```cpp
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

In this example, class `A` is a virtual base class for classes `B` and `C`, and class `D` inherits from both `B` and `C`. Without the `virtual` keyword, class `D` would have two copies of the data member `x` inherited from `A`, one through `B` and one through `C`. This would cause ambiguity and waste of memory. With the `virtual` keyword, class `D` has only one copy of the data member `x` inherited from `A`, which is shared by both `B` and `C`. This avoids the ambiguity and saves memory.

Some important points about virtual base classes are:

- A virtual base class is initialized by the most derived class in the inheritance hierarchy, not by the intermediate classes. For example, in the above example, class `D` is responsible for initializing class `A`, not classes `B` and `C`.
- A virtual base class can be accessed by using the scope resolution operator (`::`) with the class name. For example, in the above example, class `D` can access the data member `x` of class `A` by using `A::x`.
- A virtual base class can have constructors and destructors, but they are called only once by the most derived class in the inheritance hierarchy, not by the intermediate classes. For example, in the above example, if class `A` has a constructor and a destructor, they are called only by class `D`, not by classes `B` and `C`.
- A virtual base class can have virtual functions, but they are overridden by the most derived class in the inheritance hierarchy, not by the intermediate classes. For example, in the above example, if class `A` has a virtual function `f()`, and classes `B`, `C`, and `D` override it, then the version of `f()` defined by class `D` is called by any object of class `D`, not by the versions defined by classes `B` and `C`.
- A virtual base class can be abstract, but it cannot be instantiated directly. It can only be instantiated through a derived class that implements all the pure virtual functions of the virtual base class. For example, in the above example, if class `A` has a pure virtual function `g()`, then class `A` is abstract and cannot be instantiated directly. It can only be instantiated through class `D`, which must implement the function `g()`.