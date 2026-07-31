# State Chart Diagram for Unit 1 - Introduction of Software Engineering Lab

- A state chart diagram is a type of behavioral diagram in the Unified Modeling Language (UML) that shows the transitions between various states of an object or a system .
- A state is a condition in which an object exists and it changes when some event is triggered .
- A state transition is a link between two states that represents how the object or the system moves from one state to another .
- A state chart diagram can be used to model the behavior of a class, a subsystem, a package, or even an entire system .
- A state chart diagram can also show the events that trigger the transitions, the actions that are performed during the transitions or in the states, and the guards that control the flow of the transitions  .

## Example of a State Chart Diagram

- The following state chart diagram shows the states and transitions of a microwave oven.

![State Chart Diagram of a Microwave Oven](https://www.lucidchart.com/publicSegments/view/9a0c0f6f-9f8c-4a3a-8c7f-9a0c0f6f9f8c/image.png)

- The initial state is represented by a black circle and the final state is represented by a black circle with a white circle inside.
- The microwave oven has four states: Idle, Cooking, Paused, and Door Open.
- The transitions between the states are triggered by events such as Start, Stop, Pause, Resume, Open Door, and Close Door.
- The transitions can also have guards, such as [time > 0], which indicate the condition that must be true for the transition to occur.
- The transitions can also have actions, such as reset timer, which indicate the operation that is performed during the transition.
- The states can also have actions, such as heat food, which indicate the operation that is performed while the object or the system is in that state.