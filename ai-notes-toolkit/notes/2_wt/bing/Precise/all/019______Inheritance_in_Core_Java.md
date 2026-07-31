#### Inheritance in Core Java

Inheritance is one of the four fundamental principles of Object-Oriented Programming (OOP) in Java. It allows a class to inherit the properties and methods of another class, enabling code reusability and reducing redundancy.

- **Superclass and Subclass**: Inheritance involves a superclass (also known as a base class or parent class) and a subclass (also known as a derived class or child class). The subclass inherits the properties and methods of the superclass.

- **Syntax**: To inherit from a superclass, the subclass uses the `extends` keyword followed by the name of the superclass. For example, `class Subclass extends Superclass { }`.

- **Access Modifiers**: The subclass can access the `public` and `protected` members of the superclass, but not its `private` members.

- **Method Overriding**: A subclass can override a method of the superclass by providing its own implementation of the method with the same name and signature.

- **The `super` Keyword**: The `super` keyword is used to refer to the members of the superclass from within the subclass. It can be used to call the superclass's constructor or to access its methods and fields.

- **Advantages**: Inheritance promotes code reusability and reduces redundancy. It also allows for the creation of more specialized classes based on a general class.

- **Disadvantages**: Inheritance can make the code more complex and harder to understand if not used properly. It can also lead to tight coupling between classes, making it harder to change the code in the future.

- **Example**:
```java
class Animal {
    public void eat() {
        System.out.println("Animal is eating");
    }
}

class Dog extends Animal {
    public void bark() {
        System.out.println("Dog is barking");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.eat(); // inherited from Animal class
        dog.bark(); // specific to Dog class
    }
}
```

- **Mnemonic**: A helpful mnemonic to remember the concept of inheritance is "IS-A". A subclass "IS-A" superclass. For example, a `Dog` IS-A `Animal`.

- **Learning Trick**: One way to better understand inheritance is to think of it in terms of real-life relationships. For example, a child inherits traits from their parents, just as a subclass inherits properties and methods from its superclass. This can help to visualize the concept and make it easier to remember.