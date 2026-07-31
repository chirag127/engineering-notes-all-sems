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
- Lists can be modified using methods such as `append()`, `insert()`, and `remove()`.
- Example: `my_list = [1, 2, 3]`

#### Mutable Sequences
- Mutable sequences are sequences that can be modified after creation.
- Lists are an example of mutable sequences.
- Other examples include `bytearray` and `array.array`.

#### List Comprehension
- List comprehension is a concise way to create lists.
- It consists of an expression followed by a `for` clause and zero or more `if` clauses.
- Example: `[x**2 for x in range(5)]` creates a list of the first 5 square numbers.

#### Sets
- Sets are unordered collections of unique elements.
- They are created using curly braces `{}` or the `set()` function.
- Sets can be modified using methods such as `add()` and `remove()`.
- Example: `my_set = {1, 2, 3}`

#### Dictionaries
- Dictionaries are unordered collections of key-value pairs.
- They are created using curly braces `{}` with key-value pairs separated by colons `:`.
- Dictionaries can be modified by assigning values to keys.
- Example: `my_dict = {'a': 1, 'b': 2, 'c': 3}`

### Unit 3 - Function

#### Parts of A Function
- A function consists of a name, parameters, a docstring, and a body.
- The name is used to call the function.
- The parameters define the input to the function.
- The docstring describes what the function does.
- The body contains the code that is executed when the function is called.

#### Execution of A Function
- When a function is called, the code in its body is executed.
- The values of the arguments passed to the function are assigned to the parameters.
- The code in the body is executed with these parameter values.

#### Keyword and Default Arguments
- Keyword arguments are arguments that are passed to a function by explicitly specifying the name of the parameter.
- Default arguments are arguments that have a default value specified in the function definition.
- If a default argument is not provided when the function is called, the default value is used.

#### Scope Rules
- The scope of a variable refers to the region of the code where the variable can be accessed.
- Variables defined in a function have local scope and can only be accessed within the function.
- Variables defined outside of a function have global scope and can be accessed from anywhere in the code.