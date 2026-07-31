### Namespace

- A namespace is a declarative region that provides a scope to the identifiers (the names of types, functions, variables, etc) inside it.
- Namespaces are used to organize code into logical groups and to prevent name collisions that can occur especially when your code base includes multiple libraries.
- A namespace definition begins with the keyword `namespace` followed by the namespace name as follows: `namespace namespace_name { /* code declarations */ }`
- The keyword `using` can be used to introduce a name from a namespace into the current declarative region, such as `using namespace std;`
- Namespaces can be nested, meaning you can define one namespace inside another namespace.
- You can also define a namespace across multiple files by using the same namespace name in each file.
- Namespace aliases can be created using the `namespace` keyword followed by the alias name, an equal sign, and the original namespace name, such as `namespace new_name = current_name;`
- It is considered good practice to use namespaces to avoid naming conflicts and to make code more readable and organized.
