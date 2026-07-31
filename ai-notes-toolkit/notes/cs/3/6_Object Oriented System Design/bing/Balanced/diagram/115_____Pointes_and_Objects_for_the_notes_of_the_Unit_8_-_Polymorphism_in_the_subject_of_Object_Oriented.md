### Pointers and Objects for the notes of the Unit 8 - Polymorphism in the subject of Object Oriented System Design

- Polymorphism is the ability of an object to behave differently depending on the context or the type of the object.
- Polymorphism can be achieved by using inheritance and virtual functions in C++.
- Inheritance allows a derived class to inherit the common features and behavior of a base class, and also to add or override some of them.
- Virtual functions are functions that are declared with the keyword `virtual` in the base class, and can be redefined by the derived classes.
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
- The function `area` is declared as virtual in the base class, and redefined by the derived classes.
- Now, we can declare two pointers to `Polygon` and assign them the addresses of objects of type `Rectangle` and `Triangle`, respectively:

```c++
Polygon *ppoly1 = new Rectangle;
Polygon *ppoly2 = new Polygon;
ppoly1->set_values (4,5);
ppoly2->set_values (4,5);
```

- These assignments are valid, since both `Rectangle` and `Triangle` are classes derived from `Polygon`.
- Now, we can call the `area` function on these pointers, and get the correct result depending on the type of the object they point to:

```c++
cout << ppoly1->area() << endl; // prints 20
cout << ppoly2->area() << endl; // prints 10
```

- This is polymorphism, because the same function call (`area`) behaves differently depending on the type of the object (`Rectangle` or `Triangle`) that is pointed by the base class pointer (`ppoly1` or `ppoly2`).
- If we did not use pointers or references, and instead declared the objects as variables of type `Polygon`, we would not get the same result:

```c++
Polygon poly1 = Rectangle();
Polygon poly2 = Triangle();
poly1.set_values (4,5);
poly2.set_values (4,5);
cout << poly1.area() << endl; // prints 0
cout << poly2.area() << endl; // prints 0
```

- This is because the objects are sliced, meaning that only the base class part of the object is copied, and the derived class part is ignored.
- Therefore, the function call (`area`) is bound to the base class function definition at compile time, and not to the derived class function definition at run time.
- This is called static binding or early binding, and it does not support polymorphism.
- To support polymorphism, we need dynamic binding or late binding, which is achieved by using pointers or references to access the objects of different derived classes using a single base class pointer or reference.