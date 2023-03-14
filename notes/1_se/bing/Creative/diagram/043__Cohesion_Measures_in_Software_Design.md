Cohesion is a measure of how strongly related and focused the various responsibilities of a software module are. It is a desirable property of software design, as it indicates that the module has a single, well-defined purpose and function. Cohesion can be classified into different types, ranging from low to high, based on the degree of similarity and dependency among the elements of a module. Some of the common types of cohesion are:

- **Coincidental cohesion**: The lowest level of cohesion, where the elements of a module have no apparent relationship to each other. The module is a random collection of functions or data that are grouped together for convenience or by accident. This type of cohesion should be avoided, as it makes the module difficult to understand, maintain, and reuse.
- **Logical cohesion**: A slightly higher level of cohesion, where the elements of a module are related by some logical category, such as performing the same type of task, handling the same type of input or output, or belonging to the same problem domain. However, the elements are not necessarily related to each other functionally, and may have different goals and purposes. This type of cohesion is acceptable, but not ideal, as it may still introduce unnecessary coupling and complexity.
- **Temporal cohesion**: A moderate level of cohesion, where the elements of a module are related by the time of execution, such as initialization, processing, or termination. The elements are executed in a specific sequence, but they may not share any data or functionality. This type of cohesion is also acceptable, but not ideal, as it may make the module dependent on external factors and events.
- **Procedural cohesion**: A higher level of cohesion, where the elements of a module are related by the order of execution, and form a specific procedure or algorithm. The elements share some data and functionality, and perform a single task or subtask. This type of cohesion is desirable, as it makes the module more coherent and understandable.
- **Communicational cohesion**: A high level of cohesion, where the elements of a module are related by the data they operate on, and share the same input or output. The elements perform different operations on the same data, and form a coherent data transformation. This type of cohesion is also desirable, as it makes the module more efficient and consistent.
- **Sequential cohesion**: A very high level of cohesion, where the elements of a module are related by the data flow, and form a pipeline of operations. The output of one element is the input of the next element, and the elements perform a single task or subtask. This type of cohesion is ideal, as it makes the module more modular and reusable.
- **Functional cohesion**: The highest level of cohesion, where the elements of a module are related by the functionality they provide, and form a complete and independent function. The module has a single, well-defined purpose and function, and performs it with minimal or no side effects. This type of cohesion is the ultimate goal of software design, as it makes the module more reliable, maintainable, and testable.

#### Cohesion Measures in Software Design

The following diagram illustrates the different types of cohesion in software design using a simple example of a module that performs some operations on a file. The module has six elements: open file, read file, process file, write file, close file, and print file. The diagram shows how the elements are grouped together based on the type of cohesion, and how the cohesion level affects the module's quality and characteristics.

```
+----------------+    +----------------+    +----------------+    +----------------+
|                |    |                |    |                |    |                |
| Coincidental   |    | Logical        |    | Temporal       |    | Procedural     |
|                |    |                |    |                |    |                |
| +------------+ |    | +------------+ |    | +------------+ |    | +------------+ |
| | Open file  | |    | | Open file  | |    | | Open file  | |    | | Open file  | |
| +------------+ |    | +------------+ |    | +------------+ |    | +------------+ |
| +------------+ |    | +------------+ |    | +------------+ |    | +------------+ |
| | Read file  | |    | | Read file  | |    | | Read file  | |    | | Read file  | |
| +------------+ |    | +------------+ |    | +------------+ |    | +------------+ |
| +------------+ |    | +------------+ |    |