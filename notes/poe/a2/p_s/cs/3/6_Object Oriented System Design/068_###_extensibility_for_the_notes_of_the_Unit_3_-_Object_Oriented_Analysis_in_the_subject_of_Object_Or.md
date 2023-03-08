 Here is the content in markdown format for the topic ### extensibility for the notes of the Unit 3 - Object Oriented Analysis in the subject of Object Oriented System Design:

## Extensibility

- Extensibility refers to the ability of a system to easily accommodate new or changed requirements without significant modifications to the system.
- An extensible system anticipates potential changes and is designed and developed in such a way that it can be easily extended with new components, modules, or functions.
- Some key ways to achieve extensibility are:
    - Loose coupling between components - Minimize dependencies between components so that changes in one component do not affect others. This can be achieved using interfaces and abstract classes.
    - Use of interfaces - Define interfaces for components which specify what functionalities they must have rather than how they must be implemented. This enables alternate implementations to be easily plugged in.
    - Configuration over convention - Rely on external configuration rather than hardcoded conventions so that behavior can be easily modified by updating the configuration.
    - Separation of concerns - Implement components that have a single focused purpose. This makes them more reusable and replaceable.
    - Use of design patterns - Apply design patterns like strategy, observer, factory, etc. which promote loose coupling and flexible behavior.
- Advantages of extensibility:
    - Prepares the system for change - An extensible system is ready for evolving requirements and can accommodate enhancements and modifications easily.
    - Reduces cost of change - Since changes can be implemented easily by plugging in new modules or components, the cost of change is lower.
    - Increases maintainability - As the system design has anticipated changes, it is more robust and maintainable in the face of modifications.
- Disadvantages of extensibility:
    - May lead to overengineering - If extensibility is implemented when not required, it may introduce unneeded complexity and extra effort.
    - Difficult to implement - Achieving a truly extensible system requires skill and experience and it may not be feasible for every system.