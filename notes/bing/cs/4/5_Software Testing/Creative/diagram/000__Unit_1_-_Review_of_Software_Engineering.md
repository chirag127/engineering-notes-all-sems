## Unit 1 - Review of Software Engineering

Software engineering is the application of engineering principles and practices to the development and maintenance of software systems. Software engineering involves various activities, such as:

- Requirements analysis: The process of eliciting, analyzing, and documenting the needs and expectations of the stakeholders for a software system.
- Design: The process of defining the structure, behavior, and interfaces of the software system and its components.
- Implementation: The process of writing, testing, and debugging the source code of the software system and its components.
- Testing: The process of verifying and validating that the software system and its components meet the requirements and specifications.
- Deployment: The process of installing, configuring, and running the software system in the target environment.
- Maintenance: The process of modifying and updating the software system and its components to correct defects, improve performance, or adapt to changing requirements.

One of the common ways to represent and communicate the software engineering activities and artifacts is by using diagrams. Diagrams are graphical models that show the structure, behavior, or interactions of the software system and its components. There are different types of diagrams, such as:

- Class diagram: A type of static structure diagram that shows the classes, their attributes, operations, and the relationships among them.
- Sequence diagram: A type of interaction diagram that shows the sequence of messages exchanged between the objects or actors in a scenario.
- Use case diagram: A type of behavior diagram that shows the use cases, the actors, and the relationships among them.
- Activity diagram: A type of behavior diagram that shows the flow of actions or activities in a process or a system.
- Component diagram: A type of static structure diagram that shows the components, their interfaces, and the dependencies among them.

The following diagram illustrates the basic architecture of a software system using a component diagram:

```
+-----------------+        +-----------------+        +-----------------+
| User Interface  |        | Business Logic  |        | Data Access     |
| Component       |        | Component       |        | Component       |
+-----------------+        +-----------------+        +-----------------+
| +display()      |        | +process()      |        | +query()        |
| +input()        |        | +validate()     |        | +update()       |
+-----------------+        +-----------------+        +-----------------+
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        +------------------------>+------------------------>+
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        +<------------------------+<------------------------+
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
+-----------------+        +-----------------+        +-----------------+
| User Interface  |        | Business Logic  |        | Data Access     |
| Component       |        | Component       |        | Component       |
+-----------------+        +-----------------+        +-----------------+
```

The diagram shows that the software system consists of three components: User Interface, Business Logic, and Data Access. The User Interface component is responsible for displaying the information and receiving the input from the user. The Business Logic component is responsible for processing the input, validating the data, and applying the business rules. The Data Access component is responsible for querying and updating the data from the database or other sources. The diagram also shows the interfaces and the dependencies among the components. The User Interface component depends on the Business Logic component, and the Business Logic component depends on the Data Access component. The components communicate with each other by sending and receiving messages through their interfaces. The diagram uses the following notation:

- A rectangle represents a component.
- A