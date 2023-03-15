### Friend Functions

- A friend function is a function that is not a member of a class, but can access the private and protected members of the class  .
- A friend function is declared using the `friend` keyword inside the class definition   .
- A friend function can be declared anywhere in the class, either in the public, private, or protected section .
- A friend function can be called like a normal function, without using any object of the class .
- A friend function can be a global function, a member function of another class, or a template function  .
- A friend function can be declared as a friend of more than one class .
- A friend function can access the non-static members of the class through the objects passed as arguments .
- A friend function does not affect the encapsulation of the class, as it is explicitly declared as a friend by the class  .