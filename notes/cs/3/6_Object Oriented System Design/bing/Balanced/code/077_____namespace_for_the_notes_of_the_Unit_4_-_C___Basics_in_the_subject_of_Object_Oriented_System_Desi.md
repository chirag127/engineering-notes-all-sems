### Namespace
- A namespace is a declarative region that provides a scope to the identifiers (names of types, functions, variables, etc) inside it.
- Namespaces are used to organize code into logical groups and to prevent name collisions that can occur especially when your code base includes multiple libraries.
- A namespace definition begins with the keyword `namespace` followed by the namespace name as follows:

```cpp
namespace namespace_name {
   // code declarations
}
```

- The namespace name must be a valid identifier. It can be a single word or a sequence of nested names separated by the scope resolution operator `::`.
- To access the code inside a namespace, you have to use the scope resolution operator `::` along with the namespace name as follows:

```cpp
namespace_name::identifier
```

- You can also use a `using` directive to introduce the entire namespace or a specific identifier into the current scope as follows:

```cpp
using namespace namespace_name; // for the entire namespace
using namespace_name::identifier; // for a specific identifier
```

- You can define multiple namespaces with the same name in different parts of the program. They are considered as extensions of the same namespace and their contents are merged.
- You can also define namespaces inside other namespaces, creating nested namespaces. You can access the nested namespaces by using the scope resolution operator `::` for each level of nesting.
- You can also use an alias name for a namespace by using the keyword `namespace` followed by the alias name and an equal sign and the original namespace name as follows:

```cpp
namespace alias_name = original_name;
```

- You can then use the alias name to access the namespace as if it was the original name.