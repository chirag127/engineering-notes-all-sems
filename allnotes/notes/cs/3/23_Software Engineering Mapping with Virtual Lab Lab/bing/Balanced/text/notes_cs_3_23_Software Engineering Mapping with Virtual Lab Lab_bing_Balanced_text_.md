

## Identifying the Requirements from Problem Statements for the notes of the Software Engineering Mapping with Virtual Lab Lab in the subject of Software Engineering

- Requirements are the specifications of what the software system should do and how it should perform.
- Problem statements are the descriptions of the problems or needs that the software system should address or solve.
- Identifying the requirements from problem statements is the process of analyzing the problem statements and extracting the relevant and necessary requirements for the software system.
- Identifying the requirements from problem statements involves the following steps:

  - Reading and understanding the problem statements carefully and completely.
  - Identifying the stakeholders, users, and goals of the software system.
  - Identifying the functional requirements, which are the features or services that the software system should provide to the users or other systems.
  - Identifying the non-functional requirements, which are the constraints or quality attributes that the software system should satisfy or adhere to, such as performance, reliability, security, usability, etc.
  - Identifying the assumptions, dependencies, and risks that may affect the software system or its development.
  - Prioritizing and validating the requirements with the stakeholders and users, and resolving any conflicts or ambiguities.
  - Documenting and managing the requirements using appropriate tools and techniques, such as use cases, user stories, scenarios, diagrams, etc.

- Identifying the requirements from problem statements is an important and challenging task in software engineering, as it affects the quality, feasibility, and success of the software system and its development.
- Identifying the requirements from problem statements requires good communication, analytical, and critical thinking skills, as well as domain knowledge and experience.



## Estimation of Project Metrics for the notes of the Software Engineering Mapping with Virtual Lab Lab in the subject of Software Engineering

- Project metrics are quantitative measures that describe some aspect of a software project, such as size, effort, duration, quality, or productivity.
- Estimation of project metrics is the process of predicting the values of these measures based on available information and assumptions.
- Estimation of project metrics is important for planning, monitoring, and controlling software projects, as well as for evaluating their outcomes and improving their processes.
- Estimation of project metrics can be done at different levels of granularity, such as project, phase, activity, task, or resource.
- Estimation of project metrics can be done using different methods, such as expert judgment, analogy, parametric models, or machine learning.
- Estimation of project metrics can be influenced by various factors, such as project characteristics, environmental factors, historical data, or human factors.
- Estimation of project metrics can be improved by applying best practices, such as defining clear and measurable objectives, collecting and analyzing relevant data, using appropriate methods and tools, validating and updating estimates, and communicating and documenting estimates.



## Modeling UML Use Case Diagrams and Capturing Use Case Scenarios

- UML stands for Unified Modeling Language, which is a standard way of visualizing and documenting the design of a software system.
- Use case diagrams are one of the types of UML diagrams that show the behavior and requirements of a system from the perspective of the users (or actors).
- Use case diagrams consist of the following elements:
  - Actors: represent the roles or entities that interact with the system, such as users, customers, or other systems. Actors are depicted as stick figures or icons.
  - Use cases: represent the goals or functions that the actors want to achieve by using the system, such as login, register, or purchase. Use cases are depicted as ovals with names inside.
  - Relationships: represent the connections or associations between actors and use cases, or between use cases themselves. Relationships are depicted as lines with different symbols to indicate the type of relationship, such as association, include, extend, or generalize.
- Use case diagrams are useful for:
  - Representing the goals of system-user interactions
  - Defining and organizing functional requirements in a system
  - Specifying the context and requirements of a system
  - Modeling the basic flow of events in a use case
- Use case scenarios are the textual descriptions of the steps and interactions that occur in a use case. Use case scenarios can be written in different formats, such as:
  - Brief: a simple summary of the main success scenario
  - Casual: a more detailed description of the main success scenario and some alternative scenarios
  - Fully dressed: a comprehensive and structured description of the main success scenario and all possible alternative scenarios, including preconditions, postconditions, triggers, exceptions, and extensions
