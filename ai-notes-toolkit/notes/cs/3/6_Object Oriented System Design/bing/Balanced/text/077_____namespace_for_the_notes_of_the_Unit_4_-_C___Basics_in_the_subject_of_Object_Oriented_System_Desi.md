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

- However, using too many `using` directives can defeat the purpose of namespaces and cause name conflicts. It is better to use them sparingly and only for specific identifiers.
- You can also define your own aliases for namespaces or identifiers using the `namespace` keyword and an assignment operator `=`. For example:

```cpp
namespace ns = some_very_long_namespace_name; // creates an alias for a namespace
namespace UI = UserInterface; // creates an alias for a nested namespace
using Vec = std::vector<int>; // creates an alias for a type
```

- You can define namespaces in any scope, including global, local, and nested. You can also split the definition of a namespace over several units (such as different files or functions). For example:

```cpp
// file1.cpp
namespace A {
   void foo();
}

// file2.cpp
namespace A {
   void bar();
}

// main.cpp
#include "file1.cpp"
#include "file2.cpp"
int main() {
   A::foo();
   A::bar();
}
```

- The above code defines the namespace A in two different files, but they are treated as one namespace in the main file. This allows you to group related code across different units.
- You can also create unnamed namespaces, which are local to the unit they are defined in. They are equivalent to declaring the identifiers inside them as `static`. For example:

```cpp
// file1.cpp
namespace {
   int x; // x is local to file1.cpp
   void foo() {
      x = 10;
   }
}

// file2.cpp
namespace {
   int x; // x is local to file2.cpp
   void bar() {
      x = 20;
   }
}

// main.cpp
#include "file1.cpp"
#include "file2.cpp"
int main() {
   foo();
   bar();
   cout << x; // error: x is not declared in this scope
}
```

- The above code defines two unnamed namespaces in two different files, but they are not visible to each other or to the main file. This prevents name conflicts and ensures encapsulation.