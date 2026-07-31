# Protected Members in Inheritance

- Inheritance is a mechanism that allows a class to inherit the properties and behaviors of another class. The class that inherits is called the derived class, and the class that is inherited is called the base class.
- Protected members are those members of a class that can be accessed by the class itself and its derived classes, but not by other classes or functions.
- Protected members are declared using the keyword `protected` in the class definition.
- Protected members are useful when we want to restrict the access to some members of a class, but still allow the derived classes to use them.
- The access to protected members depends on the type of inheritance used: public, protected, or private.

## Public Inheritance

- Public inheritance is the most common type of inheritance, where the derived class inherits the public and protected members of the base class as public and protected respectively, and the private members of the base class are inaccessible to the derived class.
- Public inheritance preserves the access specifiers of the base class members in the derived class, and allows the derived class to access the protected members of the base class as its own protected members.
- Public inheritance also allows the objects of the derived class to access the public members of the base class through the derived class object or a pointer or reference to the derived class.
- For example, consider the following classes:

```cpp
class Base {
    private:
        int x;
    protected:
        int y;
    public:
        int z;
};

class Derived: public Base {
    public:
        void show() {
            // x is inaccessible
            // y is accessible as protected
            // z is accessible as public
            cout << "y = " << y << endl;
            cout << "z = " << z << endl;
        }
};
```

- In this example, the class `Derived` inherits the class `Base` as public. The private member `x` of `Base` is inaccessible to `Derived`, the protected member `y` of `Base` is accessible to `Derived` as protected, and the public member `z` of `Base` is accessible to `Derived` as public.
- The function `show()` of `Derived` can access the protected member `y` of `Base` as its own protected member, but cannot access the private member `x` of `Base`.
- The objects of `Derived` can access the public member `z` of `Base` through the object itself or a pointer or reference to `Derived`, but cannot access the protected member `y` of `Base` directly.

## Protected Inheritance

- Protected inheritance is a less common type of inheritance, where the derived class inherits the public and protected members of the base class as protected, and the private members of the base class are inaccessible to the derived class.
- Protected inheritance changes the access specifiers of the public and protected members of the base class to protected in the derived class, and allows the derived class to access the protected members of the base class as its own protected members.
- Protected inheritance also prevents the objects of the derived class from accessing the public members of the base class through the derived class object or a pointer or reference to the derived class, as they are now protected in the derived class.
- For example, consider the following classes:

```cpp
class Base {
    private:
        int x;
    protected:
        int y;
    public:
        int z;
};

class Derived: protected Base {
    public:
        void show() {
            // x is inaccessible
            // y is accessible as protected
            // z is accessible as protected
            cout << "y = " << y << endl;
            cout << "z = " << z << endl;
        }
};
```

- In this example, the class `Derived` inherits the class `Base` as protected. The private member `x` of `Base` is inaccessible to `Derived`, the protected member `y` of `Base` is accessible to `Derived` as protected, and the public member `z` of `Base` is also accessible to `Derived` as protected.
- The function `show()` of `Derived` can access the protected members `y` and `z` of `Base` as its own protected members, but cannot access the private member `x` of `Base`.
- The objects of `Derived` cannot access the public member `z` of `Base` through the object itself or a pointer or reference to `Derived`, as it is now protected in `Derived`.

## Private Inheritance

- Private inheritance is the rarest type