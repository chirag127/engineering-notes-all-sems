# Coupling and Cohesion Measures

Coupling and cohesion are two important concepts in software design that help to measure the quality of a software system. These measures are used to evaluate the degree of interdependence between modules and the strength of the relationship between the elements within a module.

## Coupling

Coupling refers to the degree of interdependence between modules. A high degree of coupling indicates that a change in one module may affect other modules, making the system more difficult to maintain and modify. On the other hand, low coupling indicates that modules are independent of each other, making the system easier to maintain and modify.

There are several types of coupling, including:

- **Content coupling**: This occurs when one module directly modifies or relies on the internal workings of another module. This is the highest level of coupling and should be avoided.

- **Common coupling**: This occurs when multiple modules share the same global data. This can make the system difficult to maintain, as changes to the global data may affect multiple modules.

- **Control coupling**: This occurs when one module controls the flow of another module by passing it information on what to do. This can make the system difficult to maintain, as changes to the controlling module may affect the behavior of the controlled module.

- **Stamp coupling**: This occurs when multiple modules share a composite data structure and use only parts of it. This can make the system difficult to maintain, as changes to the data structure may affect multiple modules.

- **Data coupling**: This occurs when modules share data through parameters. This is the lowest level of coupling and is generally desirable.

## Cohesion

Cohesion refers to the degree to which the elements within a module are related to each other. High cohesion indicates that the elements within a module are closely related and work together to achieve a single, well-defined task. Low cohesion indicates that the elements within a module are not closely related and may be performing multiple, unrelated tasks.

There are several types of cohesion, including:

- **Functional cohesion**: This occurs when all the elements within a module work together to achieve a single, well-defined task. This is the highest level of cohesion and is generally desirable.

- **Sequential cohesion**: This occurs when the elements within a module are related by the fact that the output of one element is the input of another. This can make the module difficult to maintain, as changes to one element may affect the behavior of other elements.

- **Communicational cohesion**: This occurs when the elements within a module are related by the fact that they operate on the same data. This can make the module difficult to maintain, as changes to the data may affect the behavior of multiple elements.

- **Procedural cohesion**: This occurs when the elements within a module are related by the fact that they are part of a procedure. This can make the module difficult to maintain, as changes to the procedure may affect the behavior of multiple elements.

- **Temporal cohesion**: This occurs when the elements within a module are related by the fact that they are executed at the same time. This can make the module difficult to maintain, as changes to the timing of one element may affect the behavior of other elements.

- **Logical cohesion**: This occurs when the elements within a module are related by the fact that they perform similar tasks. This can make the module difficult to maintain, as changes to one task may affect the behavior of other tasks.

- **Coincidental cohesion**: This occurs when the elements within a module are not related in any meaningful way. This is the lowest level of cohesion and should be avoided.

In summary, coupling and cohesion are important measures of software design quality. Low coupling and high cohesion are generally desirable, as they make the system easier to maintain and modify. These measures can be used to evaluate the design of a software system and to identify areas for improvement.