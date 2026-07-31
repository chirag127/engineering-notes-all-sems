# State Chart Diagram for Unit 1 - Introduction of Software Engineering Lab

- A state chart diagram is a type of behavioral diagram in UML that shows the transitions between various states of an object or a system in response to events   .
- A state is a condition in which an object or a system exists and it changes when some event is triggered .
- A state transition is a link between two states that indicates that the object or the system will change from the source state to the target state when a certain event occurs and a certain condition is satisfied .
- A state chart diagram consists of the following elements   :
  - Initial state: The state of an object or a system before any event occurs. It is represented by a solid circle.
  - Final state: The state of an object or a system when it is terminated or completed. It is represented by a solid circle with a hollow circle inside it.
  - Simple state: A state that does not have any substates or regions. It is represented by a rounded rectangle with the name of the state inside it.
  - Composite state: A state that has one or more substates or regions. It is represented by a rounded rectangle with the name of the state and a dashed line dividing the substates or regions inside it.
  - Substate: A state that is nested within a composite state. It is represented by a rounded rectangle with the name of the state inside it.
  - Region: A part of a composite state that can have concurrent substates. It is represented by a dashed line dividing the substates inside it.
  - Transition: A link between two states that indicates the change of state. It is represented by a solid arrow with the name of the event and the condition (optional) above it.
  - Fork: A pseudo-state that splits a transition into two or more parallel transitions. It is represented by a solid bar with one incoming transition and two or more outgoing transitions.
  - Join: A pseudo-state that merges two or more parallel transitions into one transition. It is represented by a solid bar with two or more incoming transitions and one outgoing transition.
  - Choice: A pseudo-state that selects one of the outgoing transitions based on a condition. It is represented by a hollow diamond with one incoming transition and two or more outgoing transitions.
  - Junction: A pseudo-state that joins two or more incoming transitions into one outgoing transition. It is represented by a solid diamond with two or more incoming transitions and one outgoing transition.
  - History: A pseudo-state that remembers the previous state of a composite state or a region. It is represented by a solid circle with a letter H inside it.
  - Entry point: A pseudo-state that defines an entry point for a composite state or a region. It is represented by a small solid circle with a transition pointing to it.
  - Exit point: A pseudo-state that defines an exit point for a composite state or a region. It is represented by a small solid circle with a transition pointing from it.
  - Terminate: A pseudo-state that indicates the termination of the object or the system. It is represented by a solid circle with a cross inside it.

- An example of a state chart diagram for a door is shown below:

![State chart diagram for a door](https://science-atlas.com/wp-content/uploads/2021/10/Statechart-diagram-for-a-door.png)

: https://science-atlas.com/faq/what-is-state-chart-diagram-in-software-engineering/
: https://www.guru99.com/state-machine-transition-diagram.html
: https://www.tutorialspoint.com/uml/uml_statechart_diagram.htm
: https://www.lucidchart.com/pages/uml-state-machine-diagram
: https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-state-machine-diagram/