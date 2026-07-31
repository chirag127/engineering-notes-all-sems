```markdown
### Sequence Diagrams

- Sequence diagrams are a type of interaction diagram that show how objects interact with each other in a time-ordered sequence.
- Sequence diagrams are useful for modeling the dynamic behavior of a system, such as the interactions between objects in a use case or scenario.
- Sequence diagrams consist of vertical lifelines that represent the objects involved in the interaction, and horizontal arrows that represent the messages exchanged between the objects.
- The messages can be synchronous (solid arrowhead), asynchronous (open arrowhead), or reply (dashed arrowhead). The messages can also have labels that indicate the name, parameters, and return value of the operation invoked by the message.
- The messages are arranged from top to bottom according to the chronological order of their occurrence. The vertical dashed lines that extend from the lifelines indicate the duration of the object's existence and participation in the interaction.
- Sequence diagrams can also show alternative, optional, or concurrent flows of events using fragments, such as alt, opt, par, loop, etc. Fragments are enclosed by a frame with a label that indicates the type and condition of the fragment.
- Sequence diagrams can also show the creation and destruction of objects using the create and destroy messages. The create message has a dashed line and an open arrowhead, and the destroy message has a cross at the end of the arrow.
- Sequence diagrams can also show the activation and deactivation of objects using the activation bars. The activation bars are thin rectangles that cover the lifelines and indicate the period of time when the object is active or executing an operation.
- Sequence diagrams can also show the nesting of messages using the return arrows. The return arrows are dashed lines that point back to the sender of the message and indicate the return value of the operation.
- Sequence diagrams can also show the interaction between different diagrams using the ref fragment. The ref fragment is a frame with a label that indicates the name of the referenced diagram.

Here is an example of a sequence diagram for making a hotel reservation:

![sequence diagram example](https://www.visual-paradigm.com/guide/wp-content/uploads/2018/12/sequence-diagram-example-hotel-reservation.png)
```