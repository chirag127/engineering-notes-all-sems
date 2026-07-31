## Unit 7 - Inheritance

Inheritance is a mechanism that allows a class to inherit the properties and methods of another class. The class that inherits is called the **subclass** or the **child class**. The class that is inherited from is called the **superclass** or the **parent class**.

The benefits of inheritance are:

- Code reuse: The subclass can use the existing code of the superclass without having to rewrite it.
- Extensibility: The subclass can add new features or modify the existing ones of the superclass according to its specific needs.
- Polymorphism: The subclass can override the methods of the superclass and provide different implementations for the same behavior.

The syntax for inheritance in Java is:

```java
class Subclass extends Superclass {
  // subclass fields and methods
}
```

The keyword `extends` indicates that the subclass inherits from the superclass.

The subclass inherits all the public and protected members of the superclass, but not the private ones. The subclass can access the inherited members directly, or use the keyword `super` to refer to the superclass.

The subclass can also define its own fields and methods that are not present in the superclass. These are called the **subclass-specific** members.

The subclass can also override the inherited methods of the superclass by providing a new definition for them. The overridden methods must have the same name, parameters, and return type as the superclass methods. The keyword `@Override` can be used to indicate that a method is overridden.

The subclass can also invoke the superclass constructor by using the keyword `super` followed by parentheses. The superclass constructor must be the first statement in the subclass constructor. If the subclass does not explicitly invoke the superclass constructor, the default constructor of the superclass is implicitly called.

An example of inheritance in Java is:

```java
class Animal {
  // superclass fields
  protected String name;
  protected int age;

  // superclass constructor
  public Animal(String name, int age) {
    this.name = name;
    this.age = age;
  }

  // superclass methods
  public void eat() {
    System.out.println(name + " is eating.");
  }

  public void sleep() {
    System.out.println(name + " is sleeping.");
  }
}

class Dog extends Animal {
  // subclass-specific field
  private String breed;

  // subclass constructor
  public Dog(String name, int age, String breed) {
    super(name, age); // invoking superclass constructor
    this.breed = breed;
  }

  // subclass-specific method
  public void bark() {
    System.out.println(name + " is barking.");
  }

  // overriding superclass method
  @Override
  public void eat() {
    System.out.println(name + " is eating dog food.");
  }
}

class Main {
  public static void main(String[] args) {
    // creating an object of the superclass
    Animal a = new Animal("Tommy", 5);
    a.eat(); // prints Tommy is eating.
    a.sleep(); // prints Tommy is sleeping.

    // creating an object of the subclass
    Dog d = new Dog("Rex", 3, "German Shepherd");
    d.eat(); // prints Rex is eating dog food.
    d.sleep(); // prints Rex is sleeping.
    d.bark(); // prints Rex is barking.
  }
}
```