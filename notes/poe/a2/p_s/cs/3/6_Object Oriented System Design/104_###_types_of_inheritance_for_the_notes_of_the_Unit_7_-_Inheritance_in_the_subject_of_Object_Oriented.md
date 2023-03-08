 Here is the content in markdown format for the topic ### types of inheritance for the notes of the Unit 7 - Inheritance in the subject of Object Oriented System Design:

### Types of Inheritance

Following are the major types of inheritance:

1. Single Inheritance: When a derived class inherits from only one base class, it is called single inheritance. In this type of inheritance, a derived class can inherit only one base class.
Example:

```
class Animal {
   // ...
};

class Dog extends Animal {
   // ...
};
```

Here, the Dog class inherits from the Animal class. This is an example of single inheritance.

Advantages:
- Simple and Easy to understand.
- Does not produce ambiguity.

Disadvantages:
- If the derived class needs to inherit features from multiple classes, then single inheritance is not useful.

2. Multiple Inheritance: When a derived class inherits from two or more base classes, it is called multiple inheritance. In this type of inheritance, a derived class can have more than one base class.
Example:

```
class Animal {
   // ...
};

class Bird {
   // ...
};

class Sparrow extends Animal, Bird {
   // ...
};
```

Here, the Sparrow class inherits from both the Animal and Bird classes. This is an example of multiple inheritance.

Advantages:
- Derived class can inherit features from multiple base classes.

Disadvantages:
- Produces ambiguity if features of the base classes contradict each other.
- Difficult to understand and implement.
- Not supported in many OOP languages like Java and C#.

[Other types of inheritance and more details and examples can be added here]