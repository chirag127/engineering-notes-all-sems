### Virtual Base Class

A virtual base class is a class that is specified as a common base class for two or more classes in an inheritance hierarchy. It is used to solve the diamond problem that arises in multiple inheritance.

Here are some key points to remember about virtual base classes:

1. A virtual base class is specified using the `virtual` keyword in the inheritance list of a derived class.
2. The virtual base class is shared among all the classes that inherit from it.
3. The constructors of virtual base classes are called in the order in which they appear in the inheritance list.
4. The constructors of virtual base classes are called before the constructors of non-virtual base classes.
5. The virtual base class subobject is constructed only once, even if it is inherited by multiple classes in the hierarchy.
6. The virtual base class subobject is destroyed after all the derived class subobjects have been destroyed.

In summary, a virtual base class is used to prevent multiple copies of a base class subobject in an inheritance hierarchy. It is an important concept in object-oriented programming and is commonly used in C++ to solve the diamond problem in multiple inheritance.