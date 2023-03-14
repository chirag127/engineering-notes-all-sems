## Unit 1 - Review of Software Engineering

Software engineering is a set of engineering methods used in the software development of system applications. It defines principles for specification, design, development, testing, evaluation, and maintenance.

One of the common diagrams used in software engineering is the class diagram, which is a type of static structure diagram that describes the structure of a system by showing the system's classes, their attributes, operations (or methods), and the relationships among objects.

The following diagram illustrates the basic structure of a class diagram using ASCII characters:

```
+---------------------+        +---------------------+
|       Student       |        |       Course        |
+---------------------+        +---------------------+
| - name: String      |        | - title: String     |
| - id: Integer       |        | - code: String      |
| - email: String     |        | - credits: Integer  |
+---------------------+        +---------------------+
| + enroll(c: Course) |<>------| + addStudent(s:Student) |
| + drop(c: Course)   |        | + removeStudent(s:Student) |
| + getEmail()        |        | + getTitle()         |
+---------------------+        +---------------------+
```

The diagram shows two classes: Student and Course, with their attributes and operations. The attributes are prefixed with a visibility symbol (- for private, + for public) and followed by a type. The operations are also prefixed with a visibility symbol and followed by a parameter list.

The diagram also shows a relationship between the classes, indicated by a diamond-headed line. This is an example of a composition relationship, which means that a Course object has one or more Student objects as its parts, and the lifetime of the Student objects depends on the Course object. The diamond is placed on the side of the container class (Course), and the line is labeled with a multiplicity value (0..*) to indicate how many Student objects can be associated with a Course object.

There are other types of relationships that can be shown in a class diagram, such as inheritance, association, aggregation, and dependency. Each relationship has a different notation and meaning, and they can be used to model different aspects of a system's structure and behavior. For more information on class diagrams and other types of software engineering diagrams, you can refer to the UML specification or other online resources.