- Use case scenarios are useful for:
  - Elaborating the details and variations of a use case
  - Communicating the requirements and expectations of a use case to the stakeholders and developers
  - Testing and verifying the functionality and quality of a use case
- An example of a use case diagram and a use case scenario for an online shopping system is shown below:

Use case diagram for online shopping system

Use case: Purchase items
Brief scenario: The customer browses the catalog, adds items to the shopping cart, enters the shipping and payment information, and confirms the order.
Casual scenario: The customer browses the catalog and selects some items. The system shows the details and price of each item. The customer adds the items to the shopping cart. The system updates the total amount of the cart. The customer proceeds to checkout. The system asks the customer to enter the shipping and payment information. The customer enters the information and confirms the order. The system validates the information and processes the payment. The system sends a confirmation email to the customer and updates the inventory.
Fully dressed scenario:
- Name: Purchase items
- Actor: Customer
- Preconditions: The customer has accessed the online shopping system and has a valid account.
- Postconditions: The customer has received a confirmation email and the order has been placed.
- Trigger: The customer clicks on the checkout button.
- Main success scenario:
  1. The system asks the customer to enter the shipping and payment information.
  2. The customer enters the information and confirms the order.
  3. The system validates the information and processes the payment.
  4. The system sends a confirmation email to the customer and updates the inventory.
  5. The use case ends successfully.
- Extensions:
  - 3a. The system detects an error in the information or the payment.
    - 3a1. The system displays an error message and asks the customer to correct the information or try another payment method.
    - 3a2. The customer corrects the information or tries another payment method.
    - 3a3. The use case resumes at step 3.
  - 3b. The system detects that some items are out of stock.
    - 3b1. The system displays a warning message and removes the out of stock items from the cart.
    - 3b2. The system recalculates the total amount of the cart.
    - 3b3. The use case resumes at step 2.



## E-R Modeling from the Problem Statements

- Entity-Relationship (ER) model is a high-level data model that represents the logical design of a database. 
- In ER model, real world objects or concepts are abstracted as entities, and different possible associations among them are modeled as relationships. 
- For example, student and school are two entities, and enrolled in is a relationship between them.
- From a given problem statement, we identify the possible entity sets, their attributes, and relationships among different entity sets. 
- Once we have these information, we represent them pictorially, called an ER diagram. 
- An ER diagram uses graphical notations to show the entities, attributes, relationships, and constraints. 
- Some of the common notations are:

  - Rectangles for entities
  - Ellipses for attributes
  - Diamonds for relationships
  - Lines for connections
  - Double ellipses for multivalued attributes
  - Dashed ellipses for derived attributes
  - Double lines for total participation
  - Double rectangles for weak entities
  - Double diamonds for identifying relationships

- ER modeling is important for designing databases, as it helps to:

  - Understand the requirements and scope of the problem domain. 
  - Communicate and validate the design with the stakeholders. 
  - Reduce redundancy and inconsistency in the data. 
  - Support data integrity and security. 
  - Facilitate database maintenance and evolution. 

- Enhanced Entity Relationship (EER) model is an extension of the ER model that supports more complex and realistic database designs. 
- EER model introduces concepts such as:

  - Subclasses and superclasses
  - Specialization and generalization
  - Inheritance and constraints
  - Aggregation and composition
  - Categories and union types

- EER model uses UML notation to represent these concepts.



## Identifying Domain Classes from the Problem Statements for the notes of the Software Engineering Mapping with Virtual Lab Lab in the subject of Software Engineering

