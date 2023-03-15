# Protected Members in Inheritance

- Inheritance is a mechanism that allows a class to inherit the properties and behaviors of another class. The class that inherits is called the derived class, and the class that is inherited is called the base class.
- In C++, there are three types of inheritance: public, protected, and private. Each type of inheritance affects the access specifiers of the base class members in the derived class.
- Access specifiers are keywords that define the visibility and accessibility of class members. There are three access specifiers in C++: public, protected, and private.
- Public members are accessible from anywhere, protected members are accessible from within the class and its derived classes, and private members are accessible only from within the class.
- Protected members are useful when we want to create class members that are private to their class, but that can still be inherited and accessed by a derived class.
- The syntax for declaring a protected member is:

```cpp
class Base {
  protected:
    // protected member declaration
};
```

- The syntax for inheriting a base class as protected is:

```cpp
class Derived: protected Base {
  // derived class definition
};
```

- The following table summarizes the effect of protected inheritance on the access specifiers of the base class members in the derived class :

| Base class access specifier | Derived class access specifier |
| --------------------------- | ----------------------------- |
| public                      | protected                     |
| protected                   | protected                     |
| private                     | inaccessible                  |

- This means that the public and protected members of the base class become protected members of the derived class, and the private members of the base class remain inaccessible to the derived class.
- Protected inheritance is useful when we want to restrict the access to the base class members from outside the derived class, but still allow the derived class to access them.
- An example of protected inheritance is:

```cpp
// A base class
class Animal {
  protected:
    string name;
    int age;
  public:
    Animal(string n, int a) {
      name = n;
      age = a;
    }
    void display() {
      cout << "Name: " << name << endl;
      cout << "Age: " << age << endl;
    }
};

// A derived class
class Dog: protected Animal {
  private:
    string breed;
  public:
    Dog(string n, int a, string b): Animal(n, a) {
      breed = b;
    }
    void show() {
      display(); // accessing protected member of base class
      cout << "Breed: " << breed << endl;
    }
};

int main() {
  Dog d("Max", 5, "Labrador");
  // d.display(); // error: protected member of base class
  d.show(); // accessing public member of derived class
  return 0;
}
```

- The output of the above program is:

```
Name: Max
Age: 5
Breed: Labrador
```

- In the above example, the class Animal has a protected member name and age, and a public member display. The class Dog inherits the class Animal as protected, and has a private member breed and a public member show. The class Dog can access the protected members of the class Animal, but not the private members. The main function can access the public members of the class Dog, but not the protected members of the class Animal.