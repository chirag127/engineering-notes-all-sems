### Multilevel Inheritance

- Multilevel inheritance is a type of inheritance in which a subclass inherits from another subclass that is also derived from a base class.
- In multilevel inheritance, the derived class inherits the features of the base class as well as the intermediate class.
- For example, if class A is the base class, class B is derived from class A, and class C is derived from class B, then class C is a multilevel subclass of class A.
- The syntax for multilevel inheritance in Java is:

```java
class A {
  // members of class A
}

class B extends A {
  // members of class B
}

class C extends B {
  // members of class C
}
```

- In this example, class C inherits the members of class B and class A. Class B inherits the members of class A.
- The advantages of multilevel inheritance are:
  - It allows the reuse of code and reduces redundancy.
  - It enables the creation of more specific and specialized classes from general classes.
  - It facilitates the implementation of hierarchical relationships among classes.
- The disadvantages of multilevel inheritance are:
  - It can create a complex class hierarchy that is difficult to understand and maintain.
  - It can cause ambiguity and confusion when multiple classes have the same members or methods.
  - It can increase the memory and execution overhead due to the multiple levels of inheritance.