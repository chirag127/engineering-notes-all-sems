## Unit 1 - Introduction to Software Engineering

Software engineering is the application of engineering principles and practices to the development and maintenance of software systems. Software engineering involves various activities, such as:

- Requirements analysis: defining the problem and the needs of the users and stakeholders
- Design: creating a solution that meets the requirements and follows the standards and best practices of the domain
- Implementation: coding the solution using programming languages and tools
- Testing: verifying that the solution works as expected and meets the quality criteria
- Deployment: delivering the solution to the users and ensuring its proper operation
- Maintenance: fixing bugs, adding features, and updating the solution to meet changing needs and environments

Software engineering also involves various roles, such as:

- Software engineer: a general term for someone who applies engineering principles and practices to software development
- Software architect: someone who designs the overall structure and behavior of a software system
- Software developer: someone who writes code to implement the software system
- Software tester: someone who checks the quality and functionality of the software system
- Software analyst: someone who analyzes the requirements and specifications of the software system
- Software project manager: someone who plans, organizes, and monitors the software development process

Software engineering can be represented using various diagrams, such as:

- Class diagram: a type of static structure diagram that shows the classes, attributes, operations, and relationships of a software system
- Sequence diagram: a type of interaction diagram that shows the sequence of messages exchanged between objects in a software system
- Use case diagram: a type of behavior diagram that shows the use cases, actors, and relationships of a software system
- Activity diagram: a type of behavior diagram that shows the flow of actions and decisions in a software system
- Component diagram: a type of structure diagram that shows the components, interfaces, and dependencies of a software system
- Deployment diagram: a type of structure diagram that shows the nodes, artifacts, and configurations of a software system

Here is an example of a class diagram for a software system that manages a library:

```text
+---------------------+          +---------------------+
|       Library       |          |       Book          |
+---------------------+          +---------------------+
| - books: Book[]     |<>--------| - title: String     |
| - capacity: int     |          | - author: String    |
+---------------------+          | - isbn: String      |
| + addBook(b: Book)  |          | - available: boolean|
| + removeBook(b: Book)|         +---------------------+
| + findBook(t: String)|         | + borrow()          |
| + listBooks()       |          | + return()          |
+---------------------+          +---------------------+
```

Here is an example of a sequence diagram for a use case of borrowing a book from the library:

```text
+-------+       +--------+       +-------+       +------+
| Actor |       | System |       |Library|       | Book |
+-------+       +--------+       +-------+       +------+
    |               |               |               |
    |----Borrow---->|               |               |
    |               |----findBook-->|               |
    |               |               |----borrow---->|
    |               |<---returnBook-|<---return-----|
    |<---Book-------|               |               |
    |               |               |               |
+-------+       +--------+       +-------+       +------+
```

Here is an example of a use case diagram for the library software system:

```text
+---------------------+
|     Library System  |
+---------------------+
          |
          |
+---------|---------+
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
+---------|---------+
          |
          |
+---------|---------+
|    User            |
+---------|---------+
    |     |     |
    |     |     |
    |     |     |
    |     |     |
    |     |     |
    |     |     |
    |     |     |
    |     |     |
+---|-----|-----|---+
|   |     |     |   |
|   |     |     |   |
|   |     |     |   |
|   |     |     |   |
|   |     |     |   |
|   |     |     |   |
|   |     |     |   |
|   |     |     |   |
+---|