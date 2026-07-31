Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of default arguments for the notes of the Unit 5 - C++ Functions in the subject of Object Oriented System Design.

### Default Arguments

- Default arguments are arguments that have a predefined value in the function declaration.
- Default arguments can be used to simplify the function call and avoid passing unnecessary arguments.
- Default arguments are specified by assigning a value to the parameter in the function declaration, after the parameter type and name.
- Example: `void printMessage(string message = "Hello, world!");`
- In this example, the parameter `message` has a default value of `"Hello, world!"`. If the function is called without passing an argument for `message`, the default value will be used. If the function is called with an argument for `message`, the argument value will override the default value.
- Default arguments can be omitted from right to left, but not from left to right. This means that if a function has multiple parameters with default values, the arguments for the rightmost parameters can be skipped, but the arguments for the leftmost parameters must be provided.
- Example: `void printDetails(string name, int age = 20, string city = "New York");`
- In this example, the parameters `age` and `city` have default values of `20` and `"New York"`, respectively. The function can be called in any of the following ways:

  - `printDetails("Alice");` // name = "Alice", age = 20, city = "New York"
  - `printDetails("Bob", 25);` // name = "Bob", age = 25, city = "New York"
  - `printDetails("Charlie", 30, "London");` // name = "Charlie", age = 30, city = "London"
  - `printDetails("David", city = "Paris");` // name = "David", age = 20, city = "Paris"

- However, the function cannot be called in any of the following ways, as they would cause a syntax error or ambiguity:

  - `printDetails();` // name is missing
  - `printDetails(18);` // name is missing, and age is not a string
  - `printDetails(age = 18, "Emma");` // name must be provided before age

- Default arguments can be used to provide backward compatibility for existing functions. If a new parameter is added to a function, it can be given a default value so that the existing function calls do not need to be modified.
- Example: `void add(int a, int b, bool print = false);`
- In this example, the parameter `print` is added to the function `add`, which performs the addition of two integers. The parameter `print` has a default value of `false`, which means that by default, the function does not print the result of the addition. However, if the function is called with a third argument of `true`, the function will print the result of the addition. This way, the existing function calls of the form `add(x, y);` will still work as before, and the new function calls of the form `add(x, y, true);` will have the additional functionality of printing the result.