### Protected Members

- Protected members are class members that have the access specifier `protected`.
- Protected members are accessible within the class and its subclasses, but not outside the class.
- Protected members are useful for creating class members that are private to the class, but that can still be inherited and accessed by the derived classes.
- Protected members can also be accessed by friend classes and functions of the class.
- Protected members can be inherited in different ways: public, protected, or private inheritance.
- Public inheritance makes public members of the base class public in the derived class, and the protected members of the base class remain protected in the derived class .
- Protected inheritance makes the public and protected members of the base class protected in the derived class .
- Private inheritance makes the public and protected members of the base class private in the derived class .
- Private members of the base class are always inaccessible to the derived class, regardless of the inheritance type .
- Protected members can be accessed by using the `this` pointer or the same type protected members even if declared in the base or derived class.
- Protected members cannot be accessed by using the reference or pointer of the base class, unless the base class is a friend of the derived class .