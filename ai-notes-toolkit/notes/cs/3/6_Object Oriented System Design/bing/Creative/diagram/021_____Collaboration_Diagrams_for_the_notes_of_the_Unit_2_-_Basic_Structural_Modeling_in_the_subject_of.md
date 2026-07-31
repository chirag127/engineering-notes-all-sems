# Collaboration Diagrams

- Collaboration diagrams are used to show the **relationship** between the **objects** in a system.
- Collaboration diagrams are also known as **communication diagrams** in UML 2.x.
- Collaboration diagrams are similar to **sequence diagrams**, but they focus more on the **structure** of the objects rather than the **order** of the messages.
- Collaboration diagrams can be used to model **collaborations**, **mechanisms** or the **structural organization** within a system design.
- Collaboration diagrams can also show the **conditional** and **iterative** behavior of the objects.

## Components of Collaboration Diagrams

- The four major components of a collaboration diagram are:
  - **Objects**: Objects are shown as rectangles with naming labels inside. The naming label follows the convention of object name : class name. Objects can also have **attributes** and **operations** shown in separate compartments within the rectangle.
  - **Actors**: Actors are instances that invoke the interaction in the diagram. Each actor has a name and a role, with one of them being the **primary actor** who initiates the use case. Actors are shown as **stick figures** or **rectangles** with the actor stereotype.
  - **Links**: Links are solid lines that connect objects and actors. They represent the **association** or **communication** between them. Links can have **multiplicity**, **roles** and **constraints** shown as labels on or near the line.
  - **Messages**: Messages are the information or data that is exchanged between the objects or actors. They are shown as **arrows** along the links, with the arrowhead indicating the direction of the message. Messages can have **sequence numbers**, **names**, **arguments** and **return values** shown as labels above or below the arrow.

## How to Draw a Collaboration Diagram

- The following steps can be used to draw a collaboration diagram:
  - Step 1: Open a UML Diagram template. Click on new, select Software and then pick UML Model Diagram.
  - Step 2: Identify the objects and actors involved in the use case or scenario. Drag and drop the appropriate shapes from the library onto the canvas. Name and label them accordingly.
  - Step 3: Identify the links and messages between the objects and actors. Draw the links as solid lines and the messages as arrows. Add the labels for the sequence numbers, names, arguments and return values of the messages.
  - Step 4: Add any conditional or iterative behavior to the diagram. Use **alt**, **opt**, **loop**, **break** or **par** frames to enclose the messages that are affected by the conditions or iterations. Add the guard conditions or loop expressions as labels on the frames.
  - Step 5: Review and refine the diagram. Check for the accuracy, completeness and clarity of the diagram. Adjust the layout, size and color of the shapes and lines as needed.

## Example of a Collaboration Diagram

- The following diagram shows an example of a collaboration diagram for a hotel booking system. It shows how the objects and actors interact to perform the use case of booking a room.

![collaboration diagram example](https://www.edrawmax.com/images/article/collaboration-diagram-example.png)

- The diagram can be explained as follows:
  - The primary actor is the **Customer** who initiates the use case by sending a **bookRoom** message to the **Hotel** object.
  - The **Hotel** object then sends a **checkAvailability** message to the **Room** object, which returns a **boolean** value indicating whether the room is available or not.
  - If the room is available, the **Hotel** object sends a **createReservation** message to the **Reservation** object, which creates a new reservation and returns a **confirmation number** to the **Hotel** object.
  - The **Hotel** object then sends a **confirmBooking** message to the **Customer** object, which completes the use case.
  - If the room is not available, the **Hotel** object sends a **rejectBooking** message to the **Customer** object, which ends the use case.