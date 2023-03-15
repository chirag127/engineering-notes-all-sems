### Friend Functions

A friend function is a function that is not a member of a class but has access to the class's private and protected members. Friend functions are declared inside the class with the `friend` keyword, but their definitions are outside the class, just like regular functions.

Here are some key points to remember about friend functions:

1. Friend functions are not members of the class, so they do not have access to the `this` pointer of the class.
2. Friend functions can be declared in the private or public sections of the class, but this does not affect their access to the class's members.
3. A friend function can be a friend to more than one class.
4. Friend functions can be useful when we want to allow a non-member function to access the private or protected members of a class.
5. Since friend functions are not members of the class, they cannot be called using the dot `.` or arrow `->` operators on an object of the class.

Here is an example of a friend function:

```c++
#include <iostream>
using namespace std;

class Box {
   private:
      double width;
   public:
      friend void printWidth(Box box);
      void setWidth(double wid);
};

void Box::setWidth(double wid) {
   width = wid;
}

void printWidth(Box box) {
   cout << "Width of box: " << box.width << endl;
}

int main() {
   Box box;
   box.setWidth(10.0);
   printWidth(box);
   return 0;
}
```

In this example, the `printWidth` function is a friend of the `Box` class and can access its private member `width`. The function is declared inside the class with the `friend` keyword, but its definition is outside the class.