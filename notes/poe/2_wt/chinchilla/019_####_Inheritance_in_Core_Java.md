### Inheritance in Core Java

Inheritance is one of the fundamental concepts of object-oriented programming (OOP) and is extensively used in Java programming. It allows a class to inherit the properties and methods of another class, known as the parent or superclass. The class that inherits the properties and methods is known as the child or subclass.

#### Syntax
The syntax for defining a subclass in Java is as follows:

```java
class ChildClass extends ParentClass {
    // child class body
}
```

#### Types of Inheritance
In Java, there are five types of inheritance:
1. Single Inheritance: A class extends only one superclass.
2. Multilevel Inheritance: A class extends a subclass, which in turn extends another subclass.
3. Hierarchical Inheritance: Multiple classes extend the same superclass.
4. Multiple Inheritance: A class extends more than one superclass. (Java does not support this directly)
5. Hybrid Inheritance: A combination of two or more types of inheritance.

#### Access Modifiers in Inheritance
In Java, there are four access modifiers: public, private, protected, and default. These access modifiers determine the visibility of the class, methods, and variables. The following table shows the access levels that can be used when inheriting classes:

| Access Modifier | Same Class | Package | Subclass | Anywhere |
| --- | --- | --- | --- | --- |
| public | Yes | Yes | Yes | Yes |
| protected | Yes | Yes | Yes | No |
| default | Yes | Yes | No | No |
| private | Yes | No | No | No |

#### Advantages of Inheritance
- Code reusability: Inheritance allows subclasses to inherit the properties and methods of their parent class, reducing code duplication and increasing code reuse.
- Easy maintenance: Changes made to the parent class are automatically reflected in all its subclasses.
- Polymorphism: Inheritance allows for the implementation of polymorphism, where objects of different classes can be treated as objects of the same superclass.

#### Disadvantages of Inheritance
- Tight Coupling: If a subclass is tightly coupled with its parent class, any changes made to the parent class can potentially affect the subclass.
- Inflexibility: Inheritance can sometimes lead to inflexibility in the design, as it can make it difficult to modify the inheritance hierarchy once it is established.

#### Mnemonics and Learning Tricks
- "IS-A" relationship: Inheritance can be thought of as an "IS-A" relationship, where a subclass "IS-A" type of its parent class. For example, a Car "IS-A" Vehicle.

#### Example
```java
class Vehicle {
    int speed;
    void setSpeed(int s) {
        speed = s;
    }
    void displaySpeed() {
        System.out.println("Speed: " + speed);
    }
}

class Car extends Vehicle {
    int numWheels;
    void setNumWheels(int n) {
        numWheels = n;
    }
    void displayNumWheels() {
        System.out.println("Number of wheels: " + numWheels);
    }
}

class Main {
    public static void main(String[] args) {
        Car c = new Car();
        c.setSpeed(60);
        c.setNumWheels(4);
        c.displaySpeed();
        c.displayNumWheels();
    }
}
```

#### Applications of Inheritance
- Inheritance is used extensively in Java frameworks such as Spring and Hibernate to provide a common set of functionalities to multiple classes.
- It is used in GUI programming to create a hierarchy of graphical components, where each component inherits the properties and methods of its parent component.
- Inheritance is used in game development to create a hierarchy of game objects, where each object inherits the properties and methods of its parent object.

In summary, Inheritance is a powerful concept in Java that allows for code reusability, easy maintenance, and polymorphism. It is important to understand the different types of inheritance, access modifiers, advantages, and disadvantages associated with inheritance to use it effectively in Java programming.