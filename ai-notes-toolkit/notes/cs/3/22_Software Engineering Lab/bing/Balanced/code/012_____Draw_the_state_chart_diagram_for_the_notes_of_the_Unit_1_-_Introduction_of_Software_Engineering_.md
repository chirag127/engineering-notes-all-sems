### State Chart Diagram for Unit 1 - Introduction of Software Engineering Lab

- A state chart diagram is a type of behavioral diagram in UML that shows the transitions between various states of an object or a system in response to events   .
- A state is a condition in which an object exists and it changes when some event is triggered .
- A state transition is a relationship between two states that indicates that an object in the first state will perform certain actions and enter the second state when a specified event occurs and specified conditions are satisfied .
- A state chart diagram consists of the following elements  :
  - Initial state: The starting point of a state machine diagram, denoted by a solid circle.
  - Final state: The ending point of a state machine diagram, denoted by a solid circle inside another circle.
  - Simple state: A state that does not have any substates, denoted by a rectangle with rounded corners and a name inside.
  - Composite state: A state that has one or more substates, denoted by a rectangle with rounded corners and a name inside, and a dashed line dividing the substates.
  - Concurrent state: A composite state that has two or more substates that can be active at the same time, denoted by a rectangle with rounded corners and a name inside, and a dashed line dividing the substates, and a fork symbol at the entry and exit points.
  - Transition: A directed line connecting two states, with an optional event name, guard condition, and action expression along the line.
  - Event: A stimulus that triggers a transition from one state to another.
  - Guard condition: A boolean expression that must be true for a transition to occur, enclosed in square brackets.
  - Action expression: A specification of the actions to be performed when a transition occurs, preceded by a slash.
  - History state: A pseudo-state that represents the last active state of a composite state, denoted by a circle with a letter H inside.
  - Entry action: An action that is performed when an object enters a state, preceded by the keyword entry.
  - Exit action: An action that is performed when an object exits a state, preceded by the keyword exit.
  - Do activity: An action that is performed continuously while an object is in a state, preceded by the keyword do.

- An example of a state chart diagram for a microwave oven is shown below:

![State chart diagram for a microwave oven](https://www.guru99.com/images/1/022519_0647_StateMachin1.png)

- The diagram shows the following states and transitions for the microwave oven:
  - Off: The initial state of the microwave oven, where it is not in use.
  - Idle: The state where the microwave oven is waiting for the user to enter the cooking time and press the start button.
  - Cooking: The state where the microwave oven is heating the food for the specified time.
  - Paused: The state where the microwave oven is temporarily stopped by the user or by opening the door.
  - Beeping: The final state of the microwave oven, where it is beeping to indicate that the cooking is done.
  - The transitions between the states are triggered by the following events and actions:
    - Press power button: The event that causes the microwave oven to switch from the Off state to the Idle state, and vice versa.
    - Enter time: The event that causes the user to enter the cooking time in the Idle state.
    - Press start button: The event that causes the microwave oven to start cooking in the Idle state, and to resume cooking in the Paused state.
    - Timer reaches zero: The event that causes the microwave oven to stop cooking in the Cooking state, and to start beeping in the Beeping state.
    - Press stop button: The event that causes the microwave oven to stop cooking in the Cooking state, and to stop beeping in the Beeping state, and to return to the Idle state.
    - Open door: The event that causes the microwave oven to pause cooking in the Cooking state, and to stop beeping in the Beeping state, and to enter the Paused state.
    - Close door: The event that causes the microwave oven to resume cooking in the Paused state, and to return to the Idle state.
    - The actions performed by the microwave oven during the transitions