### Mapping object oriented concepts using non-object oriented language

- Object oriented concepts are based on the idea of creating and manipulating objects that have attributes and behaviors.
- Non-object oriented languages are based on the idea of manipulating data and functions that operate on data.
- To map object oriented concepts using non-object oriented language, one needs to translate the classes, objects, methods, inheritance, and polymorphism into the corresponding data structures, variables, functions, and control structures of the target language.
- The steps required to implement a design are:

  - Translate classes into data structures: A class can be represented by a data structure that contains the attributes of the class as fields and the methods of the class as function pointers. For example, in C, one can use a struct to define a class.
  - Translate objects into variables: An object can be represented by a variable that holds an instance of the data structure that defines the class. For example, in C, one can use a pointer to a struct to create an object.
  - Translate methods into functions: A method can be represented by a function that takes the object as an argument and performs some operation on it. For example, in C, one can use a function pointer to call a method.
  - Translate inheritance into composition: Inheritance can be represented by composition, which means that a subclass can contain an instance of the superclass as a field and delegate some operations to it. For example, in C, one can use a struct to define a subclass that has a field of the type of the superclass.
  - Translate polymorphism into conditional statements: Polymorphism can be represented by conditional statements that check the type of the object and call the appropriate function based on the type. For example, in C, one can use a switch statement to implement polymorphism.

- Some examples of mapping object oriented concepts using non-object oriented language are:

  - C++ class:

    ```cpp
    class Animal {
      public:
        virtual void makeSound() = 0;
    };

    class Dog : public Animal {
      public:
        void makeSound() {
          cout << "Woof" << endl;
        }
    };

    class Cat : public Animal {
      public:
        void makeSound() {
          cout << "Meow" << endl;
        }
    };
    ```

  - C struct and function:

    ```c
    typedef struct Animal {
      void (*makeSound)();
    } Animal;

    void dogSound() {
      printf("Woof\n");
    }

    void catSound() {
      printf("Meow\n");
    }

    Animal* createDog() {
      Animal* dog = (Animal*)malloc(sizeof(Animal));
      dog->makeSound = dogSound;
      return dog;
    }

    Animal* createCat() {
      Animal* cat = (Animal*)malloc(sizeof(Animal));
      cat->makeSound = catSound;
      return cat;
    }
    ```

- Another example of mapping object oriented concepts using non-object oriented language is the Object-Relational Mapping (ORM) tool, which can help and simplify the translation between the objects and the relational database tables. An ORM tool can use class definitions (models) to create, maintain and provide full access to objects’ data and their database persistence. For example, in Python, one can use SQLAlchemy as an ORM tool to map Python classes to SQL tables.