 Here are the notes for the topic "Programming in the Large" for Unit 3 - Object Oriented Analysis:

### Programming in the Large

1. Modularize the system into components
- Split the system into modules (components/packages) that have distinct functions
- Clear definition of interfaces between modules
- Low coupling between modules
- High cohesion within modules

2. Use abstract data types to define interfaces
- Define interfaces of modules in terms of abstract data types, not concrete implementations
- Changes in implementation should not affect interfaces
- Examples: stacks, queues, lists, etc.

3. Develop the main program as a control structure
- The main program acts as a control structure that coordinates the components
- It should not do much "actual work" - delegate this to components
- The control structure can be event-driven or based on a main loop

4. Support hierarchical decomposition
- System can be hierarchically decomposed into nested subsystems
- Allows complex systems to be managed in a structured way
- Applies the same principles of modularity at each level of the hierarchy

5. Use libraries to reuse components
- Develop/use reusable components/libraries to avoid reinventing the wheel
- Libraries allow sharing/reuse of trusted, robust components
- Need well-defined interfaces to use libraries

6. Use abstraction mechanisms to hide details
- Use abstraction to hide complexity and separate interface from implementation
- Examples: abstract data types, classes/objects, modules, etc.
- Encapsulation and information-hiding are key OO concepts to manage complexity

7. Apply design patterns to common problems
- Reusable solutions to common design problems
- Provide templates/recipes to tackle recurring design issues
- Examples: singleton, factory, observer, decorator, etc.
- Allow us to leverage expert experience in design

8. Use modelling and prototyping to experiment
- Model/prototype the system to experiment with different designs
- Helps identify/resolve design issues early before implementation
- Examples: UML diagrams, simulation/simulation prototyping, etc.
- Iteratively refine models/prototypes as more is understood about the problem