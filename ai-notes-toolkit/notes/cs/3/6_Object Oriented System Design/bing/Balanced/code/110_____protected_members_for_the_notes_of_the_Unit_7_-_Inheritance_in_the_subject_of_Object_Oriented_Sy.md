### Protected Members

- Protected members are class members that have the access specifier `protected`.
- Protected members are accessible within the same class and its subclasses, but not outside the class.
- Protected members are useful for creating class members that are private to their class, but that can still be inherited and accessed by a derived class .
- Protected members can be accessed by using the `this` pointer, the same type protected members, or friend classes or functions.
- Protected members can be inherited in different ways: public, protected, or private .
- Public inheritance makes public members of the base class public in the derived class, and the protected members of the base class remain protected in the derived class.
- Protected inheritance makes the public and protected members of the base class protected in the derived class.
- Private inheritance makes the public and protected members of the base class private in the derived class.
- Private members of the base class are always inaccessible to the derived class, regardless of the inheritance type.
- The following table summarizes the access of protected members in different inheritance types:

| Inheritance Type | Base Class | Derived Class | Outside Class |
| ---------------- | ---------- | ------------- | ------------- |
| Public           | Protected  | Protected     | No            |
| Protected        | Protected  | Protected     | No            |
| Private          | Protected  | Private       | No            |

- The following code example illustrates the use of protected members in inheritance:

```cpp
// Base class
class Animal {
  protected: // protected members
    string name;
    int age;
  public: // public members
    Animal(string n, int a) {
      name = n;
      age = a;
    }
    void display() {
      cout << "Name: " << name << "\n";
      cout << "Age: " << age << "\n";
    }
};

// Derived class
class Dog : public Animal {
  private: // private members
    string breed;
  public: // public members
    Dog(string n, int a, string b) : Animal(n, a) {
      breed = b;
    }
    void display() {
      Animal::display(); // access protected members of base class
      cout << "Breed: " << breed << "\n";
    }
};

int main() {
  Dog d("Max", 5, "Labrador"); // create a Dog object
  d.display(); // access public and protected members of base and derived class
  // d.name = "Rex"; // error: cannot access protected member outside class
  return 0;
}
```

- The output of the code is:

```
Name: Max
Age: 5
Breed: Labrador
```