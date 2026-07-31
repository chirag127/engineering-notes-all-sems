### this pointer

- The `this` pointer is a special pointer that points to the current object of a class.
- The `this` pointer is implicitly passed as a hidden argument to every member function of a class.
- The `this` pointer can be used to access the data members and member functions of the current object.
- The `this` pointer can also be used to return a reference to the current object from a member function.
- The `this` pointer is useful for implementing chaining of member function calls, resolving name conflicts between data members and parameters, and implementing self-referential classes .

#### Example of using `this` pointer

```cpp
// A simple class with a constructor
class Point {
private:
    int x, y;

public:
    // Constructor
    Point(int x, int y)
    {
        // The 'this' pointer is used to differentiate
        // between the data member 'x' and the parameter 'x'
        this->x = x;
        this->y = y;
    }

    // A function that returns a reference to the current object
    Point& setX(int x)
    {
        // The 'this' pointer is used to access the current object
        this->x = x;
        // The 'this' pointer is also used to return a reference to the current object
        return *this;
    }

    // A function that prints the coordinates of the point
    void print()
    {
        std::cout << "Point(" << x << ", " << y << ")\n";
    }
};

// Driver code
int main()
{
    // Create a point object
    Point p(10, 20);

    // Print the coordinates
    p.print();

    // Use the 'this' pointer to chain function calls
    p.setX(30).print();

    return 0;
}
```

#### Output

```
Point(10, 20)
Point(30, 20)
```