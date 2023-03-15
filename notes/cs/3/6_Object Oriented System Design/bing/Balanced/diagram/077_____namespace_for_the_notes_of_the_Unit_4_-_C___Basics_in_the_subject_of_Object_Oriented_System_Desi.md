### Namespace
- A namespace is a declarative region that provides a scope to the identifiers (names of types, functions, variables, etc) inside it.
- Namespaces are used to organize code into logical groups and to prevent name collisions that can occur especially when your code base includes multiple libraries.
- A namespace definition begins with the keyword `namespace` followed by the namespace name as follows:

```cpp
namespace namespace_name {
   // code declarations
}
```

- The namespace name must be a valid identifier and it cannot be a keyword.
- The namespace definition must be placed before any function or variable definition.
- The namespace definition does not terminate with a semicolon unlike other C++ statements.
- You can create nested namespaces by placing one namespace inside another namespace as follows:

```cpp
namespace namespace_name1 {
   // code declarations
   namespace namespace_name2 {
      // code declarations
   }
}
```

- To access the members of a namespace, you have to use the scope resolution operator `::` as follows:

```cpp
namespace_name::member_name
```

- You can also use a `using` directive to introduce an entire namespace or a specific member of a namespace into the current scope as follows:

```cpp
using namespace namespace_name; // for entire namespace
using namespace_name::member_name; // for specific member
```

- A `using` directive tells the compiler to check the specified namespace when resolving names.
- A `using` directive can be placed anywhere in the code, but it is usually placed at the beginning of a file or a function.
- A `using` directive does not create a new scope, it only affects name lookup.
- You can also create an alias for a namespace or a namespace member by using the `using` declaration as follows:

```cpp
using new_name = namespace_name; // for namespace
using new_name = namespace_name::member_name; // for member
```

- A `using` declaration creates a synonym for the namespace or the member and can be used to shorten long names or avoid name conflicts.