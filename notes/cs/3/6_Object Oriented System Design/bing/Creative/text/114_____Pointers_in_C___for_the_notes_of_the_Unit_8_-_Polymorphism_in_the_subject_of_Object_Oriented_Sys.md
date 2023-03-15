### Pointers in C++ for Polymorphism

- Polymorphism is the ability of an object to behave differently depending on the context.
- In C++, polymorphism is achieved by using inheritance and virtual functions.
- Inheritance allows a derived class to inherit the properties and methods of a base class, and optionally override or extend them.
- Virtual functions are functions that are declared with the `virtual` keyword in the base class, and can be redefined by the derived classes.
- To use polymorphism in C++, we need to use pointers or references to the base class type, and assign them to the derived class objects.
- Pointers are variables that store the memory address of another variable or object.
- Pointers can be declared with the `*` operator, and dereferenced with the `*` or `->` operators.
- For example, if we have a base class `Shape` and two derived classes `Circle` and `Square`, we can declare a pointer to `Shape` and assign it to a `Circle` or `Square` object:

```cpp
Shape *ptr; // pointer to Shape
ptr = new Circle(10); // assign it to a Circle object
ptr->draw(); // call the draw method of Circle
ptr = new Square(5); // assign it to a Square object
ptr->draw(); // call the draw method of Square
```

- In this example, the `draw` method is a virtual function in the `Shape` class, and is overridden by the `Circle` and `Square` classes.
- The pointer `ptr` can point to any object that is a `Shape` or a subclass of `Shape`.
- The actual type of the object that `ptr` points to is determined at run-time, and the appropriate `draw` method is called.
- This is called **run-time polymorphism** or **dynamic binding**, because the binding of the function call to the function definition is done at run-time, not at compile-time.
- Run-time polymorphism allows us to write generic code that can work with different types of objects, without knowing their exact types in advance.
- For example, we can write a function that takes a pointer to `Shape` as a parameter, and calls its `draw` method:

```cpp
void drawShape(Shape *s) {
  s->draw(); // call the draw method of the object that s points to
}
```

- This function can work with any object that is a `Shape` or a subclass of `Shape`, such as `Circle` or `Square`.
- We can pass different types of objects to this function, and it will call the correct `draw` method for each object:

```cpp
drawShape(new Circle(10)); // draw a circle
drawShape(new Square(5)); // draw a square
```

- Pointers are essential for polymorphism in C++, because they allow us to refer to objects of different types with a common base type.
- Without pointers, we would have to use the actual type of the object, and lose the benefit of polymorphism.
- For example, if we declare a variable of type `Shape`, and assign it to a `Circle` or `Square` object, we would lose the information about the actual type of the object, and only be able to call the methods of the `Shape` class:

```cpp
Shape s; // variable of type Shape
s = Circle(10); // assign it to a Circle object
s.draw(); // call the draw method of Shape, not Circle
s = Square(5); // assign it to a Square object
s.draw(); // call the draw method of Shape, not Square
```

- This is called **compile-time polymorphism** or **static binding**, because the binding of the function call to the function definition is done at compile-time, based on the type of the variable.
- Compile-time polymorphism does not allow us to write generic code that can work with different types of objects, because it requires us to know the exact type of the object in advance.
- Compile-time polymorphism is also less flexible and less efficient than run-time polymorphism, because it does not allow us to override or extend the behavior of the base class methods in the derived classes.