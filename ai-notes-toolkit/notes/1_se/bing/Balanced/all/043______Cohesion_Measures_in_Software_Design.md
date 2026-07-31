#### Cohesion Measures in Software Design

- Cohesion is a measure of how strongly related and focused the various responsibilities of a software module are.
- A software module can be a function, a class, a package, or a subsystem.
- Cohesion is an ordinal type of measurement and is usually described as “high cohesion” or “low cohesion”.
- Modules with high cohesion tend to be preferable, because high cohesion is associated with several desirable traits of software including robustness, reliability, reusability, and understandability.
- In contrast, low cohesion is associated with undesirable traits such as being difficult to maintain, test, reuse, or even understand.
- Cohesion is often contrasted with coupling, which is a measure of how interdependent two or more software modules are.
- Low coupling and high cohesion are generally considered as the main principles of good software design.

There are different types of cohesion, depending on the degree of functional relatedness of the elements within a module. They are listed below in the order of increasing cohesion:

- **Coincidental cohesion**: The elements within a module have no apparent relationship to each other. This is the lowest level of cohesion and should be avoided. For example, a module that performs file operations, mathematical calculations, and string manipulations has coincidental cohesion.
- **Logical cohesion**: The elements within a module are logically related and perform similar functions, but they are not part of a single problem domain. For example, a module that performs different types of sorting algorithms has logical cohesion.
- **Temporal cohesion**: The elements within a module are related by the fact that they are executed at the same time or in a specific sequence. For example, a module that performs initialization, input, and output operations has temporal cohesion.
- **Procedural cohesion**: The elements within a module are related by the fact that they contribute to a specific task or subtask. For example, a module that performs the steps of a login process has procedural cohesion.
- **Communicational cohesion**: The elements within a module are related by the fact that they operate on the same data or input/output. For example, a module that performs different operations on the same database table has communicational cohesion.
- **Sequential cohesion**: The elements within a module are related by the fact that the output of one element is the input of another element. For example, a module that performs encryption, compression, and transmission of data has sequential cohesion.
- **Functional cohesion**: The elements within a module are related by the fact that they all contribute to a single well-defined function or problem domain. This is the highest level of cohesion and should be aimed for. For example, a module that calculates the area of a circle has functional cohesion.

A possible mnemonic to remember the types of cohesion is: **CLoT ProCoSeFu** (Coincidental, Logical, Temporal, Procedural, Communicational, Sequential, Functional).

Some advantages of high cohesion are:

- It improves the readability and understandability of the code.
- It reduces the complexity and size of the modules.
- It increases the reusability and maintainability of the modules.
- It facilitates the testing and debugging of the modules.
- It enhances the modularity and flexibility of the software design.

Some disadvantages of low cohesion are:

- It decreases the readability and understandability of the code.
- It increases the complexity and size of the modules.
- It reduces the reusability and maintainability of the modules.
- It complicates the testing and debugging of the modules.
- It degrades the modularity and flexibility of the software design.