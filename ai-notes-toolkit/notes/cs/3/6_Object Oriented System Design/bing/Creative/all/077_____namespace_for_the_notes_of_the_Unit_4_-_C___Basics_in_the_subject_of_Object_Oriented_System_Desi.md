# Namespace

- A namespace is a declarative region that provides a scope to the identifiers (names of types, functions, variables, etc) inside it.
- Namespaces are used to organize code into logical groups and to prevent name collisions that can occur especially when your code base includes multiple libraries.
- A namespace definition begins with the keyword `namespace` followed by the namespace name as follows:

```cpp
namespace namespace_name {
   // code declarations
}
```

- The namespace name must be a valid identifier. It can be a single word or a sequence of nested names separated by the scope resolution operator `::`.
- The namespace definition must be placed before any function, variable or type it is used in.
- The namespace definition does not terminate with a semicolon unlike other C++ statements.
- You can create aliases for your namespaces with the `namespace` keyword as follows:

```cpp
namespace new_name = current_name;
```

- You can access the members of a namespace by using the scope resolution operator `::` as follows:

```cpp
namespace_name::member_name;
```

- You can also access the members of a namespace by using the `using` directive as follows:

```cpp
using namespace namespace_name;
```

- This allows you to use the members of the namespace without the scope resolution operator. However, this can also create name conflicts if the same name is defined in more than one namespace.
- You can also use the `using` declaration to access a single member of a namespace as follows:

```cpp
using namespace_name::member_name;
```

- This allows you to use the member name without the scope resolution operator. However, this can also create name conflicts if the same name is defined in more than one namespace or in the global scope.
- You can define a namespace in multiple parts and in multiple files. The compiler will treat them as a single namespace. For example:

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
using namespace A;
int main() {
   foo();
   bar();
   return 0;
}
```

- You can also nest namespaces within one another. The inner namespaces are accessed using the scope resolution operator `::` as follows:

```cpp
namespace A {
   namespace B {
      namespace C {
         int x;
      }
   }
}

// access x as A::B::C::x
```

- You can also create unnamed namespaces or anonymous namespaces. These are directly usable in the same file and are used for declaring unique identifiers that avoid linkage conflicts. For example:

```cpp
namespace {
   int x; // unique to this file
}

// access x as x
```