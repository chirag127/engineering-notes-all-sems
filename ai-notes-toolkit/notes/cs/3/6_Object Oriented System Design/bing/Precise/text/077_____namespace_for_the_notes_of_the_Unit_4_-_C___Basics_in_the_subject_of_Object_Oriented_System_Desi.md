### Namespace

- A namespace is a declarative region that provides a scope to the identifiers (names of types, functions, variables, etc) inside it.
- Namespaces are used to organize code into logical groups and to prevent name collisions that can occur especially when your code base includes multiple libraries.
- A namespace definition begins with the keyword `namespace` followed by the namespace name and a pair of curly braces `{}` that encloses the declarations and definitions of the namespace.
- The `using` directive can be used to introduce an entire namespace or individual members of a namespace into the current scope.
- The `using` declaration can be used to introduce a single member of a namespace into the current scope.
- The `std` namespace is the standard namespace, which contains the definitions of the C++ Standard Library.
- The `::` operator is used to access members of a namespace. For example, `std::cout` refers to the `cout` object in the `std` namespace.
- Namespaces can be nested, meaning that one namespace can be defined inside another namespace.
- Namespace aliases can be used to create a shorter or more meaningful name for a namespace. For example, `namespace fs = std::filesystem;` creates an alias `fs` for the `std::filesystem` namespace.