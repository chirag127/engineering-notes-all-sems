### Use cases for the notes of the Unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design

- Basic structural modeling is the process of identifying and describing the static structure of a system using classes, relationships, interfaces, and collaborations.
- Use cases are a way of capturing the functional requirements of a system from the perspective of the external actors (users or other systems) that interact with the system.
- Use cases can be used for the notes of the Unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design for the following purposes:

  - To elicit and document the requirements of the system in a user-centric way.
  - To provide an overview of the system functionality and scope.
  - To communicate and validate the requirements with the stakeholders and users.
  - To identify the main classes, interfaces, and collaborations that are involved in the system behavior.
  - To guide the design and implementation of the system using the UML diagrams.
  - To support the testing and verification of the system using scenarios and test cases.

- Use cases are represented diagrammatically using the UML notation. A use case diagram consists of the following elements:

  - Actors: The external entities that interact with the system. They can be human users or other systems. They are depicted as stick figures with names.
  - Use cases: The discrete tasks that the system performs in response to the actors' requests. They are depicted as ovals with names.
  - Associations: The lines that connect the actors and the use cases. They indicate that an actor participates in a use case.
  - Generalizations: The relationships that indicate that one actor or use case inherits the characteristics of another actor or use case. They are depicted as dashed lines with a triangle at the end.
  - Include: The relationship that indicates that one use case includes the behavior of another use case. It is used to avoid duplication and to modularize the use cases. It is depicted as a dashed line with the keyword <<include>>.
  - Extend: The relationship that indicates that one use case extends the behavior of another use case under certain conditions. It is used to capture optional or exceptional behavior. It is depicted as a dashed line with the keyword <<extend>>.

- An example of a use case diagram for a library system is shown below:

![use case diagram](https://www.tutorialspoint.com/object_oriented_analysis_design/images/use_case_diagram.jpg)

- The diagram shows that there are three actors: Librarian, Member, and Supplier. There are eight use cases: Add Book, Search Book, Issue Book, Return Book, Reserve Book, Generate Report, Order Book, and Receive Book. The associations show which actor can initiate which use case. The generalizations show that Member is a subtype of Librarian, and that Generate Report is a general use case that has two specific use cases: Generate Fine Report and Generate Inventory Report. The include relationships show that Search Book is included in Issue Book, Return Book, and Reserve Book. The extend relationships show that Issue Book is extended by Fine Calculation and Return Book is extended by Damage Calculation.