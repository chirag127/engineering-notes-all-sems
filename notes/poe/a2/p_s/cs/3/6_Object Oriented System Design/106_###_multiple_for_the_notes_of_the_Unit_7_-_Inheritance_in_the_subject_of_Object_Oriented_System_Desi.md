 Here are the notes for Unit 7 - Inheritance in Object Oriented System Design:

### Inheritance

Inheritance is a key feature of Object Oriented Programming. It allows a class to inherit the properties and methods of another class. The class that inherits is called a subclass and the class being inherited from is called a superclass.

**Benefits of Inheritance:**

- Reusability of code: The subclass can reuse the methods and properties defined in the superclass, so you don't have to write the same code again.
- Maintainability: If there is a change in the superclass, the subclass will automatically inherit it. So, you only need to make changes in one place.
- Modeling real world relationships: Inheritance models "is a" relationship. For example, a Dog "is a" Animal. So the Dog class can inherit from the Animal class.

**Types of Inheritance:**

- Single Inheritance: A subclass inherits from only one superclass.
- Multiple Inheritance: A subclass inherits from multiple superclasses. This is not supported in Java due to ambiguity.
- Multilevel Inheritance: A subclass inherits from another subclass. This can extend to multiple levels.
- Hierarchical Inheritance: Multiple subclasses inherit from the same superclass.

**Access Modifiers with Inheritance:**

- Public: Members are accessible from anywhere.
- Protected: Members are only accessible within the class and subclasses.
- (No modifier): Members are only accessible within the package.
- Private: Members are only accessible within the class. Private members are not inherited by subclasses.

**Overriding and Overloading:**

- Overriding: A subclass can redefine a method of the superclass. This is called overriding and is done so that a subclass can give its own implementation to the method.
- Overloading: A class can have multiple methods with the same name but different parameters. This is called overloading and is used to provide alternate implementations of a method. Overloading and overriding are distinct concepts.