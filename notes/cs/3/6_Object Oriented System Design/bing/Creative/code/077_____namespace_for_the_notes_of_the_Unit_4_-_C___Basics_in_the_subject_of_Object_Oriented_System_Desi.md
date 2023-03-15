Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of namespace for the Unit 4 - C++ Basics in the subject of Object Oriented System Design.

```markdown
### Namespace
- A namespace is a declarative region that provides a scope to the identifiers (names of types, functions, variables, etc) inside it.
- Namespaces are used to organize code into logical groups and to prevent name collisions that can occur especially when your code base includes multiple libraries.
- A namespace definition begins with the keyword namespace followed by the namespace name as follows:

```cpp
namespace namespace_name {
   // code declarations
}
```

- To access the code inside a namespace, you have to use the scope resolution operator (::) along with the namespace name as follows:

```cpp
namespace_name::code; // access code defined in the namespace
```

- You can also create nested namespaces, where you can define one namespace inside another namespace as follows:

```cpp
namespace namespace1 {
   // code declarations
   namespace namespace2 {
      // code declarations
   }
}
```

- To access the code inside a nested namespace, you have to use the scope resolution operator (::) for each namespace as follows:

```cpp
namespace1::namespace2::code; // access code defined in the nested namespace
```

- You can also use an alias name for a namespace using the keyword namespace as follows:

```cpp
namespace new_name = current_name; // define an alias name for a namespace
```

- You can also use the using directive to avoid using the scope resolution operator every time. The using directive tells the compiler to check the specified namespace when resolving names. For example:

```cpp
using namespace std; // tell the compiler to check the std namespace
cout << "Hello World!" << endl; // no need to write std::cout or std::endl
```

- However, the using directive can cause name conflicts if the same name is defined in more than one namespace. To avoid this, you can use the using declaration to introduce a single name from a namespace into the current scope. For example:

```cpp
using std::cout; // only introduce cout from the std namespace
cout << "Hello World!" << endl; // no need to write std::cout
cin >> x; // error, cin is not introduced, need to write std::cin
```
```