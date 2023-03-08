 Here is the content in markdown format for the topic ### friend functions for the notes of the Unit 5 - C++ Functions in the subject of Object Oriented System Design:

### Friend Functions

- Friend functions are non-member functions that are given access to the private and protected members of a class.
- They are declared using the `friend` keyword followed by the function prototype inside the class.
- For example:

```cpp
class MyClass {
  friend void friendFunc(); // friend function prototype
  // ...
};

void friendFunc() {
  // Can access private members of MyClass
}
```

- Why use friend functions?
    - Sometimes it is required for a non-member function to access private data of a class to perform some operation. In such cases, friend functions can be used.
    - They lead to simpler designs and avoid the use of public methods to share private data which can violate encapsulation.
- Points to note:
    - Friendship is not mutual - if class A declares a function of class B as friend, B's function does not become friend of A.
    - Friendship is not inherited - friendship relation is not inherited to derived classes.
    - Global functions as well as methods of other classes can be declared as friends.
- Advantages:
    - Simpler design and avoids violating encapsulation.
    - Gives access to private data when required for operations.
- Disadvantages:
    - Overuse of friends can reduce encapsulation and information hiding in classes.
    - Dependence on friends can make code fragile and harder to maintain.
    - Friends have access to all private members which can be undesirable at times.

[Detailed diagrams and examples can be added here if required...]