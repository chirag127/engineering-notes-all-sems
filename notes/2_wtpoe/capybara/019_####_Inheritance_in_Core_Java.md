#### Inheritance in Core Java

Inheritance is a fundamental concept of object-oriented programming. It allows one class to inherit properties and behavior from another class. In Java, we can achieve inheritance by using the `extends` keyword.

#### Types of Inheritance in Java

1. Single Inheritance: In this type of inheritance, a class inherits properties and behavior from a single parent class.

2. Multilevel Inheritance: In this type of inheritance, a class inherits properties and behavior from a parent class, which in turn inherits from another parent class.

3. Hierarchical Inheritance: In this type of inheritance, multiple classes inherit properties and behavior from a single parent class.

4. Multiple Inheritance (not supported in Java): In this type of inheritance, a class inherits properties and behavior from multiple parent classes.

#### Syntax of Inheritance in Java

```java
class Parent {
   // properties and methods of Parent class
}

class Child extends Parent {
   // properties and methods of Child class
}
```

#### Advantages of Inheritance in Java

1. Reusability: Inheritance allows us to reuse the existing code from the parent class in the child class.

2. Code Organization: Inheritance allows us to organize the code in a hierarchical manner, making it easier to understand and maintain.

3. Polymorphism: Inheritance allows us to achieve polymorphism, which means that a child class can be used wherever the parent class is expected.

#### Disadvantages of Inheritance in Java

1. Tight Coupling: Inheritance can lead to tight coupling between the parent and child classes, making it difficult to modify the code.

2. Code Complexity: Inheritance can make the code complex and difficult to understand, especially when there are multiple levels of inheritance.

#### Mnemonic for Inheritance in Java

One simple mnemonic for remembering the concept of inheritance in Java is the acronym "IS-A". Inheritance can be thought of as an "IS-A" relationship, where a child class "IS-A" type of its parent class. For example, a `Dog` class "IS-A" type of an `Animal` class.

#### Example of Inheritance in Java

```java
class Animal {
   void move() {
      System.out.println("Animals can move");
   }
}

class Dog extends Animal {
   void bark() {
      System.out.println("Dogs can bark");
   }
}

public class Main {
   public static void main(String args[]) {
      Dog dog = new Dog();
      dog.move();
      dog.bark();
   }
}
```

In this example, the `Dog` class inherits the `move()` method from the `Animal` class, and adds its own `bark()` method. The `main()` method creates an object of the `Dog` class and calls its `move()` and `bark()` methods. The output of the program will be:

```
Animals can move
Dogs can bark
```

#### Conclusion

Inheritance is an important concept in Java, allowing us to reuse code, organize it in a hierarchical manner, and achieve polymorphism. However, it can also lead to tight coupling and code complexity if not used properly. By understanding the syntax and types of inheritance in Java, and using simple mnemonics like "IS-A", we can master this concept and use it effectively in our programs.