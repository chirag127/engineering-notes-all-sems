### Formulating Network Model in spm

- A network model is a graphical representation of the activities and their interrelationships in a software project.
- A network model can help to plan, schedule, monitor and control the project activities, resources and costs.
- A network model can also help to identify the critical path, the slack time, the float time and the project duration.
- There are two main methods of formulating a network model: activity-on-node (AON) and activity-on-arrow (AOA).
- In AON, the activities are represented as nodes (boxes) and the dependencies are represented as arrows (lines) between the nodes.
- In AOA, the activities are represented as arrows (lines) and the events are represented as nodes (circles).
- AON is more commonly used than AOA because it is easier to draw and modify, and it can handle complex dependencies and dummy activities.
- A network model can be constructed by following these steps:
  - Identify the activities and their dependencies. Use a work breakdown structure (WBS) or a precedence diagram to help with this step.
  - Assign a unique identifier and an estimated duration to each activity.
  - Draw the network diagram using either AON or AOA method. Start from the initial node and follow the dependencies until the final node. Make sure there are no loops or isolated nodes in the diagram.
  - Label the nodes and the arrows with the activity identifiers and durations.
  - Check the network diagram for accuracy and completeness.

- Here is an example of a network model for a software project using AON method:

```
  A(3)   B(4)   C(2)   D(5)   E(6)   F(4)   G(3)
  |      |      |      |      |      |      |
  v      v      v      v      v      v      v
+---+  +---+  +---+  +---+  +---+  +---+  +---+
|   |->|   |->|   |->|   |->|   |->|   |->|   |
+---+  +---+  +---+  +---+  +---+  +---+  +---+
  ^      ^      ^      ^      ^      ^      ^
  |      |      |      |      |      |      |
  H(2)   I(3)   J(4)   K(3)   L(2)   M(5)   N(4)
```

- A mnemonic to remember the steps of formulating a network model is: **IADLC** (Identify, Assign, Draw, Label, Check).