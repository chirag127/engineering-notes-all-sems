### Namespace in C++

A namespace is a mechanism in C++ that allows us to group a set of identifiers (such as variables, functions, and classes) under a name. This helps to avoid naming conflicts between different parts of a program.

#### Syntax

The syntax for declaring a namespace is as follows:

```cpp
namespace namespace_name {
  // declarations
}
```

#### Accessing Namespace Members

To access the members of a namespace, we can use the scope resolution operator `::`. For example:

```cpp
namespace MyNamespace {
  int x;
}

MyNamespace::x = 5;
```

#### Nested Namespace

We can nest namespaces within other namespaces to create a hierarchical namespace structure. For example:

```cpp
namespace MyNamespace {
  namespace InnerNamespace {
    int x;
  }
}

MyNamespace::InnerNamespace::x = 5;
```

#### Using Directive

We can use the `using` directive to bring all the members of a namespace into the current scope. For example:

```cpp
#include <iostream>

namespace MyNamespace {
  int x;
}

using namespace MyNamespace;

int main() {
  x = 5;
  std::cout << x << std::endl;
  return 0;
}
```

#### Using Declaration

We can use the `using` declaration to bring specific members of a namespace into the current scope. For example:

```cpp
#include <iostream>

namespace MyNamespace {
  int x;
  void foo();
}

using MyNamespace::x;
using MyNamespace::foo;

int main() {
  x = 5;
  foo();
  return 0;
}
```

#### Conclusion

In conclusion, namespaces are an important feature of C++ that allows us to organize our code and avoid naming conflicts. By using namespaces, we can create more modular and maintainable programs.