### Sequence Diagrams for Software Engineering Lab

A sequence diagram is a type of interaction diagram that shows the sequence of messages exchanged between objects in a system to perform a specific functionality . It is used to illustrate the interactions between objects in a system in the order that they occur . Sequence diagrams are time-focused and they show the order of the interaction visually by using the vertical axis of the diagram to represent time .

A sequence diagram consists of the following components:

- **Lifelines**: These are vertical dashed lines that represent the objects involved in the interaction. They are labeled with the name of the object or its role. The top of the lifeline is the creation point of the object and the bottom is the destruction point.
- **Activation boxes**: These are thin rectangles that show the period of time that an object is active or executing a method. They are placed on the lifelines and may be nested to indicate method calls.
- **Messages**: These are horizontal arrows that show the communication between objects. They are labeled with the name of the message or the method being invoked. There are different types of messages, such as synchronous, asynchronous, reply, create, and destroy messages.
- **Fragments**: These are rectangular frames that enclose a part of the interaction to show some additional information, such as conditions, loops, alternatives, parallelism, etc. They are labeled with an operator and a guard expression.
- **Combined fragments**: These are fragments that contain other fragments to show complex interactions, such as nested conditions, loops, etc.
- **Interaction use**: This is a reference to another sequence diagram that shows a common interaction that is reused in the current diagram. It is represented by a rectangular frame with a dashed border and labeled with ref and the name of the referenced diagram.

Here are two examples of sequence diagrams for the notes of the Unit 1 - Introduction of Software Engineering Lab in the subject of Software Engineering Lab:

- **Scenario 1: Student submits an assignment to the instructor**

```sequence
Student->Instructor: request assignment
Instructor->Student: send assignment details
Student->Student: work on assignment
Student->Instructor: submit assignment
Instructor->Student: acknowledge receipt
Instructor->Instructor: grade assignment
Instructor->Student: send feedback and grade
```

- **Scenario 2: Instructor updates the course syllabus and notifies the students**

```sequence
Instructor->Instructor: edit syllabus
Instructor->Course Website: upload syllabus
alt syllabus uploaded successfully
    Course Website->Instructor: confirm upload
    loop for each student
        Course Website->Student: send notification
    end
else syllabus upload failed
    Course Website->Instructor: report error
end
```