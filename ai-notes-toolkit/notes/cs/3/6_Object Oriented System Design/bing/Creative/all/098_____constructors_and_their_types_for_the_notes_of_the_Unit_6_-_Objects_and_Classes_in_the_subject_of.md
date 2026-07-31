# Constructors and their types

- A constructor is a special method of a class or structure in object-oriented programming that initializes a newly created object of that type.
- Whenever an object is created, the constructor is called automatically.
- A constructor has the same name as the class or structure and does not have a return type .
- A constructor can be overloaded, meaning that a class or structure can have multiple constructors with different parameters .
- There are different types of constructors depending on the parameters, functionality and purpose  . Some of the common types are:

  - **Default constructor**: A default constructor is the constructor that does not take any argument. It has no parameters. It is used to assign default values to the data members of the object.
  - **Parameterized constructor**: A parameterized constructor is the constructor that takes one or more arguments. It has parameters. It is used to assign specific values to the data members of the object based on the arguments passed.
  - **Copy constructor**: A copy constructor is the constructor that takes another object of the same class or structure as an argument. It has a reference parameter. It is used to create a copy of the existing object with the same values of the data members.
  - **Conversion constructor**: A conversion constructor is the constructor that takes an object of a different class or structure as an argument. It has a reference or value parameter. It is used to convert one type of object to another type of object.
  - **Move constructor**: A move constructor is the constructor that takes an rvalue reference to another object of the same class or structure as an argument. It has an rvalue reference parameter. It is used to transfer the ownership of the resources of the existing object to the new object, without copying or allocating them.
  - **Static constructor**: A static constructor is the constructor that does not take any argument. It has no parameters. It is used to initialize the static data members of the class or structure only once, before any object is created.

- A constructor can also be inherited, meaning that a derived class or structure can use the constructor of the base class or structure to initialize its own data members and the inherited data members.
- A constructor can also be invoked explicitly, meaning that the object can call the constructor of the class or structure using the new operator or the name of the constructor .