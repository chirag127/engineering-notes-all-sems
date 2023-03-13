#### Inheritance in Core Java

Inheritance is one of the key concepts in object-oriented programming. It allows developers to create new classes based on existing ones and to reuse code, which can save a lot of time and effort.

##### Syntax
```java
class SubClass extends SuperClass {
   // fields and methods
}
```

##### Explanation
- A subclass is a new class that is created based on an existing class, called the superclass.
- The subclass inherits all the fields and methods of the superclass, and can also add its own fields and methods.
- The keyword `extends` is used to create a subclass.
- The subclass can access the public and protected fields and methods of its superclass, but not the private ones.
- If a method is defined in both the superclass and the subclass, the subclass's version of the method will be used.
- The subclass can override the methods of the superclass by defining its own version of the method with the same name and parameters.

##### Example
```java
class Animal {
   public void eat() {
      System.out.println("The animal is eating");
   }
}

class Dog extends Animal {
   public void bark() {
      System.out.println("The dog is barking");
   }
}

public class Main {
   public static void main(String[] args) {
      Dog myDog = new Dog();
      myDog.eat(); // output: The animal is eating
      myDog.bark(); // output: The dog is barking
   }
}
```

##### Advantages of Inheritance
- Code reusability: Inheritance allows developers to reuse code from existing classes, which can save a lot of time and effort.
- Polymorphism: Inheritance allows objects of different classes to be treated as objects of the same class, which can simplify code and make it more flexible.
- Easy to maintain: Inheritance can make code easier to maintain, because changes made to the superclass will automatically affect all the subclasses.

##### Disadvantages of Inheritance
- Tight coupling: Inheritance can create tight coupling between classes, which can make the code harder to maintain and change.
- Complexity: Inheritance can make the code more complex, because it introduces new relationships between classes and can create multiple levels of inheritance.

##### Mnemonic
A good mnemonic for inheritance in Java is "is-a". This means that a subclass "is-a" type of its superclass. For example, a Dog "is-a" type of Animal.

##### Learning Trick
One way to remember the syntax of inheritance in Java is to think of it as "subclass extends superclass". Another way is to remember that the keyword "extends" is used to create a subclass.