### Namespace

- A namespace is a declarative region that provides a scope to the identifiers (the names of types, functions, variables, etc) inside it.
- Namespaces are used to organize code into logical groups and to prevent name collisions that can occur especially when your code base includes multiple libraries.
- A namespace definition begins with the keyword `namespace` followed by the namespace name as follows: `namespace namespace_name { /* code declarations */ }`
- The namespace definition must be placed before any function or variable definition in the code.
- Once a namespace is defined, you can use its members using the scope resolution operator `::`.
- You can also use the `using` directive to bring all the members of a namespace into the current scope, or the `using` declaration to bring a single member into the current scope.
- It is possible to define nested namespaces, where one namespace is defined inside another namespace.
- It is also possible to split the definition of a namespace over multiple files or translation units.
- The `std` namespace is the standard namespace, which contains all the standard C++ library functions and objects.
- It is recommended to avoid using the `using` directive for the `std` namespace in header files, as it can cause name collisions when the header file is included in multiple source files.