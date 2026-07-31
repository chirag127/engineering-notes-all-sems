### Coupling and Cohesion Measures

Coupling and cohesion are two key concepts in software engineering that are used to measure the quality of a software system's design. They are related to the modularity and structure of the system, and how well the components interact and cooperate with each other.

#### Coupling

Coupling refers to the degree of interdependence between software modules. It is a measure of how closely connected two routines or modules are, and how much they rely on each other's data, functionality, or control flow. High coupling means that modules are tightly connected and changes in one module may affect other modules. Low coupling means that modules are loosely connected and changes in one module have minimal impact on other modules.

Coupling can be classified into different types, depending on the nature and strength of the dependencies. Some common types of coupling are:

- **Content coupling**: This is the strongest form of coupling, where one module directly accesses or modifies the content of another module, such as a variable or a statement. This violates the principle of information hiding and makes the modules highly dependent on each other.
- **Common coupling**: This is where two or more modules share the same global data or resources, such as a global variable or a file. This creates a potential for side effects and conflicts, and reduces the readability and maintainability of the code.
- **Control coupling**: This is where one module passes control information to another module, such as a flag or a parameter, that affects the logic or behavior of the other module. This makes the modules dependent on the order and timing of execution, and reduces the flexibility and reusability of the code.
- **Stamp coupling**: This is where one module passes a data structure, such as a record or a structure, to another module, and the other module only uses a part of it. This creates unnecessary dependencies and increases the complexity and size of the data being passed.
- **Data coupling**: This is the weakest form of coupling, where one module passes data to another module, and the data is simple and primitive, such as a variable or a constant. This minimizes the dependencies and allows the modules to be independent and interchangeable.

#### Cohesion

Cohesion refers to the degree of relatedness and unity within a software module. It is a measure of how well the elements of a module belong together, and how focused and consistent the module is in performing its tasks. High cohesion means that a module has a single, well-defined purpose and responsibility, and all its elements are relevant and essential to that purpose. Low cohesion means that a module has multiple, vague, or conflicting purposes and responsibilities, and some of its elements are irrelevant or redundant.

Cohesion can be classified into different levels, depending on the degree of similarity and harmony among the elements of a module. Some common levels of cohesion are:

- **Functional cohesion**: This is the highest level of cohesion, where a module performs a single, specific, and meaningful function, and all its elements contribute to that function. This makes the module easy to understand, test, and reuse, and improves the quality and reliability of the code.
- **Sequential cohesion**: This is where a module performs a series of related subtasks, and the output of one subtask is the input of the next subtask. This makes the module logical and coherent, but also creates dependencies and coupling among the subtasks.
- **Communicational cohesion**: This is where a module performs a set of subtasks that are related by the use of the same input or output data, such as reading or writing to a file. This makes the module efficient and consistent, but also creates potential for conflicts and errors in the data.
- **Procedural cohesion**: This is where a module performs a set of subtasks that are related by the order or sequence of execution, such as a menu or a loop. This makes the module structured and organized, but also creates coupling and reduces the flexibility and reusability of the code.
- **Temporal cohesion**: This is where a module performs a set of subtasks that are related by the time of execution, such as initialization or termination. This makes the module convenient and modular, but also creates coupling and reduces the cohesion and clarity of the code.
- **Logical cohesion**: This is where a module performs a set of subtasks that are related by some logical condition, such as a switch or a case statement. This makes the module versatile and adaptable, but also creates coupling and reduces the readability and maintainability of the code.
- **Coincidental cohesion**: This is the lowest level of cohesion, where a module performs a set of subtasks that are unrelated or arbitrary, and