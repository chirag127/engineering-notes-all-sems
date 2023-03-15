# Namespace

- A namespace is a feature of C++ that allows grouping of declarations under a name that helps to avoid name collisions.
- A namespace can contain variables, functions, classes, structures, enumerations, and other namespaces.
- The syntax for declaring a namespace is:

```cpp
namespace name {
  // declarations
}
```

- To access a member of a namespace, the scope resolution operator (::) is used.

```cpp
name::member
```

- Alternatively, the using directive can be used to introduce the entire namespace or a specific member into the current scope.

```cpp
using namespace name; // for the whole namespace
using name::member; // for a specific member
```

- The using directive should be used with caution, as it may cause name conflicts with other declarations in the current scope.
- The standard library of C++ is contained in the namespace std. To use the standard library, the header files should be included and the namespace std should be referenced.

```cpp
#include <iostream>
using namespace std;

int main() {
  cout << "Hello, world!" << endl;
  return 0;
}
```

- An unnamed namespace is a namespace that has no name and is only visible in the file where it is declared. It is equivalent to declaring the members as static.

```cpp
namespace {
  // declarations
}
```