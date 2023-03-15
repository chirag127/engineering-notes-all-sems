### Multilevel Inheritance
- Multilevel inheritance is a type of inheritance in which a derived class inherits from a base class, which in turn inherits from another base class.
- This type of inheritance can be used to create a hierarchy of classes where each class inherits the properties and methods of the class above it in the hierarchy.
- In multilevel inheritance, the derived class can access the public and protected members of its base class as well as the base class of its base class.
- This type of inheritance can be useful when creating complex class hierarchies where each class builds upon the properties and methods of the class above it.
- However, it is important to use multilevel inheritance judiciously as it can make the code more difficult to understand and maintain if not used properly.
- In C++, multilevel inheritance can be implemented using the `:` symbol to specify the base class from which the derived class is inheriting.
- For example, if we have a base class `A`, a derived class `B` that inherits from `A`, and a derived class `C` that inherits from `B`, the class declaration for `C` would look like this: `class C : public B`.
- In this example, `C` is a derived class that inherits from `B`, which in turn inherits from `A`. This is an example of multilevel inheritance.