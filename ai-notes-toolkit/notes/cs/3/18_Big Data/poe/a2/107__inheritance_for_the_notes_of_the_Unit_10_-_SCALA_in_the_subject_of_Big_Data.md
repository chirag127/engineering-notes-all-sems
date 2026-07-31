 Here is the content in markdown format without any emojis or external links and in formal tone with points:

### Inheritance

1. Inheritance is a mechanism in which one class acquires the properties and behaviors of another class.
2. The class that inherits the properties and behaviors is called the subclass or child class. The class that is inherited from is called the superclass or parent class.
3. Inheritance allows us to define a class that inherits all the methods and properties from another class. Parent class is the class being inherited from, also called base class. Child class is the class that inherits from another class, also called derived class.
4. Inheritance allows us to reuse the code from the parent class. We can also override the methods and properties inherited from the parent class. This makes our code more modular and easy to maintain.
5. In Scala, we use the extends keyword for inheritance. The general form is:
class Childclass extends Parentclass
6. A class can only extend one parent class. This is called single inheritance. However, a class can implement multiple traits. This allows us to achieve multiple inheritances of sorts in Scala.
7. A parent class can be generalized to inherit from a more generic superclass, creating a hierarchy of inheritance. This makes the software more flexible and re-usable.
8. Protected members of a superclass are accessible from subclasses, but not outside the class hierarchy. Private members are not accessible by the subclasses at all.
9. Overriding methods allows a subclass to provide its own implementation of a method that it has inherited. The overridden method in the subclass has the same name and signature as the method in the superclass. Use override keyword to override a method.
10. Use super keyword to refer to the superclass and call its methods and properties. This is useful when extending a class but also wanting to reuse some of the functionality of the parent class.