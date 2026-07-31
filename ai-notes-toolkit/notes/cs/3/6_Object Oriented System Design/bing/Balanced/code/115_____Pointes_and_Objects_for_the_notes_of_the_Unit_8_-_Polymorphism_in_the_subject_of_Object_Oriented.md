# Pointers and Objects for the notes of the Unit 8 - Polymorphism in the subject of Object Oriented System Design

- Polymorphism is the ability of an object to behave differently depending on the context or the type of the object.
- Polymorphism can be achieved by using inheritance and virtual functions in C++.
- Inheritance allows a derived class to inherit the common features of a base class, and also to add new features or override existing ones.
- Virtual functions are functions that are declared with the keyword `virtual` in the base class, and can be redefined by the derived classes.
- Virtual functions allow the compiler to bind the function call to the appropriate function definition at run time, depending on the type of the object that is pointed by the pointer or referenced by the reference.
- Pointers and references are used to implement polymorphism, because they can store the address of any object of the same base class or its derived classes.
- Pointers and references can also be used to access the members and methods of the object they point or refer to, using the `->` or `.` operators respectively.
- Example:

```cpp
// Base class
class Polygon {
  protected:
    int width, height;
  public:
    void set_values (int a, int b)
      { width=a; height=b; }
    virtual int area ()
      { return 0; }
};

// Derived class 1
class Rectangle: public Polygon {
  public:
    int area ()
      { return width * height; }
};

// Derived class 2
class Triangle: public Polygon {
  public:
    int area ()
      { return (width * height / 2); }
};

int main () {
  Rectangle rect;
  Triangle trgl;
  Polygon poly;
  Polygon * ppoly1 = &rect;
  Polygon * ppoly2 = &trgl;
  Polygon * ppoly3 = &poly;
  ppoly1->set_values (4,5);
  ppoly2->set_values (4,5);
  ppoly3->set_values (4,5);
  cout << ppoly1->area() << '\n';
  cout << ppoly2->area() << '\n';
  cout << ppoly3->area() << '\n';
  return 0;
}
```

- Output:

```cpp
20
10
0
```

- Explanation:

  - The pointer `ppoly1` points to an object of type `Rectangle`, so it calls the `area` function defined in the `Rectangle` class, which returns the product of `width` and `height`.
  - The pointer `ppoly2` points to an object of type `Triangle`, so it calls the `area` function defined in the `Triangle` class, which returns the half of the product of `width` and `height`.
  - The pointer `ppoly3` points to an object of type `Polygon`, so it calls the `area` function defined in the `Polygon` class, which returns 0 by default.
  - This is an example of polymorphism, because the same function name `area` is used to invoke different function definitions, depending on the type of the object that is pointed by the pointer.