### Virtual Base Class

- A virtual base class is a special kind of base class that is used to avoid the **diamond problem** in multiple inheritance.
- The diamond problem occurs when a class inherits from two classes that have a common base class, resulting in two copies of the base class's members in the derived class.
- To avoid this problem, the common base class can be declared as virtual, which means that only one copy of its members will be inherited by the derived class.
- To declare a base class as virtual, the keyword `virtual` is used before the base class name in the derived class declaration.
- For example, consider the following class hierarchy:

```
    A
   / \
  B   C
   \ /
    D
```

- Here, class D inherits from both B and C, which in turn inherit from A. If A is not a virtual base class, then D will have two copies of A's members, which can cause ambiguity and inconsistency.
- To make A a virtual base class, the derived classes B and C should declare it as follows:

```cpp
class B : virtual public A {...};
class C : virtual public A {...};
```

- Now, class D will inherit only one copy of A's members, and the diamond problem is avoided.
- Some important points to remember about virtual base classes are:

  - The constructor of a virtual base class is always called by the most derived class, not by the intermediate classes.
  - The order of constructor invocation for virtual base classes is from left to right in the inheritance list.
  - The order of destructor invocation for virtual base classes is the reverse of the constructor invocation order.
  - A virtual base class cannot be abstract, i.e., it cannot have any pure virtual functions.
  - A virtual base class cannot be a friend of another class.