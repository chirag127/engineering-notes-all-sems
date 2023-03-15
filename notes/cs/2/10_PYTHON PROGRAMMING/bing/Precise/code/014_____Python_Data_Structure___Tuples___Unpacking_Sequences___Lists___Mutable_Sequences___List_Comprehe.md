### Python Data Structure

#### Tuples
- Tuples are ordered, immutable collections of elements.
- They are defined using parentheses `()` with elements separated by commas.
- Tuples can contain elements of different types.
- Accessing elements of a tuple is done using indexing, e.g. `my_tuple[0]` returns the first element of the tuple.

#### Unpacking Sequences
- Unpacking sequences refers to assigning the elements of a sequence to multiple variables.
- This can be done with any sequence type, including tuples and lists.
- For example, `x, y, z = my_tuple` assigns the first element of `my_tuple` to `x`, the second to `y`, and the third to `z`.

#### Lists
- Lists are ordered, mutable collections of elements.
- They are defined using square brackets `[]` with elements separated by commas.
- Lists can contain elements of different types.
- Accessing elements of a list is done using indexing, e.g. `my_list[0]` returns the first element of the list.
- Lists can be modified using methods such as `append()`, `insert()`, and `remove()`.

#### Mutable Sequences
- Mutable sequences are sequence types that can be modified.
- Lists are an example of a mutable sequence.
- Other mutable sequence types include `bytearray` and `array.array`.

#### List Comprehension
- List comprehension is a concise way to create lists.
- It consists of an expression followed by a `for` clause and zero or more `if` clauses.
- For example, `[x**2 for x in range(10) if x % 2 == 0]` creates a list of the squares of even numbers from 0 to 9.

#### Sets
- Sets are unordered collections of unique elements.
- They are defined using curly braces `{}` with elements separated by commas.
- Sets can contain elements of different types, but the elements must be hashable.
- Sets support operations such as union, intersection, and difference.

#### Dictionaries
- Dictionaries are unordered collections of key-value pairs.
- They are defined using curly braces `{}` with key-value pairs separated by commas.
- The keys must be hashable, and the values can be of any type.
- Accessing the value associated with a key is done using indexing, e.g. `my_dict[key]` returns the value associated with `key` in `my_dict`.
- Dictionaries can be modified by assigning a value to a key, e.g. `my_dict[key] = value`.

### Unit 3 - Function

#### Parts of A Function
- A function consists of a name, parameters, a docstring, and a body.
- The name is used to call the function.
- The parameters define the inputs to the function.
- The docstring provides documentation for the function.
- The body contains the code that is executed when the function is called.

#### Execution of A Function
- When a function is called, the code in the body of the function is executed.
- The values of the arguments passed to the function are assigned to the parameters.
- The code in the body of the function can access the values of the parameters and any variables defined in the body of the function.

#### Keyword and Default Arguments
- Keyword arguments are arguments that are passed to a function by explicitly specifying the name of the parameter.
- Default arguments are arguments that have a default value specified in the function definition.
- If a default argument is not provided when the function is called, the default value is used.

#### Scope Rules
- The scope of a variable refers to the region of the code where the variable can be accessed.
- Variables defined in the body of a function have local scope, meaning they can only be accessed within the function.
- Variables defined outside of a function have global scope, meaning they can be accessed from anywhere in the code.