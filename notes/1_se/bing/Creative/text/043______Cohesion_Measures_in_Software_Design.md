#### Cohesion Measures in Software Design

- Cohesion is a measure of how strongly related and focused the various responsibilities of a software module are  .
- A software module is a unit of code that performs a specific task, such as a function, a class, or a package.
- Cohesion is an ordinal type of measurement and is usually described as “high cohesion” or “low cohesion”.
- Modules with high cohesion tend to be preferable, because high cohesion is associated with several desirable traits of software including robustness, reliability, reusability, and understandability .
- In contrast, low cohesion is associated with several undesirable traits of software including complexity, fragility, duplication, and difficulty in testing .
- There are different types of cohesion that can be used to measure the degree of the module's functionality, such as functional cohesion, sequential cohesion, communicational cohesion, procedural cohesion, temporal cohesion, logical cohesion, and coincidental cohesion .
- Functional cohesion is the highest level of cohesion, where a module performs a single and well-defined task .
- Sequential cohesion is where a module performs a series of related tasks that follow a sequence, such as reading, processing, and writing data .
- Communicational cohesion is where a module performs a set of tasks that operate on the same data, such as sorting, searching, and filtering a list .
- Procedural cohesion is where a module performs a set of tasks that are related by the order of execution, such as validating input, calculating output, and displaying results .
- Temporal cohesion is where a module performs a set of tasks that are related by time, such as initializing, terminating, or logging .
- Logical cohesion is where a module performs a set of tasks that are related by logic, such as handling different cases of a switch statement .
- Coincidental cohesion is the lowest level of cohesion, where a module performs a set of tasks that are unrelated or arbitrary, such as a utility module that contains various functions .
- Cohesion is related to coupling, which is a measure of how dependent the modules are on each other .
- Low coupling and high cohesion make a system easier to maintain and improve, while high coupling and low cohesion make a system difficult to change and test .