### Friend Functions in C++

- A friend function is a function that is declared using the `friend` keyword inside the body of a class  .
- A friend function can access the private and protected data members of the class, as well as the public ones    .
- A friend function is not a member function of the class, and it does not inherit the access privileges of the class  .
- A friend function can be defined anywhere in the program, either before or after the class definition   .
- A friend function can be a global function, a member function of another class, or a function template  .
- A friend function can be declared in any section of the class (private, protected, or public), but it does not affect its access level   .
- A friend function can be declared multiple times in the same or different classes, but it can be defined only once  .
- A friend function can have default arguments, but they must be specified in the first declaration of the function  .
- A friend function can be overloaded, but it cannot be overridden  .
- A friend function can be used to implement operator overloading, as it can access the private data of the operands  .
- A friend function can be used to implement input/output operations for a class, as it can access the private data of the object  .