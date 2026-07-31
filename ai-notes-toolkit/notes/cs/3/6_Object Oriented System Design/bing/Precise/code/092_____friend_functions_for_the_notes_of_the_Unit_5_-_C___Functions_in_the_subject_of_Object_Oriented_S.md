### Friend Functions

A friend function is a function that is not a member of a class but has access to the class's private and protected members. Friend functions are declared inside the class with the `friend` keyword, but their definitions are outside the class, like any other function.

Here are some key points to remember about friend functions:

1. Friend functions are not members of the class, so they do not have access to the `this` pointer of the class.
2. Friend functions can be declared in the private or public sections of the class, but this does not affect their access to the class's members.
3. A friend function can be a friend to more than one class.
4. Friend functions can be useful when we want to allow a non-member function to access the private or protected members of a class.
5. Since friend functions are not members of the class, they cannot be called using the dot `.` or arrow `->` operators on an object of the class.

Here is an example of a friend function:

```c++
class MyClass {
private:
    int x;
public:
    MyClass(int val) : x(val) {}
    friend void printX(MyClass obj);
};

void printX(MyClass obj) {
    std::cout << obj.x << std::endl;
}

int main() {
    MyClass obj(10);
    printX(obj);
    return 0;
}
```

In this example, the `printX` function is a friend of the `MyClass` class and has access to its private member `x`. The function is defined outside the class and can be called like any other function, without using the dot `.` or arrow `->` operators on an object of the class.