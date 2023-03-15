### Virtual Base Class

- A virtual base class is a special kind of base class that is used to avoid the **diamond problem** in multiple inheritance.
- The diamond problem occurs when a class inherits from two classes that have a common base class, resulting in two copies of the base class members in the derived class.
- To avoid this ambiguity, the common base class can be declared as virtual, which means that only one copy of its members will be inherited by the derived class.
- A virtual base class can be declared by using the keyword `virtual` before the base class name in the inheritance list.
- For example, consider the following class hierarchy:

```
    A
   / \
  B   C
   \ /
    D
```

- Here, class `A` is the common base class for classes `B` and `C`, and class `D` inherits from both `B` and `C`.
- If `A` is not declared as virtual, then `D` will have two copies of `A`'s members, which can cause confusion and errors.
- To avoid this, `A` can be declared as virtual in the inheritance list of `B` and `C`, as follows:

```
class A {
  // members of A
};

class B : virtual public A {
  // members of B
};

class C : virtual public A {
  // members of C
};

class D : public B, public C {
  // members of D
};
```

- Now, `D` will have only one copy of `A`'s members, and the diamond problem is solved.
- Some important points to remember about virtual base classes are:

  - A virtual base class is initialized by the most derived class in the inheritance hierarchy, not by its immediate base classes.
  - A virtual base class cannot be abstract, meaning it cannot have any pure virtual functions.
  - A virtual base class cannot be accessed directly by the derived class using the scope resolution operator (`::`), but only through a pointer or a reference.