#### Cohesion Measures in Software Design

- Cohesion is a measure of how well the elements of a module belong together.
- Cohesion is desirable because it implies that a module has a single, well-defined purpose or function, and that it can be easily reused and maintained.
- Cohesion can be measured at different levels of granularity, such as function, class, package, or subsystem.
- There are different types of cohesion, ranging from low to high, depending on the degree of relatedness among the elements of a module.
- The types of cohesion are:

  - **Coincidental cohesion**: The elements of a module have no apparent relationship to each other. This is the lowest level of cohesion and should be avoided. Example: A module that performs file operations, mathematical calculations, and string manipulations.
  - **Logical cohesion**: The elements of a module are related by some logical category, such as type of input, output, or function, but are not necessarily related to each other. This is a low level of cohesion and should be improved. Example: A module that performs different sorting algorithms based on a parameter.
  - **Temporal cohesion**: The elements of a module are related by the time of execution, such as initialization, termination, or error handling. This is a low level of cohesion and should be improved. Example: A module that opens a file, reads data, and closes the file.
  - **Procedural cohesion**: The elements of a module are related by the sequence of steps to perform a specific task. This is a moderate level of cohesion and may be acceptable in some cases. Example: A module that validates user input, calculates results, and displays output.
  - **Communicational cohesion**: The elements of a module are related by the data they operate on, such as reading from or writing to the same file, database, or network. This is a moderate level of cohesion and may be acceptable in some cases. Example: A module that performs different operations on the same record of a file.
  - **Functional cohesion**: The elements of a module are related by the function they collectively perform, such as computing the area of a circle, or validating a password. This is a high level of cohesion and should be aimed for. Example: A module that calculates the factorial of a number.
  - **Informational cohesion**: The elements of a module are related by the data structure they manipulate, such as a stack, a queue, or a tree. This is a high level of cohesion and should be aimed for. Example: A module that implements the operations of a stack.

- A mnemonic to remember the types of cohesion is: **CLT PC FI** (Coincidental, Logical, Temporal, Procedural, Communicational, Functional, Informational).
- A learning trick to remember the order of cohesion from low to high is: **Coincidence is the lowest form of cohesion, and information is the highest form of cohesion**.