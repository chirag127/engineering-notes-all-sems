# Sequence Diagrams

- Sequence diagrams are a type of interaction diagram that show how objects interact with each other in a time-ordered manner.
- Sequence diagrams are useful for modeling the dynamic behavior of a system, such as the interactions between objects in a use case or scenario.
- Sequence diagrams consist of vertical lifelines that represent the objects or classes involved in the interaction, and horizontal arrows that represent the messages exchanged between them.
- Sequence diagrams can also show the activation of objects, the creation and destruction of objects, the return of values, the use of alternative and parallel flows, and the use of loops and conditions.
- Sequence diagrams are related to other UML diagrams, such as class diagrams, communication diagrams, state machine diagrams, and activity diagrams.

## Elements of a Sequence Diagram

- A sequence diagram has the following elements:

  - **Lifeline**: A lifeline represents an individual participant in the interaction. It is a vertical dashed line that shows the existence of an object or class over time. A lifeline can have a name and a type, which are usually shown in the format of `name : type`. A lifeline can also have a selector, which is an expression that specifies which instance of a class is being referred to, such as `name[index] : type` or `name->role : type`.
  - **Message**: A message represents a communication between two lifelines. It is a horizontal arrow that shows the flow of information from the sender to the receiver. A message can have a name, which is usually a verb or an operation, and optionally some arguments, which are shown in parentheses. A message can also have a sequence number, which is a hierarchical numbering scheme that indicates the order of messages in the interaction. A message can have different types, such as synchronous, asynchronous, reply, create, destroy, etc., which are shown by different arrow styles and labels.
  - **Execution specification**: An execution specification represents the period of time during which a lifeline is performing an action or waiting for a response. It is a thin or thick rectangle that covers a portion of a lifeline. An execution specification can have a name, which is usually the same as the message that initiates it, and optionally some arguments, which are shown in parentheses. An execution specification can also have a stereotype, which is a keyword that indicates the kind of action or behavior, such as `<<call>>`, `<<send>>`, `<<receive>>`, etc.
  - **Combined fragment**: A combined fragment represents a combination of messages that are grouped together to show some structural or behavioral aspect of the interaction. It is a large rectangle that encloses a part of the interaction. A combined fragment can have a name, which is usually the same as the operator that defines its semantics, such as `alt`, `opt`, `par`, `loop`, `break`, etc. A combined fragment can also have a guard, which is a boolean expression that specifies the condition for the execution of the fragment. A combined fragment can have one or more operands, which are the sub-sequences of messages that are executed depending on the operator and the guard.
  - **Interaction use**: An interaction use represents a reference to another interaction that occurs at some point in the current interaction. It is a large rectangle with a pentagonal tab that covers a part of the interaction. An interaction use can have a name, which is usually the same as the name of the referenced interaction, and optionally some arguments, which are shown in parentheses. An interaction use can also have a return value, which is the result of the execution of the referenced interaction, and is shown in brackets.
  - **Frame**: A frame represents the boundary of a sequence diagram. It is a large rectangle that encloses the whole diagram. A frame can have a name, which is usually the same as the name of the interaction, and optionally some parameters, which are shown in parentheses. A frame can also have a stereotype, which is a keyword that indicates the type of the diagram, such as `sd` for sequence diagram, `ref` for interaction use, etc.

## Example of a Sequence Diagram

- Below is an example of a sequence diagram for making a hotel reservation, based on the search result :

![sequence diagram example](https://www.visual-paradigm.com/guide/wp-content/uploads/2018/12/sequence-diagram-example-hotel-reservation.png)

- The sequence diagram shows the following elements:

  - **Lifelines**: The lifelines are `Customer`, `:FrontDesk`, `:Hotel`, and `:Room`. The `Customer` lif