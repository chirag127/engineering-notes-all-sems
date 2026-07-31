## Unit 8 - Polymorphism

Polymorphism is a concept in object-oriented programming that allows objects of different classes to be used interchangeably. In other words, it is the ability of an object to take on many forms.

Polymorphism is achieved through two mechanisms: method overloading and method overriding.

### Method Overloading

Method overloading is a technique in which a class has two or more methods with the same name but different parameters. The method to be called is determined at compile-time based on the number and types of arguments passed to it.

Example:

```java
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }
    
    public double add(double a, double b) {
        return a + b;
    }
}
```

In the above example, the `add()` method is overloaded to accept both integers and doubles.

### Method Overriding

Method overriding is a technique in which a subclass provides its own implementation of a method that is already defined in its superclass. The method that is overridden must have the same name, return type, and parameters as the method in the superclass.

Example:

```java
public class Animal {
    public void makeSound() {
        System.out.println("Animal is making a sound");
    }
}

public class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Dog is barking");
    }
}
```

In the above example, the `Dog` class overrides the `makeSound()` method of the `Animal` class to provide its own implementation.

### Polymorphism in Java

In Java, polymorphism is achieved through the use of inheritance, interfaces, and abstract classes.

- Inheritance: A subclass inherits the properties and methods of its superclass, and can also override its methods to provide its own implementation.

- Interfaces: An interface defines a set of methods that a class must implement. Multiple classes can implement the same interface, allowing them to be used interchangeably.

- Abstract Classes: An abstract class is a class that cannot be instantiated, but can be subclassed. It can also define abstract methods, which must be implemented by its subclasses.

### Benefits of Polymorphism

Polymorphism has several benefits in object-oriented programming:

- Code Reusability: Polymorphism allows code to be reused across different classes and objects.

- Flexibility: Polymorphism allows for greater flexibility in designing and implementing software, as objects can be used interchangeably.

- Ease of Maintenance: Polymorphism makes it easier to maintain and update code, as changes can be made to a superclass or interface, and those changes will be reflected in all the subclasses that implement it.

### Conclusion

Polymorphism is a powerful concept in object-oriented programming that allows objects of different classes to be used interchangeably. It is achieved through method overloading and method overriding, and is implemented in Java through inheritance, interfaces, and abstract classes. Polymorphism has several benefits, including code reusability, flexibility, and ease of maintenance.