#### Inheritance in Core Java

Inheritance is one of the key concepts in object-oriented programming that allows new classes to be based on existing classes. In Java, it is the mechanism by which one class acquires the properties (methods and fields) of another class. The class that is being inherited from is called the superclass, while the class that is inheriting is called the subclass.

Inheritance is represented by the "extends" keyword in Java. A subclass can inherit all the fields and methods of its superclass, including the public, private, and protected members. The subclass can also add new members and override the methods of the superclass. 

#### Types of Inheritance in Java

Java supports five types of inheritance, which are as follows:

1. Single Inheritance: In this type of inheritance, a subclass extends only one superclass. It is the simplest type of inheritance.

2. Multilevel Inheritance: In this type of inheritance, a subclass inherits from a superclass, which in turn inherits from another superclass.

3. Hierarchical Inheritance: In this type of inheritance, multiple subclasses inherit from a single superclass.

4. Multiple Inheritance: In this type of inheritance, a subclass can inherit from multiple superclasses. However, Java doesn't support multiple inheritance directly. Instead, it provides a way to achieve multiple inheritance through interfaces.

5. Hybrid Inheritance: It is a combination of two or more types of inheritance.

#### Advantages of Inheritance in Java

1. Code Reusability: Inheritance promotes code reuse as the subclass can inherit the properties of its superclass, including the methods and fields.

2. Code Organization: Inheritance allows the code to be organized in a hierarchical manner, making it easier to manage and understand.

3. Polymorphism: Inheritance enables polymorphism, which allows objects to take on different forms, depending on the context.

#### Disadvantages of Inheritance in Java

1. Tight Coupling: Inheritance can lead to tight coupling between the superclass and subclass, making it difficult to modify the superclass without affecting the subclass.

2. Inheritance Hierarchy: Inheritance can lead to a complex hierarchy of classes, making it difficult to understand and maintain.

#### Mnemonic/Learning Trick for Inheritance in Java

One useful mnemonic for understanding inheritance in Java is "IS-A" relationship. The subclass "IS-A" type of the superclass. For example, a Car "IS-A" Vehicle, a Dog "IS-A" Animal, and so on. This way, it becomes easier to understand the relationship between the superclass and subclass.