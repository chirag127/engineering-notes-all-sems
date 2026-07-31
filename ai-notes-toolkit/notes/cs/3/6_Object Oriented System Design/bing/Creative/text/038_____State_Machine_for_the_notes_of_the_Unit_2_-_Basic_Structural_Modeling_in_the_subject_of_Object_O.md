### State Machine for the notes of the Unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design

- A state machine diagram is a type of behavioral diagram in the Unified Modeling Language (UML) that shows the discrete behavior of a part of a system through finite state transitions.
- A state machine diagram can model the behavior of a class, a subsystem, a package, or a complete system .
- A state machine diagram consists of the following elements  :
  - States: The possible conditions or situations of an object in the system. A state is represented by a rounded rectangle with the name of the state inside.
  - Transitions: The changes from one state to another. A transition is represented by a directed line with an arrowhead and an optional label that indicates the event or condition that triggers the transition.
  - Initial state: The starting point of the state machine diagram. An initial state is represented by a solid circle.
  - Final state: The ending point of the state machine diagram. A final state is represented by a solid circle inside another circle.
  - Choice: A branching point that indicates a conditional transition. A choice is represented by a diamond with one incoming transition and two or more outgoing transitions.
  - Junction: A merging point that indicates a concurrent transition. A junction is represented by a diamond with two or more incoming transitions and one outgoing transition.
  - History: A pseudo-state that remembers the previous state of an object. A history is represented by a circle with a letter H inside.
  - Entry/Exit actions: The actions that are performed when an object enters or exits a state. Entry/Exit actions are represented by the keywords entry or exit followed by a slash and the action name.
  - Guards: The expressions that evaluate to true or false and determine whether a transition can be taken or not. Guards are represented by square brackets enclosing the expression.
  - Events: The occurrences that trigger a transition. Events are represented by the name of the event followed by an optional list of parameters in parentheses.
  - Actions: The activities that are performed as a result of a transition. Actions are represented by a slash followed by the action name and an optional list of parameters in parentheses.

- An example of a state machine diagram for a vending machine is shown below:

![State machine diagram for a vending machine](https://www.lucidchart.com/publicSegments/view/6f9f9f0a-9c2f-4f6a-8f5a-6f9f9f0a-9c2f-4f6a-8f5a-6f9f9f0a-9c2f-4f6a-8f5a-6f9f9f0a-9c2f-4f6a-8f5a-6f9f9f0a-9c2f-4f6a-8f5a-6f9f9f0a-9c2f-4f6a-8f5a-6f9f9f0a-9c2f-4f6a-8f5a-6f9f9f0a-9c2f-4f6a-8f5a-6f9f9f0a-9c2f-4f6a-8f5a-6f9f9f0a-9c2f-4f6a-8f5a-6f9f9f0a-9c2f-4f6a-8f5a-6f9f9f0a-9c2f-4f6a-8f5a-6f9f9f0a-9c2f-4f6a-8f5a-6f9f9f0a-9c2f-4f6a-8f5a-6f9f9f0a-9c2f-4f6a-8f5a-6f9f9f0a-9c2f-4f6a-8f5a-6f9f9f0a-9c2f-4f6a-8f5a-6f9f9f0a-9c2f-4f6a-8f5a-6