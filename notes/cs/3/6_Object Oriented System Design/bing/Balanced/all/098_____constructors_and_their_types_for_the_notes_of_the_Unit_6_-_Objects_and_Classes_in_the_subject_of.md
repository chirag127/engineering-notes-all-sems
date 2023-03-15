# Constructors and their types

- A constructor is a special method of a class or structure in object-oriented programming that initializes a newly created object of that type.
- Whenever an object is created, the constructor is called automatically.
- A constructor has the same name as the class or structure and does not have a return type.
- A constructor can have parameters to set the initial values of the object's attributes.
- A constructor can also perform other tasks, such as allocating memory, opening files, or validating input.

## Types of constructors

- There are different types of constructors depending on the number and type of parameters, the source of the object's data, and the language-specific syntax  .
- Some common types of constructors are:

  - **Default constructor**: A default constructor is the constructor that does not take any argument. It has no parameters. It sets the default values for the object's attributes, such as zero, null, or empty.
  - **Parameterized constructor**: A parameterized constructor is the constructor that takes one or more arguments to initialize the object's attributes. It can have different signatures depending on the number and type of parameters.
  - **Copy constructor**: A copy constructor is the constructor that takes another object of the same class as an argument and copies its data to the new object. It is used to create a duplicate or clone of an existing object.
  - **Conversion constructor**: A conversion constructor is the constructor that takes an object of a different class as an argument and converts its data to the new object's class. It is used to create an object of one class from an object of another class.
  - **Move constructor**: A move constructor is the constructor that takes an rvalue reference to another object of the same class as an argument and moves its data to the new object. It is used to optimize the performance and avoid unnecessary copying of temporary objects.

- Some languages may have other types of constructors, such as static constructors, which are executed only once when the class is loaded, or default constructors with optional parameters, which can be called with or without arguments .