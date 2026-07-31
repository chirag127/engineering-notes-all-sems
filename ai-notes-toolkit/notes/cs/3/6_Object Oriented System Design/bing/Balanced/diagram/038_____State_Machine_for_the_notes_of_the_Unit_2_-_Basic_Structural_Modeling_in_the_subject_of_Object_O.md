### State Machine Diagram

A state machine diagram is a type of behavioral diagram in the Unified Modeling Language (UML) that shows the discrete behavior of a part of a system through finite state transitions. It captures the software system's behavior and models the behavior of a class, a subsystem, a package, and a complete system .

A state machine diagram consists of the following elements:

- **States**: A state represents a condition or situation during the life of an object, which it may either satisfy some condition for performing some activities, or waiting for some events to be received. A state is shown as a rounded rectangle with the name of the state inside .
- **Transitions**: A transition represents a change in the state of an object due to an event or an action. A transition is shown as a solid arrow from the source state to the target state, with the name of the event or action above the arrow .
- **Initial state**: An initial state represents the starting point of a state machine diagram. It is shown as a black circle .
- **Final state**: A final state represents the end point of a state machine diagram. It is shown as a black circle with a white circle inside .
- **Choice**: A choice represents a branching point where the outcome is decided by a guard condition. It is shown as a diamond with one incoming transition and two or more outgoing transitions, each with a guard condition in square brackets .
- **Junction**: A junction represents a point where multiple transitions converge into one. It is shown as a small black circle with one incoming transition and one outgoing transition .
- **Fork**: A fork represents a point where a single transition splits into two or more parallel transitions. It is shown as a horizontal or vertical black bar with one incoming transition and two or more outgoing transitions .
- **Join**: A join represents a point where two or more parallel transitions merge into one. It is shown as a horizontal or vertical black bar with two or more incoming transitions and one outgoing transition .
- **History**: A history represents a point where the state machine remembers the last active state of a region. It is shown as a circle with a letter H inside .
- **Entry point**: An entry point represents a point where an external transition enters a composite state. It is shown as a small circle on the border of the composite state .
- **Exit point**: An exit point represents a point where an internal transition exits a composite state. It is shown as a small circle with a cross inside on the border of the composite state .
- **Submachine state**: A submachine state represents a state that is defined by another state machine diagram. It is shown as a rounded rectangle with the name of the submachine state and a small icon of a state machine diagram inside .

The following is an example of a state machine diagram for a microwave oven:

![State machine diagram for a microwave oven](https://www.javatpoint.com/images/uml/uml_state_machine_diagram.png)

The diagram shows the states and transitions of the microwave oven, such as:

- The initial state is **Off**.
- When the user presses the **Start** button, the oven transitions to the **Cooking** state and starts the timer.
- When the timer reaches zero, the oven transitions to the **Beeping** state and beeps.
- When the user presses the **Stop** button, the oven transitions to the **Off** state and stops beeping.
- The oven also has a choice point where it can transition to the **Paused** state if the user presses the **Pause** button while cooking or beeping.
- The oven also has a junction point where it can resume cooking or beeping from the **Paused** state if the user presses the **Resume** button.
- The oven also has a fork and join point where it can split and merge the **Cooking** and **Beeping** states into parallel regions. This allows the oven to cook and beep at the same time.