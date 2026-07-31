### This pointer

- The `this` pointer is a special pointer that points to the current object of a class.
- The `this` pointer is implicitly passed as a hidden argument to every non-static member function of a class.
- The `this` pointer can be used to access the data members and member functions of the current object.
- The `this` pointer can also be used to return a reference to the current object from a member function.
- The `this` pointer is useful for implementing cascaded function calls, operator overloading, and self-referential classes.

#### Example of using `this` pointer to access data members and member functions

```cpp
// A simple class with a constructor
class Point {
private:
    int x, y;

public:
    // Constructor that uses the this pointer to initialize the object
    Point(int x, int y)
    {
        this->x = x;
        this->y = y;
    }

    // A member function that prints the coordinates of the point
    void print()
    {
        std::cout << "Point: (" << this->x << ", " << this->y << ")\n";
    }
};

// Driver code
int main()
{
    // Create a point object and call its print function
    Point p(10, 20);
    p.print();
    return 0;
}
```

#### Output

```
Point: (10, 20)
```

#### Example of using `this` pointer to return a reference to the current object

```cpp
// A class that implements a simple counter
class Counter {
private:
    int count;

public:
    // Constructor that initializes the count to zero
    Counter()
    {
        count = 0;
    }

    // A member function that increments the count and returns the current object
    Counter& increment()
    {
        count++;
        return *this;
    }

    // A member function that prints the count
    void print()
    {
        std::cout << "Count: " << count << "\n";
    }
};

// Driver code
int main()
{
    // Create a counter object and call its increment function multiple times
    Counter c;
    c.increment().increment().increment().print();
    return 0;
}
```

#### Output

```
Count: 3
```