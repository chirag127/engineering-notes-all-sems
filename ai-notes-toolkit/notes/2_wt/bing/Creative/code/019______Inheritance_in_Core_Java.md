#### Inheritance in Core Java

Inheritance is a mechanism that allows a class to inherit the properties and methods of another class. The class that inherits is called the subclass or the child class, and the class that is inherited from is called the superclass or the parent class. Inheritance is one of the fundamental concepts of object-oriented programming, as it enables code reuse and polymorphism.

In Java, inheritance is achieved by using the `extends` keyword. For example, the following code defines a class `Animal` with a method `makeSound()`, and a class `Dog` that inherits from `Animal` and overrides the `makeSound()` method.

```java
// Define a superclass Animal
class Animal {
  // A method to make a sound
  public void makeSound() {
    System.out.println("Animal makes a sound");
  }
}

// Define a subclass Dog that inherits from Animal
class Dog extends Animal {
  // Override the makeSound() method
  @Override
  public void makeSound() {
    System.out.println("Dog barks");
  }
}
```

To use inheritance, we can create an object of the subclass and access the inherited properties and methods. For example, the following code creates a `Dog` object and calls the `makeSound()` method.

```java
// Create a Dog object
Dog dog = new Dog();

// Call the inherited method
dog.makeSound(); // Prints "Dog barks"
```

We can also use inheritance to create a hierarchy of classes that share common attributes and behaviors. For example, we can define another subclass `Cat` that inherits from `Animal` and overrides the `makeSound()` method.

```java
// Define a subclass Cat that inherits from Animal
class Cat extends Animal {
  // Override the makeSound() method
  @Override
  public void makeSound() {
    System.out.println("Cat meows");
  }
}
```

Now we can create objects of both `Dog` and `Cat` classes and use them interchangeably, as they are both subclasses of `Animal`. This is an example of polymorphism, which means the ability of an object to take different forms depending on the context.

```java
// Create a Dog object
Dog dog = new Dog();

// Create a Cat object
Cat cat = new Cat();

// Create an array of Animal objects
Animal[] animals = {dog, cat};

// Loop through the array and call the makeSound() method
for (Animal animal : animals) {
  animal.makeSound(); // Prints "Dog barks" and "Cat meows"
}
```

Inheritance is a powerful feature of Java that allows us to create classes that are related and share common functionality. It also enables us to write code that is more modular, reusable, and maintainable.