### Implementing inheritance for the notes of the Unit 3 - Object Oriented Analysis in the subject of Object Oriented System Design

- Inheritance is the mechanism of basing an object or class upon another object or class, retaining similar implementation .
- Inheritance enables you to create new classes that reuse, extend, and modify the behavior defined in other classes.
- Inheritance is one of the three primary characteristics of object-oriented programming, together with encapsulation and polymorphism.
- Inheritance provides code re-usability, as you can inherit the properties and methods of one class into another class, instead of writing the same code again and again.
- Inheritance also supports the concept of hierarchical classification, as you can form a hierarchy of classes that share some common attributes and behaviors.
- To implement inheritance, you need to define a base class (also called a super class or a parent class) that contains the common attributes and methods for the derived classes (also called subclasses or child classes) to inherit .
- The syntax for defining a subclass that inherits from a base class varies depending on the programming language, but usually involves a keyword such as `extends`, `inherits`, or `:` .
- For example, in Java, you can define a subclass `Dog` that inherits from a base class `Animal` as follows:

```java
class Animal {
  // attributes and methods of the animal class
}

class Dog extends Animal {
  // attributes and methods of the dog class
  // can reuse, extend, or override the attributes and methods of the animal class
}
```

- Inheritance can be single, multiple, or multilevel, depending on how many base classes or levels of hierarchy are involved .
- Single inheritance is when a subclass inherits from only one base class .
- Multiple inheritance is when a subclass inherits from more than one base class .
- Multilevel inheritance is when a subclass inherits from a base class that itself inherits from another base class, forming a chain of inheritance .
- For example, in C++, you can define a subclass `Poodle` that inherits from two base classes `Dog` and `Pet` as follows:

```cpp
class Animal {
  // attributes and methods of the animal class
};

class Dog : public Animal {
  // attributes and methods of the dog class
  // can reuse, extend, or override the attributes and methods of the animal class
};

class Pet {
  // attributes and methods of the pet class
};

class Poodle : public Dog, public Pet {
  // attributes and methods of the poodle class
  // can reuse, extend, or override the attributes and methods of the dog and pet classes
};
```

- Inheritance is a powerful tool for modeling the real-world entities and relationships in an object-oriented system .
- Inheritance can help you to achieve abstraction, modularity, and code reuse in your system design .
- However, inheritance also has some drawbacks, such as increased complexity, tight coupling, and fragile base class problem.
- Therefore, you should use inheritance wisely and follow the principles of good object-oriented design, such as favoring composition over inheritance, using interfaces instead of abstract classes, and applying the Liskov substitution principle.