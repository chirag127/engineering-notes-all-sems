#### Cohesion Measures in Software Design

Cohesion refers to the degree to which the elements of a module belong together. In software design, it is considered desirable to have high cohesion, as it indicates that the module is focused and well-defined. There are several measures of cohesion, including:

1. **Functional cohesion:** This is the strongest type of cohesion, where all elements of a module work together to perform a single, well-defined task.
2. **Sequential cohesion:** This type of cohesion occurs when the output of one element serves as the input for another element within the same module.
3. **Communicational cohesion:** This type of cohesion occurs when elements of a module operate on the same data or input.
4. **Procedural cohesion:** This type of cohesion occurs when elements of a module are grouped together because they are part of the same procedure or process.
5. **Temporal cohesion:** This type of cohesion occurs when elements of a module are grouped together because they are related in time, such as initialization or cleanup routines.
6. **Logical cohesion:** This type of cohesion occurs when elements of a module are grouped together because they are logically related, such as a group of error-handling routines.
7. **Coincidental cohesion:** This is the weakest type of cohesion, where elements of a module are grouped together arbitrarily, with no strong relationship between them.

High cohesion is desirable in software design because it makes the code easier to understand, maintain, and modify. It also promotes modularity and reusability, as modules with high cohesion can often be used in multiple contexts. In contrast, low cohesion can make the code more difficult to understand and maintain, and can lead to increased coupling between modules. Therefore, it is important to consider cohesion when designing software modules.