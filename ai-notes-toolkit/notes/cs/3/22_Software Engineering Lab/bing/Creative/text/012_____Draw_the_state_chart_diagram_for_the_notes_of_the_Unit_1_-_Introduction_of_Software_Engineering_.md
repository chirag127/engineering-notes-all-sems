### State Chart Diagram for the Notes of the Unit 1 - Introduction of Software Engineering Lab

- A state chart diagram is a type of behavioral diagram that shows the possible states of an object and the transitions between them  .
- A state is a condition or situation in which an object exists during its lifetime .
- A transition is a change from one state to another, triggered by an event or a condition .
- A state chart diagram can be used to model the behavior of a class, a subsystem, a package, or an entire system .
- A state chart diagram consists of the following elements  :
  - Initial state: The starting point of the state machine, denoted by a solid circle.
  - Final state: The ending point of the state machine, denoted by a solid circle with a hollow circle inside.
  - Simple state: A state that does not have any substates, denoted by a rounded rectangle with the state name inside.
  - Composite state: A state that has one or more substates, denoted by a rounded rectangle with the state name and a dashed line separating the substates.
  - Concurrent state: A state that has two or more regions that can execute simultaneously, denoted by a rounded rectangle with the state name and a solid line separating the regions.
  - Transition: A directed line connecting two states, with an optional event name, guard condition, and action expression on the line.
  - Event: A stimulus that triggers a transition, such as a user input, a timer, or a signal.
  - Guard condition: A boolean expression that must be true for a transition to occur, enclosed in square brackets.
  - Action expression: A statement that specifies what actions to perform when a transition occurs, preceded by a slash.
  - Entry action: An action that is executed when a state is entered, preceded by the keyword "entry".
  - Exit action: An action that is executed when a state is exited, preceded by the keyword "exit".
  - Do activity: An action that is executed continuously while a state is active, preceded by the keyword "do".
- A state chart diagram can be drawn using the following steps:
  - Identify the object or system whose behavior you want to model.
  - Identify the possible states of the object or system and their attributes.
  - Identify the events or conditions that cause the object or system to change from one state to another.
  - Identify the actions or activities that the object or system performs in each state or during each transition.
  - Draw the initial state and the final state using the appropriate symbols.
  - Draw the simple states, composite states, and concurrent states using the appropriate symbols and labels.
  - Draw the transitions between the states using the appropriate symbols and labels.
  - Add the entry actions, exit actions, and do activities to the states using the appropriate syntax.
  - Verify the completeness and correctness of the state chart diagram.

Here is an example of a state chart diagram for a door object, based on the information from :

![State chart diagram for a door object](https://science-atlas.com/wp-content/uploads/2021/10/Statechart-diagram-for-a-door-object.png)

: https://science-atlas.com/faq/what-is-state-chart-diagram-in-software-engineering/
: https://www.guru99.com/state-machine-transition-diagram.html
: https://www.tutorialspoint.com/uml/uml_statechart_diagram.htm
: https://www.lucidchart.com/pages/uml-state-machine-diagram
: https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-state-machine-diagram/