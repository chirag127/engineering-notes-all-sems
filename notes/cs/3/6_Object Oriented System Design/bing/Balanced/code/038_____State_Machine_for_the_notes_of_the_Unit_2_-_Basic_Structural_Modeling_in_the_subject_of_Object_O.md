### State Machine for the notes of the Unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design

- A state machine diagram is a type of behavioral diagram in the Unified Modeling Language (UML) that shows the discrete behavior of a part of a system through finite state transitions.
- A state machine diagram can model the behavior of a class, a subsystem, a package, or a complete system .
- A state machine diagram consists of the following elements  :
  - States: The possible conditions or situations of an object in the system. A state is represented by a rounded rectangle with the name of the state inside.
  - Transitions: The changes from one state to another. A transition is represented by a directed line with an arrowhead and an optional label that indicates the event or condition that triggers the transition.
  - Initial state: The starting point of the state machine diagram. An initial state is represented by a solid circle.
  - Final state: The ending point of the state machine diagram. A final state is represented by a solid circle inside another circle.
  - Choice: A branching point that allows multiple transitions based on different conditions or guards. A choice is represented by a diamond with one incoming transition and multiple outgoing transitions.
  - Junction: A merging point that allows multiple transitions to converge into one. A junction is represented by a diamond with multiple incoming transitions and one outgoing transition.
  - History: A pseudo-state that remembers the previous state of an object. A history state is represented by a circle with a letter H inside.
  - Submachine state: A state that contains another state machine diagram within it. A submachine state is represented by a rounded rectangle with a small circle at the bottom right corner.

- A state machine diagram can be used to describe the dynamic behavior of a system, such as the usage protocol, the life cycle, or the response to events  .
- A state machine diagram can also be used to design and simulate the system, as well as to generate code for implementation.

- An example of a state machine diagram for a vending machine is shown below:

![State machine diagram for a vending machine](https://www.lucidchart.com/publicSegments/view/9a9a0c6f-1f1f-4a8f-8c0a-9c1b00000000/image.png)

- The diagram shows the states of the vending machine, such as Idle, Waiting for selection, Waiting for payment, Dispensing item, and Out of order.
- The diagram also shows the transitions between the states, such as Select item, Insert coin, Cancel, Dispense, and Error.
- The diagram also shows the initial state, the final state, and a choice for selecting different items.