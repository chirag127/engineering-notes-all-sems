### Class Testing for the notes of the Unit 6 - Object Oriented Testing in the subject of Software Testing

Class testing is a type of testing that focuses on the verification of the classes in an object-oriented system. It involves testing the attributes, operations, and relationships of the classes, as well as the interactions between them. Class testing can be done at different levels of granularity, such as unit testing, integration testing, and system testing.

A class diagram is a useful tool for class testing, as it shows the static structure of the classes and their relationships in a system. A class diagram consists of the following elements:

- Classes: A class is a blueprint for creating objects. It has a name, attributes, and operations. A class is represented by a rectangle with three compartments: the top compartment contains the class name, the middle compartment contains the class attributes, and the bottom compartment contains the class operations. For example, a class named Student can have attributes such as name, id, and major, and operations such as enroll, drop, and graduate.

- Relationships: A relationship is a connection between two or more classes that indicates how they are related. There are different types of relationships, such as association, aggregation, composition, inheritance, and realization. A relationship is represented by a line connecting the classes, with optional symbols and labels to indicate the type, direction, and multiplicity of the relationship. For example, an association relationship between Student and Course can have a label enrolled in, and a multiplicity of 0..* at the Student end and 1 at the Course end, meaning that a student can enroll in zero or more courses, and a course must have one student enrolled in it.

- Operations: An operation is a function or a method that defines the behavior of a class. It has a name, parameters, and a return type. An operation is represented by a line in the bottom compartment of the class, with the format name(parameter list): return type. For example, an operation named enroll(course: Course): boolean can take a course as a parameter and return a boolean value indicating whether the enrollment was successful or not.

The following diagram illustrates the basic architecture of a class testing system using ASCII art:

```
+----------------+       +----------------+       +----------------+
|   Test Case    |       |   Test Suite   |       |  Test Runner   |
+----------------+       +----------------+       +----------------+
| - name: String |       | - name: String |       | - name: String |
| - input: Any   |       | - cases: List  |       | - suite: Test  |
| - output: Any  |       |                |       | - result: Test |
+----------------+       +----------------+       +----------------+
| + run(): Any   |       | + add(case:    |       | + run(): Test  |
|                |       |   Test): void  |       |                |
|                |       | + run(): List  |       |                |
+----------------+       +----------------+       +----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       +-----------------------+-----------------------+
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |