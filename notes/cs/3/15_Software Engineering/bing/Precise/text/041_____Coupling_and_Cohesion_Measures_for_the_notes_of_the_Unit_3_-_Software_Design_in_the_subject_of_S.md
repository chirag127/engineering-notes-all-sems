### Coupling and Cohesion Measures

Coupling and cohesion are two important concepts in software design that help to measure the quality of a software system. These measures are used to evaluate the relationship between the modules of a software system.

#### Coupling
Coupling refers to the degree of interdependence between the modules of a software system. It measures how closely the modules are connected to each other. A high degree of coupling indicates that the modules are tightly connected and changes in one module may affect the other modules. On the other hand, a low degree of coupling indicates that the modules are loosely connected and changes in one module have little or no effect on the other modules.

#### Types of Coupling
There are several types of coupling, including:
- Content coupling: This occurs when one module directly accesses or modifies the content of another module.
- Common coupling: This occurs when two or more modules share the same global data.
- Control coupling: This occurs when one module controls the flow of another module by passing control information.
- Stamp coupling: This occurs when two or more modules share a composite data structure and use only a part of it.
- Data coupling: This occurs when two or more modules share data through parameters.

#### Cohesion
Cohesion refers to the degree of relatedness of the elements within a single module. It measures how closely the elements of a module are connected to each other. A high degree of cohesion indicates that the elements of a module are closely related and perform a single, well-defined task. On the other hand, a low degree of cohesion indicates that the elements of a module are not closely related and may perform multiple, unrelated tasks.

#### Types of Cohesion
There are several types of cohesion, including:
- Functional cohesion: This occurs when the elements of a module work together to perform a single, well-defined task.
- Sequential cohesion: This occurs when the elements of a module are arranged in a specific order to perform a specific task.
- Communicational cohesion: This occurs when the elements of a module operate on the same input or produce the same output.
- Procedural cohesion: This occurs when the elements of a module are related by the sequence of steps to be followed.
- Temporal cohesion: This occurs when the elements of a module are related by the timing of their execution.

In summary, coupling and cohesion are important measures in software design that help to evaluate the quality of a software system. A well-designed software system should have low coupling and high cohesion. This makes the system easier to understand, maintain, and modify.