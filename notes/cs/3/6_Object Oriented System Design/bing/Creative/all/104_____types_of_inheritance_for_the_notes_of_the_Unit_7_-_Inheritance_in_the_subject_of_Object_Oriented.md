Hello, I am Sydney, your AI assistant. I can help you with your study material for Object Oriented System Design. Here are some notes on the topic of types of inheritance for Unit 7 - Inheritance.

# Types of Inheritance

Inheritance is a mechanism that allows a class to acquire the properties and methods of another class. The class that inherits is called the **subclass** or **derived class**, and the class that is inherited from is called the **superclass** or **base class**. Inheritance enables code reuse and polymorphism.

There are different types of inheritance in object oriented system design, such as:

- **Single inheritance**: A subclass inherits from only one superclass. For example, class B inherits from class A.

```java
class A {
  // properties and methods of class A
}

class B extends A {
  // properties and methods of class B
  // inherited properties and methods of class A
}
```

- **Multiple inheritance**: A subclass inherits from more than one superclass. For example, class C inherits from both class A and class B. This type of inheritance is not supported by some languages, such as Java, because it can cause ambiguity and complexity.

```java
class A {
  // properties and methods of class A
}

class B {
  // properties and methods of class B
}

class C extends A, B {
  // properties and methods of class C
  // inherited properties and methods of class A and class B
}
```

- **Hierarchical inheritance**: A superclass has more than one subclass. For example, class A is the superclass of class B and class C.

```java
class A {
  // properties and methods of class A
}

class B extends A {
  // properties and methods of class B
  // inherited properties and methods of class A
}

class C extends A {
  // properties and methods of class C
  // inherited properties and methods of class A
}
```

- **Multilevel inheritance**: A subclass inherits from another subclass, which in turn inherits from another superclass. For example, class C inherits from class B, which inherits from class A.

```java
class A {
  // properties and methods of class A
}

class B extends A {
  // properties and methods of class B
  // inherited properties and methods of class A
}

class C extends B {
  // properties and methods of class C
  // inherited properties and methods of class B and class A
}
```

- **Hybrid inheritance**: A combination of two or more types of inheritance. For example, class D inherits from class C and class E, which both inherit from class A. This type of inheritance can also cause ambiguity and complexity.

```java
class A {
  // properties and methods of class A
}

class B extends A {
  // properties and methods of class B
  // inherited properties and methods of class A
}

class C extends A {
  // properties and methods of class C
  // inherited properties and methods of class A
}

class D extends C, E {
  // properties and methods of class D
  // inherited properties and methods of class C, E and A
}

class E extends A {
  // properties and methods of class E
  // inherited properties and methods of class A
}
```

These are the main types of inheritance in object oriented system design. They can be used to model the relationships between classes and to achieve code reuse and polymorphism. However, they also have some drawbacks, such as increased coupling, reduced encapsulation, and potential conflicts. Therefore, it is important to use inheritance wisely and appropriately.