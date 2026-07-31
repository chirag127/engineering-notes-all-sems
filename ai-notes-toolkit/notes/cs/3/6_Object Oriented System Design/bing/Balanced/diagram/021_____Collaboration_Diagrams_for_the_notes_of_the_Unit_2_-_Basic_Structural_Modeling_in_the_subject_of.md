### Collaboration Diagrams

- Collaboration diagrams are used to show the **relationship** between the **objects** in a system.
- Collaboration diagrams are also known as **communication diagrams** in UML 2.x.
- Collaboration diagrams are useful for modeling **collaborations**, **mechanisms** or the **structural organization** within a system design.
- Collaboration diagrams can represent the same information as sequence diagrams, but differently. Instead of showing the **flow of messages**, they depict the **architecture of the objects** and their **links**.
- The four major components of a collaboration diagram are:
  - **Objects**: Objects are shown as rectangles with naming labels inside. The naming label follows the convention of object name : class name.
  - **Actors**: Actors are instances that invoke the interaction in the diagram. Each actor has a name and a role, with one of them being the primary actor who initiates the use case.
  - **Links**: Links are lines that connect objects and actors. They represent the communication paths or associations between them.
  - **Messages**: Messages are labels along the links that indicate the information or action flow between the objects and actors. They have a sequence number and a name, and can be synchronous or asynchronous.
- A collaboration diagram can be created by following these steps:
  - Open a UML diagram template.
  - Drag and drop the objects and actors from the library to the canvas.
  - Connect the objects and actors with links from the connector tool.
  - Label the links with messages from the text tool.
  - Adjust the layout and appearance of the diagram as needed.
- A collaboration diagram can be used to:
  - Show the **static structure** of a system and the **dynamic behavior** of a use case.
  - Show the **interaction** and **responsibility** of the objects and actors involved in a use case.
  - Show the **alternative paths** or **scenarios** of a use case.
  - Show the **logical view** or the **implementation view** of a system.

Here is an example of a collaboration diagram for a library system:

![collaboration diagram example](https://www.edrawmax.com/images/article/collaboration-diagram-uml/collaboration-diagram-uml-1.png)