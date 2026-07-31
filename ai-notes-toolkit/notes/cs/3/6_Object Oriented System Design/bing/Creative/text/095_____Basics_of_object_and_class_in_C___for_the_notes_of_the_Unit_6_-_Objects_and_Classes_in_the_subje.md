### Basics of object and class in C++

- A class is a user-defined data type that can contain data members (variables) and member functions (methods) that operate on the data members.
- An object is an instance of a class that has its own state (values of the data members) and behavior (actions of the member functions).
- To define a class, the keyword `class` is used followed by the class name and the class body enclosed in curly braces.
- To create an object of a class, the class name is used followed by the object name and an optional initialization list.
- To access the data members and member functions of an object, the dot operator (.) is used followed by the name of the member.
- A class can have different types of access specifiers for its members: public, private, and protected. Public members can be accessed by anyone, private members can only be accessed by the class itself and its friends, and protected members can be accessed by the class itself, its friends, and its derived classes.
- A class can also have static members, which are shared by all the objects of the class and belong to the class itself. Static members are declared with the keyword `static` and can be accessed using the class name and the scope resolution operator (::).
- A class can also have constructors and destructors, which are special member functions that are invoked when an object is created or destroyed. Constructors have the same name as the class and can have parameters to initialize the data members. Destructors have the same name as the class preceded by a tilde (~) and do not have any parameters or return values.

Here is an example of a class and an object in C++:

```cpp
// Define a class called Rectangle
class Rectangle {
    // Declare private data members
    private:
        int length;
        int width;
    // Declare public member functions
    public:
        // Define a constructor with parameters
        Rectangle(int l, int w) {
            length = l;
            width = w;
        }
        // Define a member function to calculate the area
        int area() {
            return length * width;
        }
        // Define a member function to calculate the perimeter
        int perimeter() {
            return 2 * (length + width);
        }
        // Define a destructor
        ~Rectangle() {
            cout << "Rectangle object destroyed" << endl;
        }
};

// Create an object of the class Rectangle
Rectangle r1(10, 5); // Invoke the constructor with arguments 10 and 5
// Access the data members and member functions of the object
cout << "Area of r1 = " << r1.area() << endl; // Invoke the area function
cout << "Perimeter of r1 = " << r1.perimeter() << endl; // Invoke the perimeter function
// The object r1 will be destroyed at the end of the scope and the destructor will be invoked
```