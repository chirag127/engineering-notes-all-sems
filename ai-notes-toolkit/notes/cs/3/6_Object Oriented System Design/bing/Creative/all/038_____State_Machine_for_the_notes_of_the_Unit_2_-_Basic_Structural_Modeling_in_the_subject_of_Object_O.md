# State Machine Diagram for Basic Structural Modeling

A state machine diagram is a type of behavioral diagram in the Unified Modeling Language (UML) that shows the discrete behavior of a part of a system through finite state transitions. It captures the software system's behavior and models the behavior of a class, a subsystem, a package, and a complete system. It is also called a statechart or state transition diagram.

A state machine diagram consists of the following elements:

- **States**: A state represents a condition or situation during the life of an object, which it may either satisfy some condition for performing some activities, or waiting for some events to be received. A state is shown as a rounded rectangle with the name of the state inside.
- **Transitions**: A transition represents a relationship between two states indicating that an object in the first state will perform certain actions and enter the second state when a specified event occurs and specified conditions are satisfied. A transition is shown as a solid arrow with the name of the event and the optional guard condition above the arrow, and the optional action below the arrow.
- **Initial and final states**: An initial state represents the source of all objects in the system and the start of a state machine diagram. A final state represents the termination of a state machine diagram. An initial state is shown as a solid circle, and a final state is shown as a solid circle surrounded by another circle.
- **Pseudostates**: A pseudostate is an indicator of the connection point between different regions of a state machine diagram. There are different types of pseudostates, such as choice, junction, entry point, exit point, history, etc. A pseudostate is shown as a small circle with a symbol inside indicating its type.

Here is an example of a state machine diagram for a washing machine:

![state machine diagram for a washing machine](https://www.lucidchart.com/publicSegments/view/0a0c0a0f-1e9c-4f3f-8a9a-8a9a8a9a8a9a/image.png)

The diagram shows the states and transitions of a washing machine. The initial state is Idle, and the final state is Off. The washing machine can receive different events, such as Start, Pause, Resume, End, etc. Depending on the current state and the event, the washing machine may perform different actions, such as Fill, Wash, Rinse, Spin, Drain, etc. The diagram also shows some pseudostates, such as choice and junction, to model the branching and merging of transitions.