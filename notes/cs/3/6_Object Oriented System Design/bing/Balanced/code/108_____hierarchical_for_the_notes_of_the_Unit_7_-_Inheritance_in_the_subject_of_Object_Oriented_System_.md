### Hierarchical Inheritance

- Hierarchical inheritance is a way of transmitting features from a parent class to one or more child classes in object-oriented programming languages.
- The parent class or superclass is the class from which the properties are taken, i.e. the features are inherited.
- The child classes or subclasses are the classes that inherit the properties from the parent class.
- In hierarchical inheritance, there is one parent class and multiple child classes.
- The child classes can also be inherited by other classes, forming a tree-like structure of inheritance hierarchy.
- Hierarchical inheritance allows code reusability, as the common features of the parent class can be used by the child classes without repetition.
- Hierarchical inheritance also enables polymorphism, as the child classes can override or modify the inherited methods of the parent class according to their own functionality.
- An example of hierarchical inheritance in C++ is:

```cpp
// Parent class
class Animal {
  public:
    void eat() {
      cout << "Animal is eating" << endl;
    }
};

// Child class 1
class Dog : public Animal {
  public:
    void bark() {
      cout << "Dog is barking" << endl;
    }
};

// Child class 2
class Cat : public Animal {
  public:
    void meow() {
      cout << "Cat is meowing" << endl;
    }
};

// Child class 3
class Tiger : public Cat {
  public:
    void roar() {
      cout << "Tiger is roaring" << endl;
    }
};
```

- In this example, Animal is the parent class, and Dog and Cat are the child classes that inherit the eat() method from Animal.
- Cat is also the parent class of Tiger, which is another child class that inherits the meow() method from Cat and the eat() method from Animal.
- Tiger is the grandchild class of Animal, and the child class of Cat.