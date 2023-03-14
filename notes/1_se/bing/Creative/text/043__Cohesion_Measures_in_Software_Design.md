#### Cohesion Measures in Software Design

- Cohesion is a measure of how strongly related and focused the various responsibilities of a software module are.
- Cohesion is an ordinal type of measurement and is usually described as “high cohesion” or “low cohesion”.
- Modules with high cohesion tend to be preferable, because high cohesion is associated with several desirable traits of software including robustness, reliability, reusability, and understandability.
- In contrast, low cohesion is associated with undesirable traits such as being difficult to maintain, test, reuse, or even understand.
- Cohesion is often contrasted with coupling, a different concept. High cohesion often correlates with loose coupling, and vice versa.
- Cohesion measures the degree of the module's functionality. It stands for how tightly the internal modules' components are bound together. It shows the functional strength of a module of software.
- The elements inside a module can be instructions, groups of instructions, definition of data, call from another module etc. and the aim is always for functions that are strongly related and the expectation is for everything inside the module to be in connection with one another where the focus is on the task.
- Cohesion is a sliding scale metric. A common mistake is to treat cohesion as a binary attribute instead of a sliding scale.
- There are different types of cohesion, such as functional cohesion, sequential cohesion, communicational cohesion, procedural cohesion, temporal cohesion, logical cohesion, and coincidental cohesion.
- Functional cohesion is the highest degree of cohesion, where a module performs a single, well-defined function.
- Sequential cohesion is where a module performs a series of related actions, where the output of one action is the input of another.
- Communicational cohesion is where a module performs a set of actions that are related by the data they operate on.
- Procedural cohesion is where a module performs a set of actions that are related by the order of execution.
- Temporal cohesion is where a module performs a set of actions that are related by time, such as initialization or termination.
- Logical cohesion is where a module performs a set of actions that are related by logic, such as a menu or a case statement.
- Coincidental cohesion is the lowest degree of cohesion, where a module performs a set of unrelated actions.
- The goal of software design is to achieve high cohesion and low coupling, as this leads to better software quality and maintainability.