### Draw the sequence diagram for any two scenarios for the notes of the Unit 1 - Introduction of Software Engineering Lab in the subject of Software Engineering Lab

- A sequence diagram is a type of interaction diagram that shows the order and timing of messages exchanged between objects in a system  .
- A sequence diagram consists of the following components   :
  - Lifelines: vertical dashed lines that represent the objects or actors involved in the scenario. They are labeled with the name and type of the object or actor.
  - Activation boxes: thin rectangles that show the period of time when an object or actor is active or executing a method.
  - Messages: horizontal arrows that show the communication or interaction between the objects or actors. They are labeled with the name and parameters of the method or event being invoked. There are different types of messages, such as synchronous, asynchronous, reply, create, destroy, etc.
  - Fragments: boxes that enclose a part of the interaction to show some additional information or constraints, such as loops, alternatives, options, etc.
  - Frame: a rectangle that surrounds the entire diagram and contains the name of the diagram and the parameters of the scenario.

- Here are two examples of sequence diagrams for the notes of the Unit 1 - Introduction of Software Engineering Lab:

  - Example 1: A student logs in to the online learning platform and views the notes of the unit.

  ```mermaid
  sequenceDiagram
  participant S as Student
  participant P as Platform
  participant N as Notes
  S->>P: enter username and password
  P->>S: validate credentials
  alt credentials valid
    P->>S: display dashboard
    S->>P: select unit 1
    P->>N: request notes
    N->>P: send notes
    P->>S: display notes
  else credentials invalid
    P->>S: display error message
  end
  ```

  - Example 2: A teacher uploads the notes of the unit to the online learning platform and assigns them to a course.

  ```mermaid
  sequenceDiagram
  participant T as Teacher
  participant P as Platform
  participant N as Notes
  participant C as Course
  T->>P: enter username and password
  P->>T: validate credentials
  alt credentials valid
    P->>T: display dashboard
    T->>P: select upload notes
    P->>T: display upload form
    T->>P: fill in details and attach file
    P->>N: create notes
    N->>P: confirm creation
    P->>T: display confirmation message
    T->>P: select assign notes
    P->>T: display courses list
    T->>P: select course
    P->>C: request course
    C->>P: send course
    P->>T: display course details
    T->>P: select notes
    P->>N: request notes
    N->>P: send notes
    P->>T: display notes details
    T->>P: confirm assignment
    P->>C: update course
    C->>P: confirm update
    P->>T: display confirmation message
  else credentials invalid
    P->>T: display error message
  end
  ```