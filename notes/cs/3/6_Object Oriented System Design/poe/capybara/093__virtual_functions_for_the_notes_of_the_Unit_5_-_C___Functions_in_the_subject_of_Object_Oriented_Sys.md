### Virtual Functions for the Notes of Unit 5 - C++ Functions in the Subject of Object Oriented System Design

Object-Oriented Programming (OOP) is a programming paradigm that is widely used in software development. One of the key features of OOP is the use of classes and objects. In C++, classes are used to encapsulate data and functions into a single unit. Functions within a class are called member functions. 

In C++, functions can be classified into two types: non-virtual and virtual functions. Virtual functions are an important concept in C++ as they enable polymorphism. Polymorphism is a powerful feature of OOP that allows objects of different types to be treated as if they are of the same type.

Here are some key points to keep in mind about virtual functions:

- Virtual functions are declared in the base class and are implemented in the derived class.
- The base class should declare a virtual function using the keyword "virtual".
- Virtual functions can be overridden in the derived class using the same function signature.
- When a virtual function is called using a pointer or reference to the base class, the implementation in the derived class is called.
- If a class contains a virtual function, it is called a polymorphic class.

Here is an example of how to use virtual functions in C++:

```
class Shape{
    public:
        virtual void draw() {
            //implementation
        }
};

class Circle : public Shape{
    public:
        void draw() {
            //implementation
        }
};

int main() {
    Shape *s1 = new Circle();
    s1->draw(); //calls the draw function of Circle class
    delete s1;
    return 0;
}
```

In the above example, we have a base class Shape with a virtual function called draw(). We also have a derived class called Circle which overrides the draw() function. In the main() function, we create an object of the Circle class and store it in a pointer to the Shape class. When we call the draw() function using the Shape pointer, it calls the draw() function of the Circle class.

In conclusion, virtual functions are an important concept in C++ as they enable polymorphism. Polymorphism is a powerful feature of OOP that allows objects of different types to be treated as if they are of the same type. By using virtual functions, we can achieve run-time polymorphism, which is essential in writing flexible and maintainable code.