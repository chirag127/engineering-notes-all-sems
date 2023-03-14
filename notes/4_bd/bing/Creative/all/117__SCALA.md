### SCALA

- Scala is a general-purpose, high-level, multi-paradigm programming language that supports both object-oriented programming and functional programming  .
- Scala is designed to be concise, expressive, and interoperable with Java . It can run on the Java virtual machine (JVM), JavaScript, or LLVM platforms .
- Scala was created by Martin Odersky and first released in 2004 . It is influenced by languages such as Java, Haskell, OCaml, Scheme, and others.
- Scala has many features that make it a powerful and versatile language, such as:

  - Syntactic flexibility: Scala allows multiple ways to write the same code, such as using infix notation, dot notation, or parentheses. It also has a concise syntax for defining classes, functions, and values.
  - Unified type system: Scala has a single root type called `Any`, from which all other types inherit. It also has a bottom type called `Nothing`, which is a subtype of every type. Scala supports both primitive types and reference types, and allows user-defined types to extend existing types .
  - For-expressions: Scala has a powerful construct called `for` that can iterate over collections, generate new collections, filter elements, and perform other operations in a declarative way .
  - Functional tendencies: Scala supports many features of functional programming, such as:

    - Everything is an expression: Scala does not have statements, only expressions that return values. This allows code to be more concise and expressive .
    - Type inference: Scala can infer the types of variables, parameters, and return values based on the context, reducing the need for explicit type annotations .
    - Anonymous functions: Scala allows defining and passing functions without giving them names, using the `=>` syntax. These functions can capture variables from the enclosing scope, creating closures .
    - Immutability: Scala encourages the use of immutable data structures and values, which are safer and easier to reason about than mutable ones. Scala provides many immutable collections, such as `List`, `Set`, and `Map`, as well as case classes, which are immutable by default .
    - Lazy (non-strict) evaluation: Scala allows defining values and functions that are only evaluated when needed, using the `lazy` keyword or the `by-name` parameter syntax. This can improve performance and avoid unnecessary computations .
    - Tail recursion: Scala supports tail recursion optimization, which means that recursive functions that call themselves as the last action can be converted to loops, avoiding stack overflow errors .
    - Case classes and pattern matching: Scala allows defining classes that have a predefined `equals`, `hashCode`, `toString`, and `copy` methods, as well as a companion object with an `apply` and `unapply` method. These classes are called case classes, and they can be used with pattern matching, which is a powerful way to deconstruct and process data based on its shape .
    - Partial functions: Scala allows defining functions that are only defined for a subset of the input domain, using the `case` syntax. These functions can be composed, lifted, or collected to create new functions .

  - Object-oriented extensions: Scala supports many features of object-oriented programming, such as:

    - Classes and objects: Scala allows defining classes that can have fields, methods, constructors, and inheritance. Scala also allows defining singleton objects that can have fields and methods, but no instances. Objects can be used as modules, factories, or companions for classes .
    - Traits: Scala allows defining traits, which are similar to interfaces, but can also have fields and methods. Traits can be mixed in with classes and objects, providing multiple inheritance and mixin composition .
    - Abstract types and generics: Scala allows defining abstract types and generic types, which are types that depend on other types. Abstract types are defined inside traits or classes, and can be overridden by subclasses. Generic types are defined using type parameters, and can be constrained by bounds or variance annotations[^