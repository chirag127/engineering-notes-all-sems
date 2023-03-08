### Virtual Base Class for the Notes of the Unit 7 - Inheritance in the Subject of Object Oriented System Design

Inheritance is one of the key features of Object Oriented Programming (OOP). It allows us to create new classes that are built upon existing classes. However, as we create deeper and more complex class hierarchies, we can run into issues with multiple inheritance. One of the ways to resolve these issues is through the use of Virtual Base Classes.

#### What is a Virtual Base Class?

A virtual base class is a base class that is declared as virtual in a derived class. When a class that derives from a virtual base class is instantiated, only one instance of the virtual base class is created. This helps to avoid issues with multiple inheritance, such as the "diamond problem".

#### How to Declare a Virtual Base Class?

A virtual base class is declared in a derived class by using the "virtual" keyword when inheriting from the base class.

```c++
class Base {
public:
    int x;
};

class Derived1 : virtual public Base {
public:
    int y;
};

class Derived2 : virtual public Base {
public:
    int z;
};

class Derived3 : public Derived1, public Derived2 {
public:
    int w;
};
```

In the above example, the class `Base` is declared as a virtual base class in both `Derived1` and `Derived2`. This ensures that only one instance of `Base` is created when `Derived3` is instantiated.

#### Advantages of Virtual Base Class

- Helps to resolve issues with multiple inheritance, such as the "diamond problem".
- Ensures that only one instance of a base class is created, which can help to reduce memory usage.

#### Disadvantages of Virtual Base Class

- Can lead to more complex code and class hierarchies.
- Can have a slight performance impact due to the use of virtual function tables.

#### Example of Virtual Base Class

```c++
#include <iostream>

class Animal {
public:
    virtual void speak() = 0;
};

class Mammal : virtual public Animal {
public:
    void speak() {
        std::cout << "Mammal speaking!" << std::endl;
    }
};

class Bird : virtual public Animal {
public:
    void speak() {
        std::cout << "Bird speaking!" << std::endl;
    }
};

class Platypus : public Mammal, public Bird {
public:
    void speak() {
        Mammal::speak();
        Bird::speak();
        std::cout << "Platypus speaking!" << std::endl;
    }
};

int main() {
    Platypus p;
    p.speak();
    return 0;
}
```

In the above example, `Animal` is declared as a virtual base class in both `Mammal` and `Bird`. This ensures that only one instance of `Animal` is created when `Platypus` is instantiated. The `speak()` function is overridden in both `Mammal` and `Bird`, and is called in the `speak()` function of `Platypus`.

#### Applications of Virtual Base Class

- Used in complex class hierarchies to avoid issues with multiple inheritance.
- Can be used to reduce memory usage in certain situations.

In conclusion, the use of virtual base classes can help to avoid issues with multiple inheritance in complex class hierarchies. By declaring a base class as virtual, we can ensure that only one instance of the base class is created. While there are some disadvantages to using virtual base classes, they can be useful in certain situations.