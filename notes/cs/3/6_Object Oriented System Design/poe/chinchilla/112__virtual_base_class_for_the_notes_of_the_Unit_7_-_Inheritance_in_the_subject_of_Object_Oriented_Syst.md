### Virtual Base Class for the Notes of Unit 7 - Inheritance in Object Oriented System Design

In object-oriented programming, inheritance is a mechanism that allows us to create a new class based on an existing class. This concept of inheritance allows the derived class to inherit the properties and behavior of the base class. In some cases, we may need to derive a class from multiple base classes. This is where the concept of virtual base class comes into play.

A virtual base class is a special type of class that is used as a base class for multiple derived classes. When a class is derived from a virtual base class, it shares a single copy of the virtual base class with all its derived classes. This helps in avoiding the problem of multiple inheritance, where the derived class may end up with multiple copies of the inherited base class.

Here are some important points to keep in mind when using virtual base class in inheritance:

1. Virtual base class is declared by using the keyword "virtual" before the base class name in the derived class declaration.

2. A virtual base class must be initialized in the constructor of the most derived class.

3. The virtual base class constructor is called before the constructor of any non-virtual base class in the most derived class.

4. If a class is derived from multiple virtual base classes, then all the virtual base classes are initialized in the order they appear in the derivation list.

5. A virtual base class is not initialized if it is already initialized by a base class higher up in the inheritance hierarchy.

6. The use of virtual base class helps in resolving the diamond problem, which occurs when two base classes of a derived class share a common base class.

In summary, the use of virtual base class in inheritance is an important concept in object-oriented programming. It helps in avoiding the problem of multiple inheritance and resolves the diamond problem. Understanding the concept of virtual base class is essential for designing complex software systems using object-oriented programming principles.