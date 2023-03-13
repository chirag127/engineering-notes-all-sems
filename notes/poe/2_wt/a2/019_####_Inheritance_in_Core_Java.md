 Here is the content in markdown format for the topic #### Inheritance in Core Java:

#### Inheritance in Core Java

Inheritance is one of the fundamental concepts of Object Oriented Programming (OOP). It allows us to define a class that inherits all the methods and properties from another class.

Inheritance allows us to reuse the code from the parent class. We can extend the functionality of the parent class by adding more methods and properties in the child class.

**Rules for Inheritance:**

1. The class which inherits the properties of another class is known as subclass (child class) and the class whose properties are inherited is known as superclass (parent class) or base class.
2. A class cannot inherit from multiple superclasses. A subclass can inherit from only one superclass.
3. The inherited methods can be overridden in the child class. This allows us to modify the implementation of methods defined in the parent class.
4. The overridden methods in the child class must have the same name, return type and parameters as the parent class method.

**Mnemonics:**

Subclass = Child, Superclass = Parent

**Examples:**

```java
class Animal {
   void eat() {
      System.out.println("Eating...");
   }
}

class Dog extends Animal {
   void bark() {
      System.out.println("Woof!");
   }
}

class TestInheritance {
   public static void main(String args[]) {
      Dog d = new Dog();
      d.eat(); // Invokes eat() method of Animal
      d.bark(); // Invokes bark() method of Dog
   }
}
```

In the above example, class Dog inherits the eat() method from its parent class Animal.

**Advantages:**

1. Code reusability - We can reuse the methods and properties of the parent class. This avoids duplication of code.
2. Extensibility - We can extend the functionality of existing classes.
3. Modularity - The code is divided into logical units which increases maintainability of the code.

**Disadvantages:**

1. The subclass becomes tightly coupled with the superclass. This may lead to unwanted dependencies.
2. The excessive use of inheritance can lead to very deep hierarchies which becomes difficult to understand and maintain.