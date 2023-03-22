### Use Case Diagram and Actor Roles

In software engineering, a use case diagram is a visual representation of the interactions between actors and a system. It is used to model the functional requirements of a system and to identify the actors that interact with it. In the Software Engineering Lab, use case diagrams are an essential tool in the development process. Here are the actor roles and use case diagram for notes of Unit 1 - Introduction:

#### Actors

1. Student - A user who will be accessing the system to view and download notes.
2. Professor - A user who will be accessing the system to upload and manage notes.
3. Admin - A user who will be responsible for managing the system and user accounts.

#### Use Case Diagram

The use case diagram for notes of Unit 1 - Introduction is as follows:

```
                                   +-----------------+
                                   |    Administrator|
                                   +-----------------+
                                             |
                                             |
                                             |
                                             |
                   +-------------------------+--------------------------+
                   |                                                    |
                   |                                                    |
           +----------------+                              +----------------+
           |    Student     |                              |    Professor   |
           +----------------+                              +----------------+
                   |                                                    |
                   |                                                    |
                   |                                                    |
                   |                                                    |
                   |                                                    |
                   |                                                    |
                   |                                                    |
            +----------------+                                  +----------------+
            |  View Notes    |                                  |   Upload Notes |
            +----------------+                                  +----------------+
```

#### Actor Roles

1. Student - This actor will be able to view and download notes from the system. The student will be able to interact with the system through the "View Notes" use case.
2. Professor - This actor will be able to upload and manage notes. The professor will be able to interact with the system through the "Upload Notes" use case.
3. Admin - This actor will be responsible for managing the system and user accounts. The admin will be able to interact with the system through various use cases, such as managing user accounts and updating the system.