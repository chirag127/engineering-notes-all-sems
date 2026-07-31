### Friend Functions

- A friend function is a function that is not a member of a class, but can access the private and protected data members of the class  .
- A friend function is declared using the `friend` keyword inside the class definition   .
- A friend function can be defined anywhere in the program, either before or after the class definition  .
- A friend function can be a global function, a member function of another class, or a function template .
- A friend function can access the data members of the class directly, without using the dot (`.`) or arrow (`->`) operators    .
- A friend function can be declared in any access specifier section of the class, such as public, private, or protected    .
- A friend function does not affect the encapsulation of the class, as it is explicitly granted access by the class    .
- A friend function can be a friend of more than one class, and a class can have more than one friend function   .

#### Example of a friend function

```cpp
// A class with a friend function
class Rectangle {
    private:
        int length;
        int width;
    public:
        // Constructor
        Rectangle(int l, int w) {
            length = l;
            width = w;
        }
        // A friend function to calculate the area
        friend int area(Rectangle r);
};

// A global function that can access the private data of Rectangle
int area(Rectangle r) {
    return r.length * r.width;
}

// A main function to test the friend function
int main() {
    // Create a Rectangle object
    Rectangle r(10, 20);
    // Call the friend function
    cout << "The area of the rectangle is " << area(r) << endl;
    return 0;
}
```

Output:

```
The area of the rectangle is 200
```