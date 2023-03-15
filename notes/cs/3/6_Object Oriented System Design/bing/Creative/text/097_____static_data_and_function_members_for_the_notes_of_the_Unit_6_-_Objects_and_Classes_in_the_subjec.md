### Static Data and Function Members

- Static data members are class variables that are shared by all objects of the class. They are declared with the keyword `static` inside the class definition, but outside any member function. They are initialized outside the class definition, usually in a source file.
- Static function members are class functions that can access only static data members or other static function members. They are also declared with the keyword `static` inside the class definition, but outside any member function. They are defined outside the class definition, usually in a source file.
- Static data and function members are useful for defining constants, counters, utility functions, and other class-related features that do not depend on the state of individual objects.
- Static data and function members have the following characteristics:
  - They are associated with the class, not with any object.
  - They are allocated memory only once, when the program starts.
  - They have the same scope as the class, meaning they can be accessed by any function or object that can access the class.
  - They have the same visibility as the class, meaning they can be public, private, or protected.
  - They can be initialized only by constant expressions or by constructors of other static objects of the same class.
  - They can be accessed by using the class name and the scope resolution operator `::`, or by using an object of the class and the dot operator `.`.
- Example of static data and function members:

```cpp
// Class definition
class Counter {
  private:
    static int count; // static data member
  public:
    Counter() { count++; } // constructor
    ~Counter() { count--; } // destructor
    static int getCount() { return count; } // static function member
};

// Static data member initialization
int Counter::count = 0;

// Main function
int main() {
  cout << "Initial count: " << Counter::getCount() << endl; // access static function member using class name
  Counter c1, c2, c3; // create three objects
  cout << "Current count: " << c1.getCount() << endl; // access static function member using object
  return 0;
}
```

- Output:

```
Initial count: 0
Current count: 3
```