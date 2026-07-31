# Hierarchical Inheritance

- Hierarchical inheritance is a way of transmitting features from a parent class to multiple child classes in object-oriented programming languages .
- The parent class or superclass is the class from which the properties are taken, i.e. the features are inherited. The child classes or subclasses are the classes that inherit the properties from the parent class .
- In hierarchical inheritance, there is one base class and multiple derived classes. Several other classes can inherit the derived classes as well. Hierarchical structures thus form a tree-like structure.
- The inheritance hierarchy of an object is fixed at instantiation when the object's type is selected and does not change with time.
- Hierarchical inheritance allows code reusability, as the common features of the parent class can be used by multiple child classes without duplication.
- Hierarchical inheritance also enables polymorphism, as the same method name can have different implementations in different child classes.
- An example of hierarchical inheritance in C++ is:

```cpp
// Base class
class Animal {
  public:
    void eat() {
      cout << "Eating..." << endl;
    }
};

// Derived class
class Dog : public Animal {
  public:
    void bark() {
      cout << "Barking..." << endl;
    }
};

// Derived class
class Cat : public Animal {
  public:
    void meow() {
      cout << "Meowing..." << endl;
    }
};

// Main function
int main() {
  // Create objects of derived classes
  Dog d;
  Cat c;

  // Call methods of base class
  d.eat();
  c.eat();

  // Call methods of derived classes
  d.bark();
  c.meow();

  return 0;
}
```