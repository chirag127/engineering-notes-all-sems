# Collaboration Diagrams

- Collaboration diagrams are used to show the **relationship** between the **objects** in a system.
- Collaboration diagrams are also known as **communication diagrams** in UML 2.x.
- Collaboration diagrams can be used to portray the **dynamic behavior** of a particular use case and define the **role** of each object.
- Collaboration diagrams are developed by first determining the **design elements** required to incorporate the **functionality** of interface features. The **interactions** among these elements are then used to build a model.
- Collaboration diagrams are similar to **sequence diagrams**, but they focus more on the **structure** of the object rather than the **sequence** of messages.
- Collaboration diagrams consist of the following elements :
  - **Objects**: The instances of classes that participate in the interaction. They are represented by rectangles with the object name and class name separated by a colon.
  - **Links**: The connections between objects that show their communication. They are represented by solid lines with optional arrows to indicate the direction of messages.
  - **Messages**: The information or data that is exchanged between objects. They are represented by labels along the links, with sequence numbers to indicate the order of messages.
  - **Roles**: The responsibilities or functions that an object performs in the interaction. They are represented by the name of the object or the name of the class in parentheses.
  - **Frames**: The boundaries that enclose a part of the interaction. They are represented by rectangles with the name of the interaction in the upper left corner.

- An example of a collaboration diagram for a bank ATM system is shown below:

![collaboration diagram example](https://www.edrawmax.com/images/article/collaboration-diagram-uml-2.png)

- In this diagram, the objects are **Customer**, **ATM**, **Account** and **Bank**. The links show how they communicate with each other. The messages show the actions that are performed by the objects, such as **insert card**, **enter PIN**, **withdraw cash**, etc. The roles show the functions that the objects perform, such as **(actor)** for Customer, **(boundary)** for ATM, **(entity)** for Account and **(control)** for Bank. The frame shows the name of the interaction, which is **Withdraw Cash**.