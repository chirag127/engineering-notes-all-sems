### Friend Functions

A friend function is a function that is not a member of a class but has access to the class's private and protected members. Friend functions are declared inside the class with the `friend` keyword, but their definitions are outside the class, just like regular functions.

Here are some key points to remember about friend functions:

1. Friend functions are not members of the class, so they do not have access to the `this` pointer of the class.
2. Friend functions can be declared in the private or public sections of the class, but this does not affect their access to the class's members.
3. A friend function can be a friend to more than one class.
4. Friend functions can be used to implement operator overloading for classes.
5. Since friend functions are not members of the class, they cannot be called using the dot `.` or arrow `->` operators.

In summary, friend functions provide a way for non-member functions to access the private and protected members of a class. This can be useful in certain situations, such as when implementing operator overloading for classes. However, it is important to use friend functions judiciously, as they can break the encapsulation of the class.