#### Inheritance in Core Java
Inheritance is a mechanism in Java that allows one class to inherit the properties and behaviors of another class. This is achieved by using the `extends` keyword. Here is an example:

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
        dog.eat();
        dog.bark();
    }
}
```

In this example, the `Dog` class extends the `Animal` class, which means that the `Dog` class inherits the `eat` method from the `Animal` class. The `Dog` class also has its own method, `bark`. In the `main` method, we create an instance of the `Dog` class and call both the `eat` and `bark` methods on it. The output of this code will be:

```
Animal is eating
Dog is barking
```