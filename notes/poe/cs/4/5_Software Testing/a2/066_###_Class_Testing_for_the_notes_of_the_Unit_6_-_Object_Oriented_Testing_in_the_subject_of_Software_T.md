 Here is the content in markdown format for the topic -

### Class Testing for the notes of the Unit 6 - Object Oriented Testing in the subject of Software Testing

Class testing involves testing individual classes of the software independently. The goal is to verify that each class meets its requirements and reveals faults as early as possible.

Some key points about Class Testing:

- Classes are tested independently without instantiating them.
- Setters and getters of class variables are tested.
- Boundary conditions are checked for methods.
- Internal data structures are checked for correctness.
- Inheritance is checked if the class is a subclass.
- Exception conditions are checked.

Advantages:

- Finds faults early thus reducing cascading effects.
- Improves modularity as classes are tested in isolation.
- Increases confidence in individual class functionality.

Disadvantages:

- May not find integration faults.
- Tedious to write test cases for each method.
- May be ignored if system testing is prioritized.

Examples of Class Testing:

- Testing a 'Transaction' class by calling debit and credit methods with various parameters and checking account balance.
- Testing a 'Database Connection' class by passing in various connection strings and credentials and checking if connection is established successfully.

In short, Class Testing ensures that each class is working as intended individually before integrating them and testing the system as a whole. This helps in early detection of faults and improves modularity. However, integration faults may be missed which can be handled in subsequent integration and system testing.