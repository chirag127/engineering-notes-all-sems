### Friend Functions

In C++, a friend function is a function that is allowed to access and manipulate private and protected data of a class. Friend functions are not members of the class, but they are declared inside the class definition. 

Some of the important points related to friend functions are:

- A friend function can be a standalone function, or it can be a member function of another class.

- A friend function is declared using the keyword 'friend' followed by the function prototype.

- A friend function can access all the private and protected members of the class it is declared in.

- Friend functions are not inherited, which means that the friend function of a base class will not be a friend of its derived classes.

- Friend functions cannot access the members of the class using the object of that class. They can only access them using the object passed as a parameter.

- Friend functions can be used to implement operators as well. 

- Friend functions can be declared in the public or private section of the class. However, it is a good practice to declare them in the private section to limit their scope.

- Friend functions can also be overloaded like any other function.

- Friend functions are useful when we want to implement a function that needs to access the private or protected members of a class, but we do not want to make those members public.

In conclusion, friend functions are an important concept in C++ that allows us to access private and protected members of a class. They are not members of the class, but they are declared inside the class definition. Friend functions can be used to implement operators and can be overloaded like any other function. It is a good practice to declare them in the private section of the class to limit their scope.