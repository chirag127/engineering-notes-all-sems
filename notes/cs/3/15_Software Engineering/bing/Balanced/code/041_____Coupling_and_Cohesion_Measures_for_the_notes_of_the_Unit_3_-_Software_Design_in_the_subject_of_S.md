# Coupling and Cohesion Measures

Coupling and cohesion are two key concepts in software engineering that are used to measure the quality of a software system’s design. They are related to the modularity and structure of the system, and how well the components interact with each other.

## Coupling

Coupling refers to the degree of interdependence between software modules. It is a measure of how closely connected two routines or modules are, and how much they depend on each other. High coupling means that modules are closely connected and changes in one module may affect other modules. Low coupling means that modules are loosely connected and changes in one module have little or no impact on other modules.

Coupling can be classified into different types, such as:

- Content coupling: when one module directly accesses or modifies the content of another module.
- Common coupling: when two modules share the same global data.
- Control coupling: when one module passes control information to another module.
- Stamp coupling: when two modules communicate using a composite data structure.
- Data coupling: when two modules communicate using simple data parameters.
- Message coupling: when two modules communicate using message passing.

The degree of coupling decreases from content coupling to message coupling, and the goal is to achieve low coupling or message coupling in a software system.

## Cohesion

Cohesion refers to the degree of relatedness and focus of the responsibilities of a software module. It is a measure of how well the elements of a module belong together and support a common goal. High cohesion means that a module has a single, well-defined purpose and function. Low cohesion means that a module has multiple, unrelated or poorly defined responsibilities and functions.

Cohesion can be classified into different types, such as:

- Functional cohesion: when a module performs a single specific function.
- Sequential cohesion: when a module performs a series of related actions in a sequence.
- Communicational cohesion: when a module performs a set of actions related by the input or output data.
- Procedural cohesion: when a module performs a set of actions related by the order of execution.
- Temporal cohesion: when a module performs a set of actions related by the time of execution.
- Logical cohesion: when a module performs a set of actions related by a logical condition.
- Coincidental cohesion: when a module performs a set of actions that have no logical relationship.

The degree of cohesion increases from coincidental cohesion to functional cohesion, and the goal is to achieve high cohesion or functional cohesion in a software system.

## Coupling and Cohesion Trade-offs

Both coupling and cohesion are important factors in determining the maintainability, scalability, and reliability of a software system. High coupling and low cohesion can make a system difficult to change and test, while low coupling and high cohesion make a system easier to maintain and improve.

However, there may be trade-offs between coupling and cohesion, depending on the design choices and constraints of the system. For example, increasing the cohesion of a module may require increasing its coupling with other modules, or decreasing the coupling of a module may require decreasing its cohesion. Therefore, the optimal level of coupling and cohesion may vary depending on the context and requirements of the system.

## Coupling and Cohesion Metrics

There are various metrics and methods to measure and evaluate the coupling and cohesion of a software system. Some of the common metrics are:

- Coupling Between Objects (CBO): the number of classes that a class is coupled to.
- Lack of Cohesion in Methods (LCOM): the number of pairs of methods in a class that do not share any attributes.
- Cohesion Among Methods in Class (CAMC): the ratio of the number of methods accessing a given attribute to the total number of methods in a class.
- Normalized Hamming Distance (NHD): the average distance between the methods of a class in terms of the attributes they access.
- Tight Class Cohesion (TCC): the ratio of the number of pairs of methods in a class that access at least one common attribute to the total number of pairs of methods in a class.
- Loose Class Cohesion (LCC): the ratio of the number of connected components in a graph representing the methods and attributes of a class to the total number of methods in a class.

These metrics can be used to assess the quality and complexity of the software design, and to identify potential areas for improvement and refactoring.