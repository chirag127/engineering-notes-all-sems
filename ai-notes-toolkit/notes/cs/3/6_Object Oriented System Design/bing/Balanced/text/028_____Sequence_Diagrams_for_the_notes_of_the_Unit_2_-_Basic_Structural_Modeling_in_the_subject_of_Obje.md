### Sequence Diagrams

- Sequence diagrams are a type of interaction diagram that show how objects interact with each other in a time-ordered manner.
- Sequence diagrams are useful for modeling the dynamic behavior of a system, such as the flow of messages and events between objects in a use case scenario.
- Sequence diagrams consist of the following elements:
  - Objects: The entities that participate in the interaction. They are represented by vertical lifelines with the object name on top.
  - Messages: The communication between objects. They are represented by horizontal arrows with the message name and optional arguments on top. Messages can be synchronous (solid arrowhead), asynchronous (open arrowhead), or reply (dashed arrowhead).
  - Activation: The period of time when an object is performing an action or waiting for a reply. It is represented by a thin or thick rectangle on the lifeline.
  - Lifespan: The duration of an object's existence. It is represented by a dashed line that extends from the creation to the destruction of the object. An object can be created by a message (solid arrowhead with a dashed line) or destroyed by a message (crossed circle with a dashed line).
  - Combined fragments: The sections of the interaction that show conditional or iterative behavior. They are represented by a frame with an operator (such as alt, opt, loop, etc.) and a guard condition on the top left corner. The frame encloses the messages that belong to the fragment.
  - Interaction use: The reuse of another interaction diagram within a sequence diagram. It is represented by a frame with the keyword ref and the name of the reused diagram on the top left corner. The frame encloses the parameters and return values of the interaction.
  - Timing constraints: The specification of the time interval or duration of a message or an event. They are represented by brackets with the constraint expression on the message arrow or the lifeline.
- Sequence diagrams follow some basic rules and guidelines, such as:
  - The objects are arranged from left to right according to the order of their creation or involvement in the interaction.
  - The messages are arranged from top to bottom according to the chronological order of their occurrence.
  - The messages should have meaningful and consistent names that reflect the intention and functionality of the interaction.
  - The activation and lifespan of an object should be consistent with the messages it sends and receives.
  - The combined fragments and interaction uses should be used to simplify and modularize the interaction.
  - The timing constraints should be used to specify the temporal aspects of the interaction.

- Here is an example of a sequence diagram for making a hotel reservation:

![sequence diagram example](https://www.visual-paradigm.com/guide/wp-content/uploads/2016/12/sequence-diagram-hotel-reservation.png)