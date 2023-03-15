A use case diagram is a graphical representation of the interactions between a system and its external actors. It shows the functionality of the system from the user's point of view and the relationships among the use cases. A use case diagram is one of the artifacts of the Unified Modeling Language (UML) and is used for software engineering.

The main components of a use case diagram are:

- Actors: The external entities that interact with the system. They can be human users, other systems, or devices. Actors are represented by stick figures or icons.
- Use cases: The actions or services that the system provides to the actors. They are represented by ovals with the use case name inside.
- Associations: The lines that connect actors and use cases. They indicate that an actor participates in a use case.
- Include relationships: The dashed arrows with the label "include" that connect use cases. They indicate that a use case is a mandatory part of another use case.
- Extend relationships: The dashed arrows with the label "extend" that connect use cases. They indicate that a use case is an optional or conditional part of another use case.
- Generalization relationships: The solid arrows with an empty triangle head that connect actors or use cases. They indicate that an actor or a use case inherits the characteristics of another actor or use case.

An example of a use case diagram for the notes of the Unit 1 - Introduction of Software Engineering Lab in the subject of Software Engineering Lab is shown below:

![use case diagram example](https://i.imgur.com/9X9Zf6v.png)

The diagram shows the following actors and use cases:

- Student: The actor who wants to learn about software engineering concepts and practices. The student can perform the following use cases:
  - View notes: The student can view the notes of the unit 1 on the online platform or download them as PDF files.
  - Take quiz: The student can take a quiz on the unit 1 topics and get feedback on their performance.
  - Submit assignment: The student can submit an assignment on the unit 1 topics and get feedback on their submission.
- Instructor: The actor who teaches the software engineering course and provides the notes, quizzes, and assignments. The instructor can perform the following use cases:
  - Upload notes: The instructor can upload the notes of the unit 1 on the online platform or provide links to external resources.
  - Create quiz: The instructor can create a quiz on the unit 1 topics and set the parameters such as time limit, number of questions, and scoring scheme.
  - Evaluate assignment: The instructor can evaluate the assignment submissions of the students and provide feedback and grades.
- Administrator: The actor who manages the online platform and ensures its functionality and security. The administrator can perform the following use cases:
  - Manage users: The administrator can create, update, delete, and assign roles to the users of the online platform.
  - Manage content: The administrator can create, update, delete, and organize the content of the online platform such as notes, quizzes, and assignments.
  - Monitor system: The administrator can monitor the system performance, usage, and security and take actions to resolve any issues.

The diagram also shows the following relationships among the use cases:

- The use case "View notes" includes the use case "Download notes" as the student can download the notes as PDF files after viewing them on the online platform.
- The use case "Take quiz" extends the use case "View notes" as the student can optionally take a quiz after viewing the notes on the online platform.
- The use case "Submit assignment" extends the use case "View notes" as the student can optionally submit an assignment after viewing the notes on the online platform.
- The use case "Create quiz" includes the use case "Set quiz parameters" as the instructor has to set the parameters such as time limit, number of questions, and scoring scheme when creating a quiz.
- The use case "Evaluate assignment" includes the use case "Provide feedback" as the instructor has to provide feedback and grades to the students when evaluating their assignment submissions.
- The use case "Manage users" generalizes the use cases "Create user", "Update user", "Delete user", and "Assign role" as the administrator can perform any of these actions when managing the users of the online platform.
- The use case "Manage content" generalizes the use cases "Create content", "Update content", "Delete content", and "Organize content" as the administrator can perform any of these actions when managing the content of the online platform.