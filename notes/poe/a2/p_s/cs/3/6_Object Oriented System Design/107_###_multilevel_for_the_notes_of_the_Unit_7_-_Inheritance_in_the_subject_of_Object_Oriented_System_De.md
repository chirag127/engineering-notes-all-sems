 Here are the notes for Unit 7 - Inheritance in Object Oriented System Design:

### Multilevel Inheritance

- In multilevel inheritance, a derived class inherits from a base class that in turn inherits from another base class.
- It arranges the classes in a hierarchical order from general to specific.
- The derived class inherits the features of the intermediate base class and the topmost base class.
- For example:

```
class Person
{
    //...
}

class Employee : Person
{
    //...
}

class Manager : Employee
{
    //...
}
```

Here, `Manager` inherits from `Employee` which in turn inherits from `Person`. So, `Manager` gets the features of both `Employee` and `Person`.
- This is useful to model real-world relationships where one object is a specific type of another object which is in turn a specific type of a third object.
- The features of the topmost base class are available to the most derived class.
- However, it can make the code complex and hard to maintain if taken to an extreme level. So, multilevel inheritance should be used judiciously.

Advantages:
- Reusability of code. Derived classes can reuse the features of multiple base classes.
- Modelling real-world relationships.

Disadvantages:
- The code can become complex with too many levels of inheritance.
- It can be difficult to maintain or debug the code.

Applications:
- Modelling organizational hierarchies (employee -> manager -> CEO).
- Modelling biological classification (animal -> mammal -> dog).