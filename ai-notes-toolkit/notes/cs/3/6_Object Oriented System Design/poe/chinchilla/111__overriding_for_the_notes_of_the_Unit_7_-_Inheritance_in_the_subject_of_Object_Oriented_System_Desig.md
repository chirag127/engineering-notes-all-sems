### Overriding in Inheritance

Inheritance is a fundamental concept in object-oriented programming that allows us to create new classes based on existing ones. One of the key features of inheritance is the ability to override methods in the parent class in the child class.

Overriding is the process of providing a new implementation for a method that is already defined in the parent class. When a method is called on an object of the child class, the overridden method in the child class is executed instead of the method in the parent class.

#### Rules for Overriding

When overriding a method, there are some rules that must be followed:

- The name, return type, and parameter list of the overriding method must match the method being overridden in the parent class.
- The access level of the overriding method cannot be more restrictive than the access level of the method being overridden. For example, if a method in the parent class is public, the overriding method in the child class cannot be private or protected.
- The overriding method can throw any exception that is allowed by the parent method or any exception that is a subclass of the allowed exceptions.

#### Example of Overriding

Let's consider a simple example to understand how overriding works:

```
class Animal {
  public void makeSound() {
    System.out.println("The animal makes a sound");
  }
}

class Cat extends Animal {
  public void makeSound() {
    System.out.println("Meow");
  }
}
```

In this example, we have a parent class `Animal` and a child class `Cat` that extends the `Animal` class. The `Animal` class has a method `makeSound` that prints a message to the console. The `Cat` class overrides the `makeSound` method and provides its own implementation that prints "Meow" to the console.

Now, let's create an object of the `Cat` class and call the `makeSound` method:

```
Cat cat = new Cat();
cat.makeSound();
```

The output of the above code will be "Meow" because we have overridden the `makeSound` method in the `Cat` class.

#### When to Use Overriding

Overriding is useful when we want to provide a different implementation of a method in the child class than the one in the parent class. This is often the case when we want to customize the behavior of a method for a specific subclass.

However, it's important to use overriding carefully and only when necessary. Overriding can lead to confusion and unexpected behavior if not used correctly. Therefore, it's important to understand the rules for overriding and to test the behavior of the overridden method thoroughly.