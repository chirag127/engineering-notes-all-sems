### Activity Diagrams

- Activity diagrams are a type of behavior diagrams that show the flow of control and data among activities in a system.
- Activity diagrams are also called object-oriented flowcharts because they capture the dynamic behavior of the system in terms of objects and their interactions.
- Activity diagrams consist of activities, actions, control nodes, object nodes, and edges that connect them.
- An activity is a behavior that is divided into one or more actions. An action is an atomic operation that can be executed by the system or an actor.
- A control node is a point in the flow of control that can change the direction or terminate the flow. Examples of control nodes are initial nodes, final nodes, decision nodes, merge nodes, fork nodes, and join nodes.
- An object node is a point in the flow of data that can store, create, or destroy objects. Examples of object nodes are object flows, pins, and parameter nodes.
- An edge is a connection between two nodes that shows the direction of the flow of control or data. Examples of edges are control flows, object flows, and exception flows.
- Activity diagrams can be used to model the workflow of a system, the use cases of a system, or the business processes of an organization.
- Activity diagrams can also be used to model the concurrent and parallel behavior of a system, such as multitasking, synchronization, and communication.
- Activity diagrams can be drawn at different levels of abstraction, from a high-level overview of the system to a detailed specification of a single action.

Here is an example of an activity diagram that models the workflow for a word processor to create a document:

```markdown
![Activity Diagram Example](activity_diagram_example.png)

Activity Diagram Example

- The initial node (a solid circle) marks the start of the workflow.
- The final node (a solid circle inside a hollow circle) marks the end of the workflow.
- The activity "Create a document" is composed of four actions: "Open the word processing package", "Create a file", "Save the file", and "Type the document".
- The control flows (solid arrows) show the sequence of actions.
- The object flows (dashed arrows) show the flow of data between actions. The object "File" is created by the action "Create a file" and stored by the action "Save the file".
- The decision node (a diamond) shows a point where the flow of control can branch based on a condition. In this case, the condition is whether the user wants to save the file or not.
- The merge node (a diamond) shows a point where the flow of control can converge from different branches. In this case, the merge node is used to join the two branches after the decision node.
- The fork node (a horizontal bar) shows a point where the flow of control can split into multiple concurrent flows. In this case, the fork node is used to start two parallel actions: "Save the file" and "Type the document".
- The join node (a horizontal bar) shows a point where the flow of control can synchronize from multiple concurrent flows. In this case, the join node is used to end the two parallel actions and resume the sequential flow.
```