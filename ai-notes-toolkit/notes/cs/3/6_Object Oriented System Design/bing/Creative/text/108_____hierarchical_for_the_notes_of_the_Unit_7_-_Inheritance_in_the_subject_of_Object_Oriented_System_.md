### Hierarchical Inheritance

- Hierarchical inheritance is a way of transmitting features from a parent class to multiple child classes in object-oriented programming languages .
- The parent class or superclass is the class from which the properties are taken, i.e. the features are inherited .
- The child classes or subclasses are the classes that inherit the properties of the parent class .
- In hierarchical inheritance, there is one base class and multiple derived classes.
- Several other classes can inherit the derived classes as well, forming a tree-like structure.
- In hierarchical inheritance, each child class can have its own unique features as well as the features of the parent class .
- In hierarchical inheritance, the inheritance hierarchy of an object is fixed at instantiation when the object's type is selected and does not change with time.
- For example, if there is a class Person that has attributes like name, age, and gender, and two classes Student and Employee that inherit from Person, then Student and Employee are child classes of Person, and Person is the parent class of Student and Employee. Student and Employee can have their own attributes like roll number, salary, etc. as well as the attributes of Person. A Student object cannot become an Employee object while retaining the state of its Person superclass.