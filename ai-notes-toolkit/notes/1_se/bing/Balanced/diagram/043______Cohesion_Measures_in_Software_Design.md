Cohesion is a measure of how strongly related and focused the various responsibilities of a software module are. It shows the functional strength of a module of software. A good software design implies high cohesion, which means that the module performs a single well-defined task. High cohesion is associated with several desirable traits of software including robustness, reliability, reusability, and understandability. In contrast, low cohesion means that the module performs multiple unrelated tasks, which makes it difficult to maintain and test.

There are different types of cohesion, ranging from low to high, that can be used to measure the quality of a software module. These are :

- **Coincidental cohesion**: The module has no logical relationship among its elements. It is an arbitrary grouping of code statements. This is the lowest level of cohesion and should be avoided.
- **Logical cohesion**: The module performs a series of related tasks, such as input, output, or error handling. The tasks are related by logic, but not by functionality. The module can be parameterized to perform different tasks based on the input.
- **Temporal cohesion**: The module performs a series of tasks that are related by time, such as initialization, termination, or event handling. The tasks are performed in a specific sequence, but not necessarily related by functionality.
- **Procedural cohesion**: The module performs a series of tasks that are related by the order of execution, such as a control flow. The tasks are performed in a specific sequence to achieve a specific result, but not necessarily related by functionality.
- **Communicational cohesion**: The module performs a series of tasks that are related by the use of the same data, such as a database query. The tasks operate on the same input or output data, but not necessarily related by functionality.
- **Sequential cohesion**: The module performs a series of tasks that are related by the flow of data, such as a pipeline. The output of one task is the input of another task, and the tasks are related by functionality.
- **Functional cohesion**: The module performs a single well-defined task, such as a mathematical function. The input and output of the module are clearly defined, and the module has a single purpose. This is the highest level of cohesion and should be aimed for.

A possible diagram to illustrate the different types of cohesion in software design is:

#### Cohesion Measures in Software Design

```
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |                 |                 |                 |
|                 |                 |                 |                 |                 |                 |                 |
|                 |                 |                 |                 |                 |                 |                 |
|                 |                 |                 |                 |                 |                 |                 |
|                 |                 |                 |                 |                 |                 |                 |
|                 |                 |                 |                 |                 |                 |                 |
|                 |                 |                 |                 |                 |                 |                 |
|                 |                 |                 |                 |                 |                 |                 |
|                 |                 |                 |                 |                 |                 |                 |
|                 |                 |                 |                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |                 |                 |                 |
|                 |                 |                 |                 |                 |                 |                 |
|                 |                 |                 |                 |                 |                 |                 |
|                 |                 |                 |                 |                 |                 |                 |
|                 |                 |                 |                 |                 |                 |                 |
|                 |                 |                 |                 |                 |                 |                 |
|                 |                 |                 |                 |                 |                 |                 |
|                 |                 |                 |                 |                 |                 |                 |
|                 |                 |                 |                 |                 |                 |                 |
|                 |                 |                 |                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |                 |                 |                 |
|                 |                 |                 |                 |                 |                 |                 |
|                 |                 |                 |                 |                 |                 |                 |
|                 |                 |                 |                 |                 |                 |                 |
|    Input    +---+---+    Output   |                 |

```
