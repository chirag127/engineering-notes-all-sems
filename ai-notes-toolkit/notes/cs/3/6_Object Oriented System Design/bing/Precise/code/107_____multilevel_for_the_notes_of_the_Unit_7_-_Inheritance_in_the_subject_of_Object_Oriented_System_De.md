### Multilevel Inheritance

Multilevel inheritance is a type of inheritance in Object Oriented System Design where a class inherits from a superclass, which in turn inherits from another superclass, forming a chain of inheritance. This is also known as a hierarchy of inheritance.

Here are some key points to remember about multilevel inheritance:

1. In multilevel inheritance, a subclass inherits from a superclass, which in turn inherits from another superclass.
2. The subclass inherits all the members (data members and member functions) of its superclass, as well as the members of the superclass's superclass.
3. The subclass can also add its own members, and can override the inherited members by providing its own implementation.
4. The constructors of the superclass and its superclass are called in the order of inheritance, from the topmost superclass to the bottommost subclass.
5. The destructors are called in the reverse order of inheritance, from the bottommost subclass to the topmost superclass.

Multilevel inheritance can be useful in situations where there is a natural hierarchy of classes, and where each level in the hierarchy adds additional functionality or data to the previous level. However, it can also make the code more complex and harder to understand, so it should be used judiciously.