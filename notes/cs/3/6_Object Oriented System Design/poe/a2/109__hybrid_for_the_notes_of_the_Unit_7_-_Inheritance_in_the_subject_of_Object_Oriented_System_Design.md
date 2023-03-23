 Here are the notes for Unit 7 - Inheritance in Object Oriented System Design:

### Inheritance

- Inheritance is a mechanism in which one class acquires the properties and behaviors of another class. The inheriting class is known as the subclass and the class it inherits from is known as the superclass.
- The benefits of inheritance are:
- It represents an is-a relationship. The subclass inherits from the superclass because it is a type of the superclass. For example, a Square is a Shape, so the Square class would inherit from the Shape class.
- It allows us to eliminate redundant code. The subclass can reuse methods and properties of the superclass, so we don't have to write the same code multiple times.
- It enables us to extend the functionality of a superclass. The subclass can override methods of the superclass and provide specialized implementations.
- The syntax for creating a subclass is:

class SubClass(SuperClass):
    [...]

- A subclass can access and modify the methods and properties of its superclass using the super() keyword.
- Inheritance supports polymorphism. The same method name can refer to different implementations in a superclass and subclass. The correct implementation is called based on the object type.
- Inheritance can be single-level (one superclass, one subclass) or multi-level (a chain of superclasses and subclasses).
- Python also supports multiple inheritance, where a subclass can inherit from multiple superclasses. However, this can lead to issues such as the diamond problem, so it should be used with caution.

The notes are written in markdown format without any emojis or external links as requested. The content is formal and written in points as study material for learning Object Oriented System Design. Please let me know if you would like me to clarify or expand on any of the points.