#### Cohesion Measures in Software Design

- Cohesion is a measure of how well the elements of a module belong together.
- Cohesion is desirable because it implies that a module has a single, well-defined purpose or function, and that it can be easily reused and maintained.
- Cohesion can be measured at different levels of granularity, such as function, class, package, or subsystem.
- There are different types of cohesion, ranging from low to high, depending on the degree of relatedness among the elements of a module.
- The types of cohesion are:

  - **Coincidental cohesion**: The elements of a module have no apparent relationship to each other. This is the lowest level of cohesion and should be avoided. Example: A module that performs file operations, mathematical calculations, and string manipulations.
  - **Logical cohesion**: The elements of a module are related by some logical category, such as type of input or output, but not by the problem domain. This is a low level of cohesion and should be improved. Example: A module that performs all operations on dates, such as validation, formatting, and arithmetic.
  - **Temporal cohesion**: The elements of a module are related by the time of execution, such as initialization, termination, or error handling. This is a low level of cohesion and should be improved. Example: A module that performs all startup tasks, such as opening files, allocating memory, and creating objects.
  - **Procedural cohesion**: The elements of a module are related by the sequence of steps in a procedure, such as a control flow or an algorithm. This is a moderate level of cohesion and may be acceptable in some cases. Example: A module that implements the bubble sort algorithm.
  - **Communicational cohesion**: The elements of a module are related by the data they operate on, such as a common input, output, or global variable. This is a moderate level of cohesion and may be acceptable in some cases. Example: A module that performs all operations on a customer record, such as reading, writing, updating, and deleting.
  - **Functional cohesion**: The elements of a module are related by the functionality they provide, such as a single abstract task or a service. This is a high level of cohesion and should be aimed for. Example: A module that calculates the net pay of an employee, given the gross pay and deductions.
  - **Informational cohesion**: The elements of a module are related by the information they manipulate, such as a data structure or an object. This is the highest level of cohesion and should be aimed for. Example: A module that defines and implements the methods and attributes of a customer class.

- A mnemonic to remember the types of cohesion is: **CLoTiP CoFuIn** (Coincidental, Logical, Temporal, Procedural, Communicational, Functional, Informational).
- A learning trick to remember the order of cohesion from low to high is: **Coincidence is the lowest form of cohesion, information is the highest form of cohesion**.