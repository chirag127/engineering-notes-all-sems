### Pointers and Objects for the notes of the Unit 8 - Polymorphism in the subject of Object Oriented System Design

- Polymorphism is the ability of an object to behave differently depending on the context or the type of the object.
- Polymorphism can be achieved by using inheritance and virtual functions in C++.
- Inheritance allows a derived class to inherit the common features and behavior of a base class, and also to add or override some of them.
- Virtual functions are functions that are declared with the `virtual` keyword in the base class, and can be redefined by the derived classes.
- Virtual functions allow the compiler to bind the function call to the appropriate function definition at run time, depending on the type of the object that is pointed or referenced by the base class pointer or reference.
- Pointers and references are used to implement polymorphism because they allow us to access the objects of different derived classes using a single base class pointer or reference.
- For example, consider the following class hierarchy:

```c++
class Polygon {
  protected:
    int width, height;
  public:
    void set_values (int a, int b)
      { width=a; height=b; }
    virtual int area ()
      { return 0; }
};

class Rectangle: public Polygon {
  public:
    int area ()
      { return width * height; }
};

class Triangle: public Polygon {
  public:
    int area ()
      { return width * height / 2; }
};
```

- In this example, `Polygon` is the base class, and `Rectangle` and `Triangle` are the derived classes.
- The base class has a virtual function `area` that returns 0, and the derived classes override this function to return the correct area of the shape.
- Now, we can declare two pointers to `Polygon` and assign them the addresses of the objects of `Rectangle` and `Triangle`, respectively:

```c++
Polygon *ppoly1 = new Rectangle;
Polygon *ppoly2 = new Triangle;
```

- These assignments are valid, since both `Rectangle` and `Triangle` are classes derived from `Polygon`.
- Now, we can use the pointers to call the `area` function on the objects:

```c++
ppoly1->set_values (4,5);
ppoly2->set_values (4,5);
cout << ppoly1->area() << endl;
cout << ppoly2->area() << endl;
```

- The output of this code will be:

```c++
20
10
```

- This is because the compiler will invoke the appropriate `area` function depending on the type of the object that is pointed by the pointer, even though the pointer is of type `Polygon`.
- This is an example of polymorphism, where the same function name can have different behaviors for different objects.
- If we did not use pointers or references, and instead declared the objects as `Polygon`, then the polymorphism would not work, and the compiler would always call the base class function `area` that returns 0.
- This is because the compiler would bind the function call to the function definition at compile time, based on the type of the object, and not at run time, based on the type of the pointer or reference.
- Therefore, pointers and references are essential for implementing polymorphism in C++.