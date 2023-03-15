### Protected Members

In the context of Object Oriented System Design, inheritance is a mechanism that allows a class to inherit properties and methods from another class. In this process, the class that inherits is called the derived class, and the class that is inherited from is called the base class.

One of the key concepts in inheritance is the accessibility of members of the base class from the derived class. Members of a class can have different access specifiers, such as `public`, `private`, and `protected`.

- `Public` members are accessible from anywhere, including from outside the class and from derived classes.
- `Private` members are only accessible from within the class itself, and are not accessible from derived classes.
- `Protected` members are accessible from within the class itself and from derived classes, but not from outside the class.

In the context of inheritance, `protected` members provide a middle ground between `public` and `private` access. They allow derived classes to access and use the members of the base class, while still preventing access from outside the class.

Here are some key points to remember about `protected` members:

- `Protected` members are accessible from within the class itself and from derived classes.
- `Protected` members are not accessible from outside the class.
- `Protected` members provide a way for derived classes to access and use members of the base class, while still preventing access from outside the class.
- `Protected` members can be useful when you want to allow derived classes to access certain members of the base class, but you don't want those members to be accessible from outside the class.

In summary, `protected` members provide a way to control the accessibility of members of a class in the context of inheritance. They allow derived classes to access and use members of the base class, while still preventing access from outside the class. This can be useful when designing object-oriented systems.