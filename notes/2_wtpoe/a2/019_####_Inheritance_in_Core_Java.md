 Here is the content in markdown format for #### Inheritance in Core Java:

#### Inheritance in Core Java

Inheritance is one of the fundamental concepts of Object Oriented Programming (OOP). It allows us to define a class that inherits all the methods and properties from another class.

**Parent Class (Super Class)**: The class whose features are inherited is known as parent class or super class.

**Child Class (Sub Class)**: The class that inherits the features from another class is known as child class or sub class.

**Advantages of Inheritance**:

- Code Reusability: We can reuse the code of parent class in the child class thus eliminating code duplication.
- Extension: We can extend the functionality of parent class by adding more attributes and methods in the child class.
- Polymorphism: Inheritance enables polymorphism thus making our program robust and efficient.

**Types of Inheritance**:

- Single Inheritance: A child class inherits from only one parent class.
- Multiple Inheritance: A child class inherits from multiple parent classes. (Not supported in Java)
- Hierarchical Inheritance: Multiple child classes inherit from one parent class.
- Multilevel Inheritance: A child class acts as the parent class for another child class.

**Is-A Relationship**: Inheritance reflects Is-A relationship. For example: Car Is-A Vehicle. Here Vehicle is super class and Car is sub class.

**Uses**: Inheritance can be used for representing real world relationships between classes where one class shares common characteristics with another class. It is useful for code reuse and building robust programs.

**Examples**:

- Vehicle -> Car (Car Is-A Vehicle)
- Animal -> Dog (Dog Is-A Animal)
- Employee -> Manager (Manager Is-A Employee)

**Mdmonics and Learning Tricks**:

- Think in terms of Is-A relationship to determine if inheritance can be used.
- The class inheriting the features is called child/sub class and the class whose features are inherited is called parent/super class.
- "extends" keyword is used to inherit features from parent class.
- "super" keyword is used to refer parent class constructor and methods.
- To override a method, use same method signature in child class.

I hope this helps! Let me know if you would like me to explain anything in more detail.