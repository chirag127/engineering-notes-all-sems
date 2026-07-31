# Coupling and Cohesion Measures

Coupling and cohesion are two key concepts in software engineering that are used to measure the quality of a software system's design. They are related to the modularity and structure of the system, and how well the components interact with each other.

## Coupling

Coupling refers to the degree of interdependence between software modules. It is a measure of how closely connected two routines or modules are, and how much they depend on each other. High coupling means that modules are closely connected and changes in one module may affect other modules. Low coupling means that modules are loosely connected and changes in one module have little or no impact on other modules.

Coupling can be classified into different types, such as:

- Content coupling: When one module directly accesses or modifies the content of another module. This is the highest form of coupling and should be avoided.
- Common coupling: When two modules share the same global data. This can create unwanted side effects and make the system hard to maintain.
- Control coupling: When one module passes control information to another module, such as a flag or a function pointer. This can make the system complex and reduce readability.
- Stamp coupling: When two modules communicate using a composite data structure, such as a record or a class. This can create unnecessary dependencies and increase the size of the interface.
- Data coupling: When two modules communicate using simple data items, such as parameters or return values. This is the lowest form of coupling and should be preferred.

Coupling can be measured using various metrics, such as:

- Efferent coupling: The number of modules that a module depends on. This indicates the outgoing dependencies of a module.
- Afferent coupling: The number of modules that depend on a module. This indicates the incoming dependencies of a module.
- Instability: The ratio of efferent coupling to the total coupling (efferent + afferent). This indicates how sensitive a module is to changes in other modules.
- Abstractness: The ratio of abstract classes and interfaces to the total number of classes in a module. This indicates how general and flexible a module is.
- Distance from the main sequence: The absolute value of the difference between abstractness and instability. This indicates how balanced a module is between abstractness and stability.

## Cohesion

Cohesion refers to the degree of relatedness and focus of the responsibilities of a software module. It is a measure of how well the elements of a module belong together, and how well they support a single purpose. High cohesion means that a module has a clear and narrow functionality, and all its elements are relevant and essential. Low cohesion means that a module has a vague and broad functionality, and some of its elements are irrelevant or redundant.

Cohesion can be classified into different types, such as:

- Functional cohesion: When a module performs a single and specific function. This is the highest form of cohesion and should be aimed for.
- Sequential cohesion: When a module performs a series of related actions that follow a logical sequence. This is a good form of cohesion, but it can be improved by breaking the module into smaller modules with functional cohesion.
- Communicational cohesion: When a module performs a set of actions that operate on the same data. This is a moderate form of cohesion, but it can be improved by separating the data manipulation from the data access.
- Procedural cohesion: When a module performs a set of actions that are related by the order of execution. This is a low form of cohesion, and it can be improved by grouping the actions by functionality or data.
- Temporal cohesion: When a module performs a set of actions that are related by time, such as initialization or cleanup. This is a weak form of cohesion, and it can be improved by moving the actions to the modules where they belong.
- Logical cohesion: When a module performs a set of actions that are related by logic, such as a switch statement or a conditional statement. This is a poor form of cohesion, and it can be improved by creating separate modules for each case or condition.
- Coincidental cohesion: When a module performs a set of actions that are not related at all. This is the lowest form of cohesion and should be avoided.

Cohesion can be measured using various metrics, such as:

- Lines of code: The number of lines of code in a module. This indicates the size and complexity of a module.
- Cyclomatic complexity: The number of linearly independent paths through a module. This indicates the branching and decision making of a module.
- Lack of cohesion in methods: The number of pairs of methods in a class that do not