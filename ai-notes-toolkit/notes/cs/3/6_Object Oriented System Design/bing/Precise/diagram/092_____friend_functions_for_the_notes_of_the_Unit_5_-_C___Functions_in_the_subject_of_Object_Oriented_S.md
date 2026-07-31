### Unit 5 - C++ Functions: Friend Functions

- A friend function is a function that is not a member of a class but has access to the class's private and protected members.
- Friend functions are declared inside the class with the keyword `friend` preceding the function prototype.
- The friend function is not considered a member function of the class, so it cannot be called using the dot operator on an object of the class.
- The friend function can be called like a normal function, without the need for an object of the class.
- Friend functions can be useful when two or more classes need to share data or functionality.
- A common use of friend functions is for overloading operators, where the left operand is not an object of the class.
- Friend functions can also be used to provide a specific interface to the class, without exposing the class's internal implementation.
- It is important to use friend functions judiciously, as they can break the encapsulation of the class.