- A domain class is a representation of a real-world entity or concept that is relevant to the problem domain of a software system.
- A domain class has attributes (properties or characteristics) and operations (behaviors or actions) that describe its state and behavior in the problem domain.
- Identifying domain classes from the problem statements is a process of analyzing the textual description of the problem domain and extracting the nouns and verbs that represent the entities and actions involved in the problem.
- The steps for identifying domain classes from the problem statements are:

  - Read the problem statement carefully and identify the nouns and verbs that are relevant to the problem domain.
  - Eliminate the nouns and verbs that are irrelevant, ambiguous, or redundant.
  - Group the remaining nouns and verbs into categories based on their similarity or relationship.
  - For each category, select a representative noun as the name of the domain class and list the attributes and operations that correspond to the nouns and verbs in the category.
  - Refine the domain classes by checking for completeness, consistency, and clarity.
  - Draw a domain model diagram that shows the domain classes and their associations.

- An example of identifying domain classes from the problem statement of a library management system is:

  - Problem statement: A library management system allows the librarian to manage the books and the borrowers. The librarian can add, delete, update, and search for books and borrowers. The librarian can also issue, return, and renew books. The system keeps track of the book details, borrower details, and transaction details.
  - Nouns and verbs: librarian, manage, books, borrowers, add, delete, update, search, issue, return, renew, system, track, book details, borrower details, transaction details.
  - Eliminated nouns and verbs: system, track, details.
  - Categories: 
    - Librarian: librarian, manage
    - Book: book, add, delete, update, search, issue, return, renew
    - Borrower: borrower, add, delete, update, search
    - Transaction: transaction, issue, return, renew
  - Domain classes:
    - Librarian: attributes: id, name, password; operations: manageBooks, manageBorrowers, manageTransactions
    - Book: attributes: id, title, author, publisher, status; operations: addBook, deleteBook, updateBook, searchBook, issueBook, returnBook, renewBook
    - Borrower: attributes: id, name, address, phone, email; operations: addBorrower, deleteBorrower, updateBorrower, searchBorrower
    - Transaction: attributes: id, bookId, borrowerId, issueDate, returnDate, dueDate, fine; operations: issueBook, returnBook, renewBook, calculateFine
  - Domain model diagram:

    ```mermaid
    classDiagram
      Librarian --|> Book
      Librarian --|> Borrower
      Librarian --|> Transaction
      Book "1" -- "0..*" Transaction : issued to
      Borrower "1" -- "0..*" Transaction : borrowed by
      class Librarian{
        -id : int
        -name : string
        -password : string
        +manageBooks()
        +manageBorrowers()
        +manageTransactions()
      }
      class Book{
        -id : int
        -title : string
        -author : string
        -publisher : string
        -status : string
        +addBook()
        +deleteBook()
        +updateBook()
        +searchBook()
        +issueBook()
        +returnBook()
        +renewBook()
      }
      class Borrower{
        -id : int
        -name : string
        -address : string
        -phone : string
        -email : string
        +addBorrower()
        +deleteBorrower()
        +updateBorrower()
        +searchBorrower()
      }
      class Transaction{
        -id : int
        -bookId : int
        -borrowerId : int
        -issueDate : date
        -returnDate : date
        -dueDate : date
        -fine : double
        +issueBook()
        +returnBook()
        +renewBook()
        +calculateFine()
      }
    ```



## Statechart and Activity Modeling for the notes of the Software Engineering Mapping with Virtual Lab Lab in the subject of Software Engineering

- A statechart diagram is a kind of diagram used in computer science and related fields to describe the behavior of a system or an object over time.
- A statechart diagram shows the possible states of an object and the transitions between them. A state is a condition or situation that an object can be in, and a transition is a change from one state to another triggered by an event or a condition.
- A statechart diagram can have nested states, parallel states, entry and exit actions, guards, events, and actions.
- An activity diagram is a special kind of statechart diagram that focuses on the flow of actions and activities within a system or a process.
- An activity diagram shows the sequence and concurrency of actions, the synchronization and branching of flows, the use of swimlanes to partition activities by actors or objects, and the input and output of data.
- An activity diagram can have initial and final nodes, action nodes, control nodes, object nodes, pins, partitions, and edges.
- Statechart diagrams and activity diagrams are two popular UML diagrams to visualize the dynamic behavior of an information system.
- Statechart diagrams and activity diagrams can be used to model the states and activities of classes, use cases, components, subsystems, or the whole system .
- Statechart diagrams and activity diagrams can be used for system analysis, design, simulation, testing, and documentation  .



