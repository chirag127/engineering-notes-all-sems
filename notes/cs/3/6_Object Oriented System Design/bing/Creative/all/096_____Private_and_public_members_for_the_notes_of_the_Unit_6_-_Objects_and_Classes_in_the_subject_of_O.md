# Private and public members

- In object-oriented system design, a class is a blueprint for creating objects that have certain properties and behaviors.
- A class can have members, which are the attributes (data) and operations (functions) that belong to the class.
- Members can have different levels of access, which determine who can use them and how.
- The two most common levels of access are public and private.
- Public members are visible and accessible from anywhere in the system. They can be used by any object or class that has a reference to the class that defines them.
- Private members are hidden and accessible only from within the class that defines them. They cannot be used by any other object or class, even if they have a reference to the class that defines them.
- Public and private members are indicated by symbols in the class diagram. A public member is prefixed by the symbol ‘+’, while a private member is prefixed by the symbol ‘−’  .
- For example, consider the following class diagram of a Person class:

![Person class diagram](https://www.tutorialspoint.com/object_oriented_analysis_design/images/ooad_uml_basic_notation.jpg)

- The Person class has four attributes: name, age, gender, and address. The name and age attributes are public, while the gender and address attributes are private. This means that any object or class can access the name and age of a Person object, but only the Person object itself can access its gender and address.
- The Person class also has four operations: getName, getAge, getGender, and getAddress. The getName and getAge operations are public, while the getGender and getAddress operations are private. This means that any object or class can call the getName and getAge operations of a Person object, but only the Person object itself can call its getGender and getAddress operations.
- The purpose of using public and private members is to enforce the principle of data hiding, which is one of the important features of object-oriented programming. Data hiding allows preventing the functions of a program to access directly the internal representation of a class type. It also helps to maintain the integrity and consistency of the data, and to avoid unwanted interference or modification by other parts of the system.