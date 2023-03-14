#### Inheritance in Scala

- Inheritance is an important pillar of OOP (Object Oriented Programming). It is the mechanism in Scala by which one class is allowed to inherit the features (fields and methods) of another class  .
- The keyword used for inheritance is `extends`. The syntax is:

```scala
class child_class_name extends parent_class_name {
  // Methods and fields
}
```

- Scala supports various types of inheritance, such as:
  - Single inheritance: A subclass inherits from only one superclass directly  .
  - Multilevel inheritance: A subclass inherits from a superclass, which in turn inherits from another superclass, and so on  .
  - Hierarchical inheritance: More than one subclass inherits from the same superclass .
  - Multiple inheritance: A subclass inherits from more than one superclass directly. This is not possible with classes, but only with traits .
  - Hybrid inheritance: A combination of two or more types of inheritance. This can also be achieved with traits .

- Inheritance allows us to reuse the code of the superclass and extend or override its functionality in the subclass.
- Inheritance also supports the concept of polymorphism, which means that a subclass object can be treated as a superclass object.