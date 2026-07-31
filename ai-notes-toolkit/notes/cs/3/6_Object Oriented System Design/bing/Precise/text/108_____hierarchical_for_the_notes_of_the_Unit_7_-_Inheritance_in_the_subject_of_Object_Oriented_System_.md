### Hierarchical Inheritance in Object Oriented System Design

- Hierarchical inheritance is a type of inheritance where multiple classes inherit from a single base class.
- This type of inheritance is used to represent a hierarchy of related classes, where the base class represents a common set of attributes and behaviors that are shared by all the derived classes.
- In hierarchical inheritance, the derived classes can add or override the attributes and behaviors of the base class to specialize their behavior.
- An example of hierarchical inheritance is a class hierarchy representing different types of vehicles, where the base class `Vehicle` represents common attributes and behaviors such as `make`, `model`, `year`, `speed`, and `drive()`, and the derived classes `Car`, `Truck`, and `Motorcycle` represent specialized types of vehicles with additional attributes and behaviors.
- Hierarchical inheritance can be implemented in object-oriented programming languages such as Java and C++ using the `extends` or `:` keyword, respectively.
- In hierarchical inheritance, the derived classes have access to the public and protected members of the base class, but not to its private members.
- Hierarchical inheritance can lead to code reuse and a more organized and maintainable codebase, as common attributes and behaviors are defined in the base class and shared by all the derived classes.