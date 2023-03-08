 Here is the content in markdown format for the topic ### virtual functions for the notes of the Unit 5 - C++ Functions in the subject of Object Oriented System Design:

### Virtual Functions

- Virtual functions are functions in a base class that are overridden in a derived class.
- A virtual function defines the interface, i.e., the signature of the function, but leaves the implementation details to the derived class.
- The derived class overrides the base class virtual function and provides its own implementation.
- This allows polymorphism where a call to a member function will cause a different function to be executed depending on the type of object that invokes the function.
- To make a function virtual, simply add the keyword `virtual` before the function declaration in the base class. For example:
    ```C++
    class Animal {
    public:
        virtual void makeSound() {
            // base class implementation
        }
        // ...
    };
    ```
- When a virtual function is called, the version of the function that is called depends on the type of the object through which the function is called, not the type of the pointer or reference.
- This is known as runtime polymorphism and allows us to invoke derived class versions of a function through base class pointers and references.
- For example:
    ```C++
    Animal *a = new Dog(); // a points to a Dog
    a->makeSound(); // calls Dog::makeSound()
    ```
- If `makeSound()` was not declared `virtual` in the `Animal` base class, then `Animal::makeSound()` would always be called, even if the object was of type `Dog`.
- A derived class can provide a definition for a virtual function to override the base class definition:
    ```C++
    class Dog : public Animal {
    public:
        void makeSound() {
            // derived class implementation
        }
        // ...
    };
    ```
- When overriding, the derived class function must have the same return type and parameters as the base class virtual function. It can also extend the base class implementation instead of fully overriding it, using the `override` keyword to indicate that the function is intended to override a base class virtual function.
- Advantages:
    - Achieves polymorphism.
    - Enables functions to be overridden in derived classes.
    - Implementation is left to the derived classes.
    - Late binding is achieved.
- Disadvantages:
    - There is overhead in calling virtual functions.
    - The compiler needs to ensure the correct function is called at runtime, which is slower than regular function calls.