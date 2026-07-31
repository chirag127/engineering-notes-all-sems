### Unit 7 - Inheritance in Object Oriented System Design

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows the creation of hierarchical classifications. It is a mechanism by which one class acquires the properties and behaviors of another class. Here are some key points to remember about inheritance:

1. Inheritance allows the reuse of code by allowing a new class to inherit the properties and methods of an existing class.
2. The class that is being inherited from is called the base class or superclass, while the class that is inheriting is called the derived class or subclass.
3. Inheritance is transitive, meaning that if class B inherits from class A, and class C inherits from class B, then class C also inherits the properties and methods of class A.
4. Inheritance can be used to model "is-a" relationships between classes. For example, if we have a class `Animal` and a class `Dog`, we can say that a `Dog` is an `Animal` and have the `Dog` class inherit from the `Animal` class.
5. Inheritance allows for the creation of more specific classes based on a general class. For example, we can create a `Mammal` class that inherits from the `Animal` class and then create specific classes such as `Dog` and `Cat` that inherit from the `Mammal` class.
6. Inheritance can also be used to add or override methods in the derived class. This allows for the creation of specialized behavior in the derived class while still reusing code from the base class.
7. Inheritance should be used judiciously and not overused. It is important to carefully design the class hierarchy to ensure that inheritance is used appropriately and does not result in overly complex or rigid class structures.