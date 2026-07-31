### Sequence Diagram for Software Engineering Lab

A sequence diagram is a type of interaction diagram that shows the sequence of messages exchanged between objects in a system to perform a specific functionality . It is used to depict the interactions between several objects in a system and the order in which they occur . A sequence diagram can help software developers and business professionals to understand the requirements of a new system or to document an existing process .

The basic components of a sequence diagram are:

- **Objects**: The entities that participate in the interaction. They are represented by rectangles with the object name and an optional classifier (such as a class name or a role name) underlined. Objects can be created, destroyed, or have multiple instances in a sequence diagram.
- **Lifelines**: The vertical dashed lines that show the existence and the state of an object over time. They are attached to the objects and extend downwards along the timeline. Lifelines can have activation boxes that indicate when an object is active or executing a method.
- **Messages**: The horizontal arrows that show the communication between objects. They are labeled with the name of the operation or the event that triggers the message. Messages can be synchronous (solid arrowhead), asynchronous (open arrowhead), reply (dashed arrowhead), or create/destroy (solid arrowhead with a cross at the tail). Messages can also have sequence numbers, conditions, or iterations to indicate the order, the guard, or the repetition of the message.
- **Fragments**: The rectangular frames that enclose a part of the interaction to show some additional information or constraints. They are labeled with an operator (such as alt, opt, loop, par, etc.) and a guard condition (if applicable). Fragments can be nested or combined to represent complex scenarios.

Here are two examples of sequence diagrams for the notes of the Unit 1 - Introduction of Software Engineering Lab in the subject of Software Engineering Lab:

- **Example 1**: A sequence diagram for the scenario of a student registering for a course in an online learning system.

```sequence
Student->+Online Learning System: login(username, password)
Online Learning System->-Student: display dashboard
Student->+Online Learning System: select course
Online Learning System->-Student: display course details
alt course is available
    Student->+Online Learning System: register for course
    Online Learning System->+Payment Gateway: request payment
    Payment Gateway->-Online Learning System: confirm payment
    Online Learning System->-Student: confirm registration
else course is full
    Online Learning System->-Student: display error message
end
```

- **Example 2**: A sequence diagram for the scenario of a teacher grading an assignment submitted by a student in an online learning system.

```sequence
Teacher->+Online Learning System: login(username, password)
Online Learning System->-Teacher: display dashboard
Teacher->+Online Learning System: select assignment
Online Learning System->-Teacher: display assignment details
loop for each submission
    Teacher->+Online Learning System: download submission
    Online Learning System->-Teacher: send submission file
    Teacher->+Online Learning System: upload feedback
    Online Learning System->-Teacher: store feedback
    Teacher->+Online Learning System: enter grade
    Online Learning System->-Teacher: store grade
end
```

: Sequence diagram - Wikipedia
: UML Sequence Diagram | Symbol and Components of Sequence Diagram - EDUCBA
: Creating UML Sequence Diagrams | Gliffy by Perforce
: Sequence Diagram Tutorial – Complete Guide with Examples
: What is Sequence Diagram? - Visual Paradigm
: UML Sequence Diagram Tutorial | Lucidchart