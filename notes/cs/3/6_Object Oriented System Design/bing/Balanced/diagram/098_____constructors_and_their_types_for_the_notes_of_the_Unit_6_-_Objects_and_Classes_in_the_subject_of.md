### Constructors and their types

- A constructor is a special method of a class or structure in object-oriented programming that initializes a newly created object of that type.
- Whenever an object is created, the constructor is called automatically.
- A constructor has the same name as the class or structure and does not have a return type.
- A constructor can have parameters to set the initial values of the object's properties or fields.
- There are different types of constructors depending on the number and type of parameters, the source of the object's data, and the inheritance relationship between classes .
- Some of the common types of constructors are:

  - Default constructor: A constructor that does not take any argument and has no parameters. It sets the default values for the object's properties or fields.
  - Parameterized constructor: A constructor that takes one or more arguments and has parameters that match the arguments. It sets the initial values for the object's properties or fields based on the arguments.
  - Copy constructor: A constructor that takes another object of the same type as an argument and has a parameter that is a reference to that object. It copies the values of the object's properties or fields from the argument object.
  - Conversion constructor: A constructor that takes an object of a different type as an argument and has a parameter that is a reference to that object. It converts the values of the object's properties or fields from the argument object to the new object's type.
  - Move constructor: A constructor that takes an object of the same type as an argument and has a parameter that is a rvalue reference to that object. It moves the values of the object's properties or fields from the argument object to the new object, leaving the argument object in an unspecified state.

- A derived class constructor must initialize the derived class, and provide instructions on how to initialize the base class object included in the derived class.
- A derived class constructor can call the base class constructor using the `super` keyword in some languages, such as Java and C#, or the base class name in some languages, such as C++ .
- A derived class constructor can also override the base class constructor if it has the same signature (name and parameters) as the base class constructor.