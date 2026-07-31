 Here is the formal content on Inheritance in Core Java in markdown format without any emojis or external links:

#### Inheritance in Core Java

1. Inheritance is an important concept in Object Oriented Programming (OOP). It allows a class to inherit the properties and methods of another class.
2. The class that inherits the properties of another class is called a subclass or child class. The class whose properties are inherited is called a superclass or parent class.
3. Inheritance allows code reusability. The subclass can reuse the code of the superclass, so you don't have to write the same code again.
4. To inherit a class, use the extends keyword. For example, class Bike extends Vehicle {}. Here Bike is the subclass and Vehicle is the superclass.
5. A subclass can have its own methods and properties in addition to the inherited ones. This is called overriding. The subclass can override methods of the superclass if needed.
6. A subclass can be extended further to form a hierarchy of inheriting classes. This is called a class hierarchy. The hierarchy can go up to multiple levels but should not be too deep.
7. The Object class is the root class of all classes in Java. So, ultimately, every class inherits from the Object class.
8. To refer to a superclass constructor, use the super keyword. This is necessary when the subclass constructor needs to call the superclass constructor.
9. An interface can also be extended using the extends keyword. A class can implement multiple interfaces but can extend only one class.
10. Inheritance represents an "is-a" relationship. The subclass "is-a" type of the superclass. For example, a Bike "is-a" Vehicle. Inheritance should only be used if this relationship is true.