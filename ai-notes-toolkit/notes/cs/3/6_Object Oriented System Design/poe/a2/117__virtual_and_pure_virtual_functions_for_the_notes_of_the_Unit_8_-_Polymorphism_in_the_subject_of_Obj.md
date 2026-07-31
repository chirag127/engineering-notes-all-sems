 Here are the notes on virtual and pure virtual functions for Unit 8 - Polymorphism in Object Oriented System Design:

### Virtual Functions

- Virtual functions are functions in base class that are redefined in derived class.
- They are declared using virtual keyword in base class.
- The derived class overrides the virtual function and provides its own implementation.
- This is called runtime polymorphism as the function to be called is decided at runtime based on the object type.
- They are mainly used to achieve runtime polymorphism.

### Pure Virtual Functions

- Pure virtual functions are virtual functions that have no implementation in base class.
- They are declared using = 0 after the function declaration.
- The derived class must override and provide implementation to pure virtual functions.
- Classes with pure virtual functions are called abstract classes and cannot be instantiated.
- They are useful to provide a common interface to derived classes and force them to provide implementation.

**Points to Remember:**

- Virtual functions can be overridden in derived class.
- Pure virtual functions have no implementation and must be overridden.
- Abstract classes cannot be instantiated and are used to provide common interface.
- Runtime polymorphism is achieved using virtual and pure virtual functions.

The notes are written in a formal tone with points and without any emojis or external links as per the given instructions. The content is written inside headers for the given topic using Markdown format. Please let me know if you would like me to modify or add any other points to the notes.