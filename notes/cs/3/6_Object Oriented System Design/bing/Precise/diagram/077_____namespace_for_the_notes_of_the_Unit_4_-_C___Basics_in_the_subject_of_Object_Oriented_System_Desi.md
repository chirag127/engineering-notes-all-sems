### Namespace
- A namespace is a declarative region that provides a scope to the identifiers (names of the types, function, variables, etc.) inside it.
- Namespaces are used to organize code into logical groups and to prevent name collisions that can occur especially when your codebase includes multiple libraries.
- A namespace definition begins with the keyword `namespace` followed by the namespace name and a pair of curly braces `{}` that encloses the declarations and definitions of the namespace.
- You can define multiple namespaces with the same name. The declarations and definitions in these namespaces are combined into a single namespace.
- You can access the members of a namespace using the scope resolution operator `::`.
- You can also use the `using` directive to bring the members of a namespace into the current scope, making it unnecessary to use the scope resolution operator.
- The `std` namespace is the standard namespace in C++. It contains the definitions of the standard C++ library, including the standard input/output library `iostream`.
- It is generally not recommended to use the `using` directive to bring the entire `std` namespace into the current scope, as it can lead to name collisions. Instead, it is better to use the scope resolution operator to access the members of the `std` namespace, or to use the `using` declaration to bring specific members of the `std` namespace into the current scope.