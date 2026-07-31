Cohesion is a measure of how strongly related and focused the various responsibilities of a software module are. It shows the functional strength of a module of software. A good software design implies clean decomposition of the problem into modules and the neat arrangement of these modules in a hierarchy. The primary characteristic of neat module decomposition is high cohesion. Modules with high cohesion tend to be preferable, because high cohesion is associated with several desirable traits of software including robustness, reliability, reusability, and understandability. In contrast, low cohesion is associated with undesirable traits such as being difficult to maintain, test, reuse, or even understand.

There are different types of cohesion, ranging from low to high, depending on the degree of similarity and relatedness of the elements within a module. Some of the common types of cohesion are:

- **Coincidental cohesion**: The lowest level of cohesion, where the elements within a module have no apparent relationship to each other. The module is a random collection of functions or code segments. This type of cohesion should be avoided as it makes the module difficult to understand, maintain, and reuse.
- **Logical cohesion**: A slightly higher level of cohesion, where the elements within a module are logically related, but not functionally. For example, a module that performs different types of input or output operations, or a module that contains different error handling routines. This type of cohesion is also undesirable, as it violates the principle of separation of concerns and makes the module less cohesive.
- **Temporal cohesion**: A moderate level of cohesion, where the elements within a module are related by the time of execution. For example, a module that performs initialization, termination, or cleanup tasks. This type of cohesion is acceptable, but not ideal, as it still groups unrelated functions together based on a temporal criterion.
- **Procedural cohesion**: A higher level of cohesion, where the elements within a module are related by the order of execution and form a specific sequence of steps. For example, a module that performs a series of calculations or data transformations. This type of cohesion is better than the previous ones, as it reflects a clear purpose and functionality of the module.
- **Communicational cohesion**: A high level of cohesion, where the elements within a module are related by the data they operate on. For example, a module that performs different operations on the same data structure or file. This type of cohesion is desirable, as it shows a strong relationship between the elements and the data they manipulate.
- **Functional cohesion**: The highest level of cohesion, where the elements within a module perform a single and well-defined function. For example, a module that calculates the area of a circle or a module that sorts an array. This type of cohesion is ideal, as it reflects the highest degree of focus and clarity of the module.

The following diagram illustrates the different types of cohesion and their relative levels:

#### Cohesion Measures in Software Design

```
+----------------+----------------+----------------+----------------+----------------+----------------+
|                |                |                |                |                |                |
|                |                |                |                |                |                |
|                |                |                |                |                |                |
|                |                |                |                |                |                |
|                |                |                |                |                |                |
|                |                |                |                |                |                |
|                |                |                |                |                |                |
|                |                |                |                |                |                |
|                |                |                |                |                |                |
|                |                |                |                |                |                |
|                |                |                |                |                |                |
+----------------+----------------+----------------+----------------+----------------+----------------+
|                |                |                |                |                |                |
|                |                |                |                |                |                |
|                |                |                |                |                |                |
|                |                |                |                |                |                |
|                |                |                |                |                |                |
|                | Coincidental  | Logical        | Temporal       | Procedural     | Communicational|
|                | Cohesion      | Cohesion       | Cohesion       | Cohesion       | Cohesion       |
|                |                |                |                |                |                |
|                |                |                |                |                |                |
|                |                |                |                |                |                |
|                |                |                |                |                |                |
+----------------+----------------+----------------+----------------+----------------+----------------

```