## Modeling UML Class Diagrams and Sequence Diagrams

- UML stands for Unified Modeling Language, which is a standard notation for describing the structure and behavior of software systems.
- UML class diagrams and sequence diagrams are two types of diagrams that can be used to model software systems.
- Class diagrams show the static structure of a system, such as the classes, interfaces, attributes, operations, and relationships among them.
- Sequence diagrams show the dynamic behavior of a system, such as the sequence of messages exchanged between objects over time.
- Class diagrams and sequence diagrams work together to allow precise modeling of a system and to convey unambiguous code-mapping information to developers.
- To model a system using class diagrams and sequence diagrams, the following steps can be followed:

  - Identify the classes and interfaces that are relevant to the system and their attributes and operations.
  - Draw a class diagram that shows the classes and interfaces and their relationships, such as inheritance, association, aggregation, composition, and dependency.
  - Identify the use cases and scenarios that describe the functionality and interactions of the system.
  - Draw a sequence diagram for each scenario that shows the objects involved and the messages they exchange in chronological order.
  - Use the same names and types for the classes and objects in both diagrams to ensure consistency and traceability.
  - Use the class diagram and the sequence diagram to verify and validate the system requirements and design.

- An example of a class diagram and a sequence diagram for a school management system is shown below :

Class diagram for school management system

Sequence diagram for school management system

- Class diagram for school management system shows the classes and interfaces such as Student, Teacher, Course, Exam, etc. and their attributes and operations such as name, id, enroll, teach, etc. and their relationships such as inheritance, association, and aggregation.
- Sequence diagram for school management system shows the objects and messages involved in a scenario of a student taking an online exam, such as Student, Exam, Course, Teacher, etc. and their messages such as login, startExam, submitAnswer, gradeExam, etc. in chronological order.



## Modeling Data Flow Diagrams for the notes of the Software Engineering Mapping with Virtual Lab Lab in the subject of Software Engineering

- Data Flow Diagrams (DFDs) are graphical representations of the data processing and flow in a software system  .
- DFDs show the sources, destinations, storage, and transformation of data, as well as the events and functions that trigger data flow .
- DFDs can be used to model the functional aspects of a software system, such as the inputs, outputs, processes, and data stores involved in each function  .
- DFDs can also be used to analyze the existing system and identify the requirements and design of a new or improved system  .
- DFDs can be drawn at different levels of abstraction, from the context diagram that shows the entire system as a single process, to the detailed diagram that shows the internal structure and logic of each process  .
- DFDs use four basic symbols to represent the components of a system :
  - Process: A circle or a rounded rectangle that represents a function or a transformation of data.
  - Data store: A rectangle with two parallel lines on the side that represents a place where data is stored or retrieved.
  - Data flow: An arrow that represents the movement or direction of data between processes, data stores, or external entities.
  - External entity: A rectangle that represents a source or destination of data outside the system boundary.
- DFDs follow some basic rules and conventions to ensure clarity and consistency :
  - Each process should have a unique name and number that describes its function.
  - Each data flow should have a label that describes the data or information being transferred.
  - Each data store should have a name that identifies the data or information being stored.
  - Each external entity should have a name that identifies the source or destination of data.
  - Processes should not have direct data flows between them, but should use data stores or external entities as intermediaries.
  - Data flows should not cross each other, but should use junctions or forks to split or join data flows.
  - Data flows should not have loops or cycles, but should have a clear beginning and end point.
  - Data flows should not have multiple sources or destinations, but should have a single source and a single destination.
