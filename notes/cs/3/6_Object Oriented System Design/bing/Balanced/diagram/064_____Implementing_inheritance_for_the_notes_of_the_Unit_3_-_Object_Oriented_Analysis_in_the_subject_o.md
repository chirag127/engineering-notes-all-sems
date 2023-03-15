### Implementing inheritance for the notes of the Unit 3 - Object Oriented Analysis in the subject of Object Oriented System Design

- Inheritance is the mechanism of basing an object or class upon another object or class, retaining similar implementation.
- Inheritance enables you to create new classes that reuse, extend, and modify the behavior defined in other classes.
- Inheritance is one of the three primary characteristics of object-oriented programming, together with encapsulation and polymorphism.
- Inheritance provides code re-usability, as you can inherit the properties and methods of one class into another class, instead of writing the same code again and again.
- Inheritance also supports the concept of hierarchical classification, as you can form a hierarchy of classes that share some common attributes and behaviors.

- To implement inheritance, you need to define a base class (also called a super class or a parent class) and a derived class (also called a sub class or a child class).
- The base class is the general class that defines the common attributes and methods for all the derived classes.
- The derived class is the specific class that inherits the attributes and methods from the base class, and can also add its own attributes and methods or override the inherited ones.
- The syntax for defining a derived class varies depending on the programming language, but usually involves using a keyword such as `extends`, `inherits`, or `:` to indicate the relationship with the base class.
- For example, in Java, you can define a base class called `Animal` and a derived class called `Dog` as follows:

```java
// Base class
public class Animal {
  // Attributes
  private String name;
  private int age;

  // Constructor
  public Animal(String name, int age) {
    this.name = name;
    this.age = age;
  }

  // Methods
  public String getName() {
    return name;
  }

  public int getAge() {
    return age;
  }

  public void makeSound() {
    System.out.println("Animal sound");
  }
}

// Derived class
public class Dog extends Animal {
  // Attributes
  private String breed;

  // Constructor
  public Dog(String name, int age, String breed) {
    // Calling the base class constructor
    super(name, age);
    this.breed = breed;
  }

  // Methods
  public String getBreed() {
    return breed;
  }

  // Overriding the inherited method
  public void makeSound() {
    System.out.println("Woof woof");
  }
}
```

- In this example, the `Dog` class inherits the attributes and methods from the `Animal` class, and also adds its own attribute (`breed`) and method (`getBreed`).
- The `Dog` class also overrides the inherited method `makeSound` to provide a more specific implementation for dogs.
- To create an object of the derived class, you can use the same syntax as for the base class, but pass the additional arguments for the derived class attributes.
- For example, you can create a `Dog` object as follows:

```java
// Creating a Dog object
Dog d = new Dog("Rex", 5, "German Shepherd");
```

- To access the inherited attributes and methods, you can use the dot operator (`.`) on the derived class object, as if they were defined in the derived class itself.
- For example, you can access the `name` and `age` attributes and the `getName` and `getAge` methods of the `Animal` class through the `Dog` object as follows:

```java
// Accessing the inherited attributes and methods
System.out.println(d.getName()); // Rex
System.out.println(d.getAge()); // 5
```

- To access the derived class attributes and methods, you can also use the dot operator (`.`) on the derived class object.
- For example, you can access the `breed` attribute and the `getBreed` method of the `Dog` class as follows:

```java
// Accessing the derived class attributes and methods
System.out.println(d.getBreed()); // German Shepherd
d.makeSound(); // Woof woof
```

- Note that the `makeSound` method of the `Dog` class overrides the `makeSound` method of the `Animal` class, so calling it on the `Dog` object will execute the derived class implementation, not the base class implementation.
- This is an example of polymorphism, which is another important