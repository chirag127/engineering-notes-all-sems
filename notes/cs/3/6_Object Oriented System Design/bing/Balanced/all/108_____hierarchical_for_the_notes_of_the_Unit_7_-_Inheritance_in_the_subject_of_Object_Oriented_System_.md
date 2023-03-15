# Hierarchical Inheritance

- Hierarchical inheritance is a type of inheritance in which a single class (called the superclass or the base class) is inherited by more than one class (called the subclasses or the derived classes).
- In hierarchical inheritance, the subclasses inherit the common features and behavior of the superclass, but they can also have their own specific features and behavior.
- Hierarchical inheritance can be represented by a tree-like structure, where the superclass is the root node and the subclasses are the child nodes.
- Hierarchical inheritance can be implemented in object-oriented programming languages by using the keyword `extends` (in Java) or `:` (in C++) to indicate the inheritance relationship between the classes.
- For example, consider the following hierarchy of classes:

```
class Animal {
  // common attributes and methods of all animals
}

class Dog extends Animal {
  // specific attributes and methods of dogs
}

class Cat extends Animal {
  // specific attributes and methods of cats
}

class Bird extends Animal {
  // specific attributes and methods of birds
}
```

- In this example, `Animal` is the superclass and `Dog`, `Cat`, and `Bird` are the subclasses. They all inherit the common features of `Animal`, but they also have their own specific features.
- Hierarchical inheritance can be useful for organizing classes into categories and subcategories, and for reusing code and avoiding duplication.