### Mapping object oriented concepts using non-object oriented language

- Object oriented concepts are based on the idea of creating and manipulating objects that have attributes and behaviors.
- Non-object oriented languages are based on the idea of manipulating data and functions that operate on data.
- To map object oriented concepts using non-object oriented language, one has to translate the classes, objects, methods, inheritance, polymorphism and encapsulation into the corresponding data structures, variables, functions, modules and scopes of the target language.
- The steps required to implement a design are:
  - Translate classes into data structures: A class can be represented by a data structure that contains the attributes of the class as fields and the methods of the class as function pointers. For example, in C, one can use a struct to define a class.
  - Translate objects into variables: An object can be represented by a variable that holds an instance of the data structure that defines the class. For example, in C, one can use a pointer to a struct to create an object.
  - Translate methods into functions: A method can be represented by a function that takes the object as an argument and performs some operation on it. For example, in C, one can use a function pointer to call a method.
  - Translate inheritance into modules: Inheritance can be represented by using modules that contain the data structures and functions of the parent class and the child class. For example, in C, one can use a header file to include the parent class and a source file to define the child class.
  - Translate polymorphism into function pointers: Polymorphism can be represented by using function pointers that can point to different functions depending on the type of the object. For example, in C, one can use a function pointer to implement a virtual method.
  - Translate encapsulation into scopes: Encapsulation can be represented by using scopes that limit the access to the data and functions of the class. For example, in C, one can use static variables and functions to hide the implementation details of the class.

: [Mapping object-oriented concepts using non-object-oriented language](https://citizenchoice.in/course/Object-Oriented-System-Design/CHAPTER%203%20:%20Object%20Oriented%20Analysis/Mapping-Object-Oriented-Concepts-using-Non-Object-Oriented-Language)