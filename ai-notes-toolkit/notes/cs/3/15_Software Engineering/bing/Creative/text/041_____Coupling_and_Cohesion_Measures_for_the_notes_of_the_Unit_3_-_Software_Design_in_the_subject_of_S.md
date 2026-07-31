### Coupling and Cohesion Measures

Coupling and cohesion are two key concepts in software engineering that are used to measure the quality of a software system's design. They are related to the degree of interdependence and modularity of the software components.

#### Coupling
- Coupling refers to the degree of interdependence between software modules .
- High coupling means that modules are closely connected and changes in one module may affect other modules .
- Low coupling means that modules are independent and changes in one module have minimal impact on other modules .
- Low coupling is desirable as it makes the system easier to maintain, test, and reuse  .
- Coupling can be measured by various metrics, such as efferent coupling, afferent coupling, instability, and abstractness.
- Efferent coupling is the number of outgoing dependencies from a module to other modules.
- Afferent coupling is the number of incoming dependencies to a module from other modules.
- Instability is the ratio of efferent coupling to total coupling (efferent + afferent).
- Abstractness is the ratio of abstract classes and interfaces to total classes and interfaces in a module.
- A module with high efferent coupling and low afferent coupling is unstable and difficult to change.
- A module with low efferent coupling and high afferent coupling is stable and easy to change.
- A module with high abstractness and low instability is abstract and stable.
- A module with low abstractness and high instability is concrete and unstable.

#### Cohesion
- Cohesion refers to the degree of relatedness and unity of the elements within a software module .
- High cohesion means that the elements within a module are strongly related and perform a single well-defined task .
- Low cohesion means that the elements within a module are weakly related and perform multiple unrelated tasks .
- High cohesion is desirable as it makes the system easier to understand, maintain, and reuse  .
- Cohesion can be measured by various metrics, such as functional cohesion, sequential cohesion, communicational cohesion, procedural cohesion, temporal cohesion, logical cohesion, and coincidental cohesion .
- Functional cohesion is the highest level of cohesion, where the elements within a module perform a single specific function .
- Sequential cohesion is where the elements within a module are related by the sequence of operations, such that the output of one element is the input of another element .
- Communicational cohesion is where the elements within a module are related by the data they operate on, such that they access the same data or data structure .
- Procedural cohesion is where the elements within a module are related by the order of execution, such that they follow a specific control flow .
- Temporal cohesion is where the elements within a module are related by the time of execution, such that they are executed together in a specific time period .
- Logical cohesion is where the elements within a module are related by the logic of the task, such that they perform different tasks based on some condition .
- Coincidental cohesion is the lowest level of cohesion, where the elements within a module are not related at all and are grouped arbitrarily .

: Software Engineering | Coupling and Cohesion - GeeksforGeeks
: Coupling (computer programming) - Wikipedia
: Coupling vs Cohesion | Top Comparison to Learn with Infographics - EDUCBA
: The basics of software coupling metrics and concepts
: Software Engineering | Coupling and Cohesion - javatpoint