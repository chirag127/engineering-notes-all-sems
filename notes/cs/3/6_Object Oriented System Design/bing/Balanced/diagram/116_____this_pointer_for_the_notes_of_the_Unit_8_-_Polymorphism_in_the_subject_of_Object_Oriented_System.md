### This pointer

- This pointer is a special pointer that points to the current object of a class.
- This pointer is implicitly passed as a hidden argument to every member function of a class.
- This pointer is useful for accessing the data members and member functions of the current object.
- This pointer is also used to resolve the scope resolution operator (::) when there is a global variable with the same name as a data member of the class.
- This pointer can be used to return the current object from a member function.
- This pointer can be used to implement cascading of function calls on the same object.
- This pointer cannot be modified, as it is a constant pointer.
- This pointer is of the same type as the class, i.e., if the class name is X, then the type of this pointer is X*.

#### Example of this pointer

```cpp
// A simple example of this pointer
#include <iostream>
using namespace std;

class Test
{
private:
    int x;
    int y;
public:
    Test(int x = 0, int y = 0) { this->x = x; this->y = y; }
    Test &setX(int a) { x = a; return *this; }
    Test &setY(int b) { y = b; return *this; }
    void print() { cout << "x = " << x << " y = " << y << endl; }
};

int main()
{
    Test obj1(5, 5);

    // Chained function calls.  All calls modify the same object
    // as the same object is returned by reference
    obj1.setX(10).setY(20).print();
    return 0;
}
```

Output:

```
x = 10 y = 20
```