### Friend Functions for the Notes of the Unit 5 - C++ Functions in the Subject of Object Oriented System Design

In C++, a friend function is a function that is given permission to access a class's private and protected data. It is declared inside the class, but defined outside the class. In this section, we will discuss the friend functions in detail.

#### Definition of Friend Functions
A friend function is a non-member function that is granted access to the private and protected members of a class. It can be declared in the class definition, but it is defined outside the class definition. A friend function can access the private and protected members of the class, but it is not a member of the class.

#### Syntax of Friend Functions
The syntax of a friend function is as follows:

```
class Class_Name
{
      // declaration of class members
      friend Return_Type Function_Name(Arguments);
};
```

#### Advantages of Friend Functions
- Friend functions can access private and protected data of a class.
- Friend functions can be used to implement operators that are not members of a class.
- Friend functions can be used to access private or protected members of different classes.
- Friend functions can be used to implement functions that need access to private or protected members of a class.

#### Disadvantages of Friend Functions
- Friend functions can violate the encapsulation principle of object-oriented programming.
- Friend functions can make the code more complex and harder to maintain.
- Friend functions can break the modularity of classes.

#### Examples of Friend Functions
Below is an example of a friend function:

```
class Class_Name
{
    private:
        int x;
    public:
        Class_Name(int a)
        {
            x = a;
        }
        friend int Function_Name(Class_Name obj);
};
 
int Function_Name(Class_Name obj)
{
    return obj.x;
}
```

#### Applications of Friend Functions
- Friend functions can be used to implement operators that are not members of a class.
- Friend functions can be used to access private or protected members of different classes.
- Friend functions can be used to implement functions that need access to private or protected members of a class.

In conclusion, friend functions are an important concept in C++ programming. They provide a way to access private and protected data of a class from outside the class without violating the encapsulation principle of object-oriented programming. However, they should be used carefully to avoid making the code more complex and harder to maintain.