### Coupling and Cohesion Measures

Coupling and cohesion are two important concepts in software design that help to measure the quality of a software system. These measures are used to evaluate the degree of interdependence between modules and the strength of the relationship between the elements within a module.

#### Coupling
Coupling refers to the degree of interdependence between modules. A high degree of coupling indicates that a change in one module may affect other modules, making the system more difficult to maintain and modify. There are several types of coupling, including:
- Content coupling: when one module directly accesses or modifies the content of another module.
- Common coupling: when two or more modules share global data.
- Control coupling: when one module controls the flow of another module by passing control information.
- Stamp coupling: when two or more modules share a composite data structure.
- Data coupling: when two or more modules share data through parameters.

#### Cohesion
Cohesion refers to the degree to which the elements within a module are related to one another. A high degree of cohesion indicates that the elements within a module are strongly related and work together to achieve a single, well-defined task. There are several types of cohesion, including:
- Functional cohesion: when all the elements within a module work together to achieve a single, well-defined task.
- Sequential cohesion: when the output of one element serves as the input for another element.
- Communicational cohesion: when the elements within a module operate on the same input or produce the same output.
- Procedural cohesion: when the elements within a module are related by the sequence of steps to be followed.
- Temporal cohesion: when the elements within a module are related by the time at which they are executed.
- Logical cohesion: when the elements within a module are related by the logical structure of the problem being solved.
- Coincidental cohesion: when the elements within a module have no meaningful relationship to one another.

In summary, coupling and cohesion are important measures in software design that help to evaluate the quality of a software system. A well-designed system should have low coupling and high cohesion, making it easier to maintain and modify.