- DFDs can be verified and validated by checking the consistency, completeness, and correctness of the data flow and the processes :
  - Consistency: The data flow and the processes should match the system objectives and specifications, and should not have any contradictions or conflicts.
  - Completeness: The data flow and the processes should cover all the possible scenarios and cases, and should not have any gaps or missing information.
  - Correctness: The data flow and the processes should reflect the actual or desired behavior and logic of the system, and should not have any errors or mistakes.



## Estimation of Test Coverage Metrics and Structural Complexity

- Test coverage metrics are used to measure and monitor the testing activity of a software program. They help to assess the thoroughness, effectiveness and efficiency of testing techniques.
- Structural complexity is a measure of how complex a program is in terms of its control flow and logic. It can be estimated by using control flow graphs (CFGs), which are visual representations of the flow of control within a program .
- A CFG consists of nodes and edges, where nodes represent basic blocks and edges represent transitions between them. A basic block is a sequence of statements that has a single entry point and a single exit point.
- A CFG can help to identify the linearly independent paths in a program, which are paths that traverse at least one edge that is not traversed by any other path. The number of linearly independent paths is also known as the cyclomatic complexity of a program, which is a metric of structural complexity .
- Test coverage metrics can be derived from the CFG and the cyclomatic complexity of a program. Some examples of test coverage metrics are:
  - Statement coverage: the percentage of statements that are executed by the test cases.
  - Branch coverage: the percentage of branches (edges) that are executed by the test cases.
  - Path coverage: the percentage of paths that are executed by the test cases.
  - Condition coverage: the percentage of conditions (boolean expressions) that are evaluated to both true and false by the test cases .
- Test coverage metrics can help to identify the gaps and weaknesses in the testing process, and guide the selection and generation of test cases. They can also help to evaluate the quality and reliability of the software program.



## Designing Test Suites for the notes of the Software Engineering Mapping with Virtual Lab Lab in the subject of Software Engineering

- A test suite is a collection of test cases that are intended to test a software program for its specified behaviors and requirements .
- Test suites are created after the test plan, which defines the scope, objectives, strategy, and resources for testing.
- Test suites can be organized based on the test cycle, such as unit testing, integration testing, system testing, and acceptance testing, or based on the test scope, such as functional testing, performance testing, security testing, and usability testing.
- Test suites should include test parameters, such as the application name, version, environment, test data, expected results, and test execution status.
- Test suites should also include test scripts, which are the detailed steps to execute the test cases and verify the expected results.
- Test design is the process of creating test suites or test cases based on the software requirements and specifications.
- Test design techniques are the methods or approaches to generate test cases or test suites that can effectively cover the test objectives and criteria.
- Test design techniques can be classified into three categories: specification-based, structure-based, and experience-based.
- Specification-based techniques, also known as black-box techniques, derive test cases from the external view of the software, such as the functional requirements, user stories, use cases, or user interface.
- Structure-based techniques, also known as white-box techniques, derive test cases from the internal view of the software, such as the code, logic, or architecture.
- Experience-based techniques, also known as exploratory techniques, derive test cases from the tester's knowledge, intuition, or creativity.
- Some examples of specification-based techniques are equivalence partitioning, boundary value analysis, decision table testing, state transition testing, and use case testing.
- Some examples of structure-based techniques are statement coverage, branch coverage, path coverage, and mutation testing.
- Some examples of experience-based techniques are error guessing, checklist-based testing, and exploratory testing.
- The choice of test design techniques depends on the type, complexity, and quality of the software, as well as the availability of resources, time, and tools.
- The goal of test design is to create test suites that are effective, efficient, and maintainable.
- Effective test suites can detect as many defects as possible with a high level of confidence and coverage.
- Efficient test suites can minimize the cost and effort of testing while maximizing the value and benefit of testing.
- Maintainable test suites can be easily updated, modified, or reused when the software changes or evolves.

