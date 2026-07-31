### Coupling and Cohesion Measures

Coupling and cohesion are two key concepts in software engineering that are used to measure the quality of a software system’s design. They are related to the modularity and structure of the system, and how well the components interact with each other.

- **Coupling** refers to the degree of interdependence between software modules. High coupling means that modules are closely connected and changes in one module may affect other modules. Low coupling means that modules are independent and changes in one module have minimal impact on other modules. Uncoupled modules have no interdependence at all .
- **Cohesion** refers to the degree of relatedness and focus of the responsibilities of a single module. High cohesion means that a module performs a single well-defined task or function. Low cohesion means that a module performs multiple unrelated or loosely related tasks or functions. No cohesion means that a module has no specific purpose .
- Both coupling and cohesion are important factors in determining the maintainability, scalability, and reliability of a software system. High coupling and low cohesion can make a system difficult to change and test, while low coupling and high cohesion make a system easier to maintain and improve .

There are different types and levels of coupling and cohesion that can be used to classify and evaluate software modules. Some of the common ones are:

- **Types of coupling** :
  - **Content coupling**: when one module directly accesses or modifies the content of another module. This is the highest and worst form of coupling.
  - **Common coupling**: when two or more modules share the same global data or resources. This can cause unwanted side effects and dependencies.
  - **Control coupling**: when one module passes control information or flags to another module. This can make the modules dependent on the order and logic of execution.
  - **Stamp coupling**: when two or more modules communicate by passing composite data structures or records. This can create unnecessary dependencies on the structure and format of the data.
  - **Data coupling**: when two or more modules communicate by passing simple data values or parameters. This is the lowest and best form of coupling, as it minimizes the dependencies between modules.
- **Types of cohesion** :
  - **Coincidental cohesion**: when a module performs multiple unrelated tasks or functions. This is the lowest and worst form of cohesion, as it makes the module hard to understand and reuse.
  - **Logical cohesion**: when a module performs multiple related tasks or functions, but only one of them is selected based on some input or condition. This can make the module complex and confusing.
  - **Temporal cohesion**: when a module performs multiple tasks or functions that are related by time, such as initialization, cleanup, or error handling. This can make the module dependent on the sequence of execution.
  - **Procedural cohesion**: when a module performs multiple tasks or functions that are related by the order of execution, such as a sequence of steps in an algorithm. This can make the module cohesive, but not modular.
  - **Communicational cohesion**: when a module performs multiple tasks or functions that are related by the use of the same input or output data. This can make the module efficient, but not independent.
  - **Sequential cohesion**: when a module performs multiple tasks or functions that are related by the output of one task or function being the input of another. This can make the module coherent, but not flexible.
  - **Functional cohesion**: when a module performs a single well-defined task or function. This is the highest and best form of cohesion, as it makes the module simple and reusable.

There are different methods and metrics to measure the coupling and cohesion of software modules. Some of the common ones are:

- **Methods of measuring coupling and cohesion**:
  - **Efferent coupling (Ce)**: the number of modules that a module depends on or calls. This indicates how much a module relies on other modules.
  - **Afferent coupling (Ca)**: the number of modules that depend on or call a module. This indicates how much a module is used by other modules.
  - **Instability (I)**: the ratio of efferent coupling to total coupling (Ce / (Ce + Ca)). This indicates how sensitive a module is to changes in other modules.
  - **Abstractness (A)**: the ratio of abstract classes or interfaces to total classes in a module. This indicates how general or specific a module is.
  -