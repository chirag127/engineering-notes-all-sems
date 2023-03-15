### State Chart Diagram for Unit 1 - Introduction of Software Engineering Lab

- A state chart diagram is a type of behavioral diagram in the Unified Modeling Language (UML) that shows the transitions between various states of an object or a system .
- A state is a condition in which an object exists and it changes when some event is triggered .
- A state transition is a link between two states that represents how an object or a system can move from one state to another .
- A state chart diagram can be used to model the behavior of a class, a subsystem, a package, or even an entire system .
- A state chart diagram can also show the actions and activities that are performed in each state, the events that trigger the transitions, and the guards that control the flow of execution  .
- A state chart diagram can have the following elements  :
  - Initial state: The starting point of the state machine. It is represented by a black circle.
  - Final state: The ending point of the state machine. It is represented by a black circle with a white circle inside.
  - Simple state: A state that does not have any substates. It is represented by a rounded rectangle with the name of the state inside.
  - Composite state: A state that has one or more substates. It is represented by a rounded rectangle with the name of the state and a dashed line dividing the substates.
  - Concurrent state: A state that has two or more regions that can execute simultaneously. It is represented by a rounded rectangle with the name of the state and a solid line dividing the regions.
  - Submachine state: A state that refers to another state machine diagram. It is represented by a rounded rectangle with the name of the state and a small circle with a cross inside.
  - Transition: A link between two states that shows the movement from one state to another. It is represented by a solid line with an arrowhead pointing to the target state. It can have an optional label that shows the event, guard, and action of the transition.
  - Event: A stimulus that triggers a transition. It is represented by a name followed by an optional list of parameters in parentheses.
  - Guard: A condition that must be true for a transition to occur. It is represented by a boolean expression in square brackets.
  - Action: An activity that is performed when a transition occurs. It is represented by a name followed by an optional list of parameters in parentheses.
  - Entry action: An action that is performed when a state is entered. It is represented by the keyword "entry" followed by a slash and the action.
  - Exit action: An action that is performed when a state is exited. It is represented by the keyword "exit" followed by a slash and the action.
  - Do activity: An action that is performed continuously while a state is active. It is represented by the keyword "do" followed by a slash and the action.
  - History state: A pseudo-state that remembers the last active substate of a composite state. It is represented by a circle with a letter H inside. It can be shallow or deep, depending on whether it remembers only the direct substate or all the nested substates.
  - Choice state: A pseudo-state that represents a branching point based on a guard condition. It is represented by a diamond with one incoming transition and two or more outgoing transitions.
  - Junction state: A pseudo-state that represents a merging point of two or more transitions. It is represented by a diamond with two or more incoming transitions and one outgoing transition.
  - Fork state: A pseudo-state that represents a splitting point of one transition into two or more concurrent regions. It is represented by a horizontal or vertical bar with one incoming transition and two or more outgoing transitions.
  - Join state: A pseudo-state that represents a joining point of two or more concurrent regions into one transition. It is represented by a horizontal or vertical bar with two or more incoming transitions and one outgoing transition.
  - Terminate state: A pseudo-state that represents the termination of the entire state machine. It is represented by a circle with a cross inside.

- An example of a state chart diagram for a door object is shown below:

![State chart diagram for a door object](https://science-atlas.com/wp-content/uploads/2021/10/State-M