### State Machine for the notes of the Unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design

- A state machine diagram is a type of behavioral diagram in the Unified Modeling Language (UML) that shows the discrete behavior of a part of a system through finite state transitions.
- A state machine diagram can model the behavior of a class, a subsystem, a package, or a complete system .
- A state machine diagram consists of the following elements  :
  - **States**: The possible conditions or situations of an object in the system. A state is represented by a rounded rectangle with the name of the state inside.
  - **Transitions**: The changes from one state to another state. A transition is represented by a solid arrow with the name of the event or trigger that causes the transition above the arrow. Optionally, the name of the action or activity that occurs during the transition can be written below the arrow.
  - **Initial state**: The starting point of the state machine diagram. An initial state is represented by a solid circle.
  - **Final state**: The ending point of the state machine diagram. A final state is represented by a solid circle inside another circle.
  - **Choice**: A branching point that indicates a conditional transition. A choice is represented by a diamond with one incoming transition and two or more outgoing transitions. The guard conditions for each outgoing transition are written inside square brackets near the arrow.
  - **Composite state**: A state that contains other states within it. A composite state is represented by a rounded rectangle with a dashed line dividing the name of the state and the inner states. A composite state can have an initial state and a final state inside it.
  - **History state**: A state that remembers the last active state of a composite state. A history state is represented by a circle with the letter H inside. A transition from a history state to a composite state means that the composite state will resume from the last active state it had before leaving it.
  - **Entry/Exit actions**: The actions or activities that are performed when entering or exiting a state. Entry actions are written with the keyword "entry" followed by a slash and the name of the action. Exit actions are written with the keyword "exit" followed by a slash and the name of the action.
  - **Do activity**: The action or activity that is performed continuously while being in a state. Do activity is written with the keyword "do" followed by a slash and the name of the action.

- An example of a state machine diagram for a vending machine is shown below:

![State machine diagram for a vending machine](https://www.lucidchart.com/publicSegments/view/4a8a-4b4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a-4a4a-8a4a