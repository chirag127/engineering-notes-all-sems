### Protected Members

Protected members are a feature of Object Oriented System Design that allows for more flexible and secure access control within a class hierarchy. Protected members are accessible within the class in which they are declared, as well as within any derived classes. This means that protected members can be accessed by member functions of the class, as well as by member functions of any classes that inherit from the class.

Here are some key points to remember about protected members:

- Protected members are declared using the `protected` keyword.
- Protected members are accessible within the class in which they are declared, as well as within any derived classes.
- Protected members are not accessible outside of the class hierarchy, even if an object of the class is used.
- Protected members provide a way to share data and functionality between related classes, while still maintaining some level of encapsulation.

In summary, protected members provide a middle ground between public and private access, allowing for more flexible and secure access control within a class hierarchy. They are an important tool in the design of object-oriented systems.