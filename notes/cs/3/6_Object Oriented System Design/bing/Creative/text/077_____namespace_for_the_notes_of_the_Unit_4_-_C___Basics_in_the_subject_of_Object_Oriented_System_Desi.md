### Namespace

- A namespace is a declarative region that provides a scope to the identifiers (names of types, functions, variables, etc) inside it.
- Namespaces are used to organize code into logical groups and to prevent name collisions that can occur especially when your code base includes multiple libraries.
- A namespace definition begins with the keyword `namespace` followed by the namespace name as follows:

```cpp
namespace namespace_name {
   // code declarations
}
```

- The namespace name must be a valid identifier. It can be a single name or a nested name, such as `std::cout`.
- To access the code inside a namespace, you have to use the scope resolution operator `::` as follows:

```cpp
namespace_name::identifier
```

- Alternatively, you can use the `using` directive to introduce the entire namespace or a specific identifier into the current scope, such as:

```cpp
using namespace std; // using the entire std namespace
using std::cout; // using only the cout identifier from the std namespace
```

- However, using the `using` directive can cause name conflicts if the same identifier is declared in more than one namespace. Therefore, it is better to use the scope resolution operator to specify the exact namespace.
- You can also define your own namespaces and nest them inside other namespaces. You can split the definition of a namespace over several units (such as different header files).
- You can also create unnamed namespaces or anonymous namespaces, which are directly usable in the same program and do not need any name. Unnamed namespaces are useful for declaring unique identifiers that are local to a file and do not conflict with the same name in other files. For example:

```cpp
namespace {
   // code declarations
}
```

- You can also use the `using` declaration to introduce a single name from a namespace into the current scope, such as:

```cpp
using std::cout; // using only the cout identifier from the std namespace
```

- This way, you can use the name without the scope resolution operator, but still avoid name conflicts with other namespaces.