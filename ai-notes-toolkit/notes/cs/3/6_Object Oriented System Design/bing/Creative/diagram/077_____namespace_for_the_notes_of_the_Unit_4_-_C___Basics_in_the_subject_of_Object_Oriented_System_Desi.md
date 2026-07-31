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

- You can also use a `using` directive to introduce the entire namespace or specific identifiers into the current scope, so that you don't have to use the scope resolution operator every time. For example:

```cpp
using namespace std; // introduces the entire std namespace
using std::cout; // introduces only the cout identifier
```

- However, using too many `using` directives can defeat the purpose of namespaces and lead to name conflicts. It is better to use them sparingly and only for specific identifiers.
- You can also define aliases for namespaces or identifiers using the `namespace` keyword as follows:

```cpp
namespace new_name = current_name; // for namespaces
namespace std_lib = std; // example
namespace new_name = current_name::identifier; // for identifiers
namespace io = std::ios; // example
```

- You can define namespaces in any scope, including global, local, or nested inside other namespaces. You can also split the definition of a namespace over several units (such as different files or functions), as long as the name and the content are consistent. For example:

```cpp
// file1.cpp
namespace A {
   void func1();
   void func2();
}

// file2.cpp
namespace A {
   void func3();
   void func4();
}
```

- Both files will contribute to the same namespace A, and the final namespace will contain all the four functions. This feature allows you to group related code that may be distributed over different files or libraries.