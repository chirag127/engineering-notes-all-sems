# Coupling and Cohesion Measures

Coupling and cohesion are two key concepts in software engineering that are used to measure the quality of a software system's design. They are related to the modularity and structure of the system, and how well the components interact and cooperate with each other.

## Coupling

Coupling refers to the degree of interdependence between software modules. It is a measure of how closely connected two routines or modules are, and how much they depend on each other's data, control, or interface. High coupling means that modules are closely connected and changes in one module may affect other modules. Low coupling means that modules are loosely connected and changes in one module have little or no impact on other modules.

Coupling can be classified into different types, such as:

- Content coupling: when one module directly accesses or modifies the content of another module.
- Common coupling: when two modules share the same global data.
- Control coupling: when one module passes control information to another module.
- Stamp coupling: when two modules communicate using a composite data structure.
- Data coupling: when two modules communicate using simple data parameters.
- Message coupling: when two modules communicate using message passing.

The desirable level of coupling is low coupling, or message coupling, which implies that modules are independent and communicate only when necessary. Low coupling often correlates with high cohesion, and vice versa.

## Cohesion

Cohesion refers to the degree of relatedness and focus of the responsibilities of a software module. It is a measure of how well the elements of a module belong together, and how well they support a single purpose or functionality. High cohesion means that a module has a single, well-defined role and responsibility. Low cohesion means that a module has multiple, unrelated roles and responsibilities.

Cohesion can be classified into different types, such as:

- Functional cohesion: when a module performs a single function or task.
- Sequential cohesion: when a module performs a series of related actions that follow a logical sequence.
- Communicational cohesion: when a module performs a set of actions that relate to the same input or output data.
- Procedural cohesion: when a module performs a set of actions that are related by the order of execution.
- Temporal cohesion: when a module performs a set of actions that are related by time, such as initialization or termination.
- Logical cohesion: when a module performs a set of actions that are logically related, but not necessarily sequential or communicational.
- Coincidental cohesion: when a module performs a set of actions that are not related at all.

The desirable level of cohesion is high cohesion, or functional cohesion, which implies that a module has a clear and specific purpose and functionality. High cohesion often correlates with low coupling, and vice versa.

## Benefits of Low Coupling and High Cohesion

Both coupling and cohesion are important factors in determining the maintainability, scalability, and reliability of a software system. High coupling and low cohesion can make a system difficult to change and test, while low coupling and high cohesion make a system easier to maintain and improve. Some of the benefits of low coupling and high cohesion are:

- Reduced complexity: low coupling and high cohesion reduce the interdependencies and interactions between modules, making the system simpler and more understandable.
- Increased modularity: low coupling and high cohesion increase the separation of concerns and the encapsulation of modules, making the system more modular and flexible.
- Enhanced reusability: low coupling and high cohesion increase the potential for reusing modules in different contexts and applications, making the system more reusable and adaptable.
- Improved testability: low coupling and high cohesion increase the independence and isolation of modules, making the system more testable and verifiable.
- Higher quality: low coupling and high cohesion increase the consistency and coherence of modules, making the system more reliable and robust.