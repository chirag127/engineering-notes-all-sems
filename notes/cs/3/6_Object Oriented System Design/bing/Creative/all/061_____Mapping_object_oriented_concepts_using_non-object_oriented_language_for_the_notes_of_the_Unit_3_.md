# Mapping object oriented concepts using non-object oriented language

Object oriented programming (OOP) is a programming paradigm that organizes data and behavior into reusable units called objects. Objects have attributes (data) and methods (functions) that operate on the data. Objects can also interact with other objects through messages.

Non-object oriented languages, such as C, do not have built-in support for objects, but they can still implement some of the basic concepts of OOP using structures, functions, and pointers. Here are some examples of how to map OOP concepts using non-OOP language:

- **Classes and instances**: A class is a blueprint for creating objects of the same type. An instance is a specific object created from a class. In non-OOP languages, we can use structures to define the data fields of a class, and functions to define the methods of a class. For example, in C, we can define a class called `Person` as follows:

```c
// Define a structure to represent a person
struct Person {
  char* name; // data field
  int age; // data field
};

// Define a function to print a person's name and age
void print_person(struct Person* p) {
  printf("Name: %s, Age: %d\n", p->name, p->age); // method
}

// Create an instance of Person
struct Person alice;
alice.name = "Alice";
alice.age = 25;

// Call the print_person function on the instance
print_person(&alice);
```

- **Inheritance and polymorphism**: Inheritance is a mechanism that allows a class to inherit the attributes and methods of another class, called the parent or super class. The inheriting class, called the child or sub class, can also override or extend the inherited behavior. Polymorphism is the ability of an object to behave differently depending on its type or context. In non-OOP languages, we can use pointers and function pointers to simulate inheritance and polymorphism. For example, in C, we can define a class called `Animal` and a sub class called `Dog` as follows:

```c
// Define a structure to represent an animal
struct Animal {
  char* name; // data field
  void (*make_sound)(); // function pointer to represent a method
};

// Define a function to make a generic animal sound
void animal_sound() {
  printf("I am an animal\n");
}

// Define a function to make a dog sound
void dog_sound() {
  printf("Woof woof\n");
}

// Create an instance of Animal
struct Animal a;
a.name = "Animal";
a.make_sound = animal_sound;

// Create an instance of Dog
struct Animal d;
d.name = "Dog";
d.make_sound = dog_sound;

// Call the make_sound function on both instances
a.make_sound(); // prints "I am an animal"
d.make_sound(); // prints "Woof woof"
```

- **Encapsulation and abstraction**: Encapsulation is the principle of hiding the internal details of an object from the outside world, and only exposing a public interface that defines how the object can be used. Abstraction is the process of simplifying a complex system by focusing on the essential features and ignoring the irrelevant details. In non-OOP languages, we can use static variables and functions to achieve encapsulation and abstraction. For example, in C, we can define a module called `Counter` that provides a simple interface for counting, but hides the implementation details from the user:

```c
// Define a static variable to store the count
static int count = 0;

// Define a static function to increment the count
static void increment() {
  count++;
}

// Define a public function to get the current count
int get_count() {
  return count;
}

// Define a public function to reset the count
void reset_count() {
  count = 0;
}

// Use the Counter module
int main() {
  printf("Count: %d\n", get_count()); // prints 0
  increment();
  increment();
  printf("Count: %d\n", get_count()); // prints 2
  reset_count();
  printf("Count: %d\n", get_count()); // prints 0
  return 0;
}
```

These are some of the ways to map object oriented concepts using non-object oriented language. However, these techniques have some limitations and drawbacks, such as:

- They are not as expressive and concise as the native OOP syntax.
- They require manual memory management and error handling.
- They do not support some