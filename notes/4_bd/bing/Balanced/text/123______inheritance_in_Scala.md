#### Inheritance in Scala

- Inheritance is a mechanism that allows a class to inherit the features and behavior of another class.
- The class that inherits is called the **subclass** or the **derived class**.
- The class that is inherited is called the **superclass** or the **base class**.
- In Scala, inheritance is achieved by using the `extends` keyword.
- A subclass can override the methods and fields of the superclass by using the `override` keyword.
- A subclass can also access the methods and fields of the superclass by using the `super` keyword.
- Scala supports **single inheritance**, which means that a class can only extend one superclass.
- Scala also supports **multiple inheritance** through **traits**, which are abstract types that can contain methods and fields.
- A class can mix in multiple traits by using the `with` keyword.
- Traits can also extend other traits or classes, forming a linear hierarchy called the **linearization** of the class.
- The order of the traits in the linearization determines the method resolution and the super calls.