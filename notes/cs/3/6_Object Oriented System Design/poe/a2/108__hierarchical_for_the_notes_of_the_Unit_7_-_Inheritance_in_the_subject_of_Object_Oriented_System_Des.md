 Here are the notes in markdown format for the topic Inheritance in Object Oriented System Design:

### Inheritance

- Inheritance is a mechanism in which one class acquires the properties and behaviors of another class.
- The class that inherits the properties and behaviors is called a subclass (also called a derived class, extended class, or child class).
- The class that is being inherited from is called a superclass (also called a base class or parent class).
- Inheritance allows programmers to reuse code and is a key concept of object-oriented programming.
- The subclass inherits all the public and protected methods and properties of its superclass. It can also define its own.
- A subclass can override methods of its superclass. This means that a method in the subclass has the same name as in the superclass, but its implementation is different.
- The keyword `extends` is used to inherit from a superclass. For example:

```
class Animal {
  constructor(name) {
    this.name = name;
  }
  speak() {
    console.log(this.name + ' makes a noise.');
  }
}

class Dog extends Animal {
  speak() {
    console.log(this.name + ' barks.');
  }
}

let dog = new Dog('Rufus');
dog.speak(); // Rufus barks.
```

- In the example above, the `Dog` class extends the `Animal` class and overrides the `speak()` method.
- A class can extend only one other class. If a class extends multiple classes, it's called multiple inheritance and is not supported in JavaScript.
- To prevent a method from being overridden, you can mark it as `final`. A `final` method cannot be overridden in subclasses.

That's the notes on Inheritance in markdown format for Object Oriented System Design.