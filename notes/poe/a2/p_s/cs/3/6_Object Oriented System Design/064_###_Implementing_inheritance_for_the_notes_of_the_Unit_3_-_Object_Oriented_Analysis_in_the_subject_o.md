 Here is the content in Markdown format:

### Implementing inheritance for the notes of the Unit 3 - Object Oriented Analysis in the subject of Object Oriented System Design:

1. Inheritance is a mechanism in which one class acquires the properties and behaviors of another class. 
The class that inherits the properties of another class is called the child or sub class and the class that allows inheritance is called the parent or super class.
2. To implement inheritance between two classes:
- Declare that the child class will inherit from the parent class by using the extends keyword. For example:
class ChildClass extends ParentClass {
    // child class contents
}
- The child class will inherit all the public and protected properties and methods of the parent class.
- The child class can also override the methods of the parent class by redefining them. The overridden methods in the child class can extend the behavior of the methods in the parent class.
3. Benefits of Inheritance:
- Code reusability - The child class can reuse and share the code of the parent class, reducing redundancy.
- Provides abstraction - The child class can inherit the abstraction of the parent class and further refine it as required.
- Allows modeling relationships - The `is-a` relationship between classes can be implemented using inheritance. The child class `is-a` type of the parent class.
4. Disadvantages of Inheritance:
- Tight coupling - The child class is tightly coupled with the parent class. Changes in the parent class can affect the child class.
- Limited Extensibility - There are possibilities of overuse of inheritance leading to complex hierarchies that are hard to maintain.
- Fragile base class problem - If the parent class is changed, all the subclasses may break. It is hard to predict the consequences of changes to the parent class.

[Detailed ASCII diagrams, codes, examples, etc. can be added here if required.]