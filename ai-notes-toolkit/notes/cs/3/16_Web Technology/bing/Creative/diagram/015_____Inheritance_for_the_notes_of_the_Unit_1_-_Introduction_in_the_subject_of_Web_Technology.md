Hello, I am Sydney, your AI assistant. I can help you with your study material for Web Technology. Here are some notes on the topic of inheritance:

### Inheritance

- Inheritance is a concept in object-oriented programming that allows one class to inherit the properties and methods of another class.
- Inheritance enables code reuse and reduces redundancy by allowing subclasses to share common features with their superclasses.
- Inheritance also supports polymorphism, which is the ability of an object to behave differently depending on its type or context.
- Inheritance can be implemented in different ways depending on the programming language, such as single inheritance, multiple inheritance, hierarchical inheritance, or hybrid inheritance.
- Inheritance can be represented by a class diagram, which shows the relationship between classes using a notation of boxes and lines. A subclass is connected to its superclass by a solid line with an empty arrowhead pointing to the superclass. For example:

```text
+-----------------+
|    Animal       |
+-----------------+
| +name: String   |
| +age: int       |
+-----------------+
| +makeSound():void|
+-----------------+
       ^
       |
+-----------------+
|    Dog          |
+-----------------+
| +breed: String  |
+-----------------+
| +bark(): void   |
+-----------------+
```

- In this example, the class Dog inherits from the class Animal, which means that a Dog object has all the attributes and methods of an Animal object, plus its own specific attributes and methods.
- Inheritance can also be expressed by using keywords such as extends, implements, or inherits, depending on the programming language. For example, in Java, the class Dog can be defined as:

```java
public class Dog extends Animal {
  // attributes
  private String breed;

  // constructor
  public Dog(String name, int age, String breed) {
    super(name, age); // call the superclass constructor
    this.breed = breed;
  }

  // methods
  public String getBreed() {
    return breed;
  }

  public void bark() {
    System.out.println("Woof!");
  }

  @Override // override the superclass method
  public void makeSound() {
    bark();
  }
}
```

- In this example, the keyword extends indicates that the class Dog inherits from the class Animal. The keyword super is used to access the superclass constructor, attributes, or methods. The keyword @Override is used to indicate that the subclass method overrides the superclass method.