### Python Data Structure

#### Tuples
- Tuples are ordered, immutable collections of elements.
- They are similar to lists, but their elements cannot be changed once assigned.
- Tuples are created using parentheses `()` and elements are separated by commas `,`.
- Example: `my_tuple = (1, 2, 3)`

#### Unpacking Sequences
- Unpacking sequences refers to the process of assigning elements from a sequence to multiple variables.
- The number of variables must match the number of elements in the sequence.
- Example: `x, y, z = (1, 2, 3)`

#### Lists
- Lists are ordered, mutable collections of elements.
- They are created using square brackets `[]` and elements are separated by commas `,`.
- Lists can contain elements of different types.
- Example: `my_list = [1, 'two', 3.0]`

#### Mutable Sequences
- Mutable sequences are sequences whose elements can be changed after assignment.
- Lists are an example of mutable sequences.

#### List Comprehension
- List comprehension is a concise way to create lists.
- It consists of an expression followed by a `for` clause and zero or more `if` clauses.
- Example: `squares = [x**2 for x in range(10)]`

#### Sets
- Sets are unordered collections of unique elements.
- They are created using curly braces `{}` or the `set()` function.
- Sets do not allow duplicate elements.
- Example: `my_set = {1, 2, 3}`

#### Dictionaries
- Dictionaries are unordered collections of key-value pairs.
- They are created using curly braces `{}` with key-value pairs separated by colons `:`.
- Keys must be unique and immutable.
- Example: `my_dict = {'key1': 'value1', 'key2': 'value2'}`

### Unit 3 - Function

#### Parts of A Function
- A function consists of a name, parameters, a docstring, and a body.
- The name is used to call the function.
- Parameters are variables that receive the arguments passed to the function.
- The docstring is a string that describes what the function does.
- The body contains the code that is executed when the function is called.

#### Execution of A Function
- A function is executed by calling its name followed by parentheses `()`.
- Arguments can be passed to the function by placing them inside the parentheses.
- The arguments are assigned to the parameters in the order they are passed.
- The code in the function body is then executed.

#### Keyword and Default Arguments
- Keyword arguments are arguments that are passed to a function by explicitly specifying the parameter name.
- Default arguments are arguments that have a default value specified in the function definition.
- If a default argument is not passed when calling the function, the default value is used.

#### Scope Rules
- The scope of a variable refers to the region of the code where the variable can be accessed.
- Variables defined inside a function have local scope and can only be accessed within the function.
- Variables defined outside a function have global scope and can be accessed from anywhere in the code.