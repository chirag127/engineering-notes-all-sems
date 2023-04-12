

## Identifying the Requirements from Problem Statements for the notes of the Software Engineering Mapping with Virtual Lab Lab in the subject of Software Engineering

- A problem statement is a concise description of an issue or a need that a software system aims to address or fulfill.
- A requirement is a condition or capability that a software system must have or meet to satisfy the problem statement and the stakeholders' needs and expectations.
- Identifying the requirements from problem statements is a crucial step in software engineering, as it helps to define the scope, objectives, and specifications of the software system.
- To identify the requirements from problem statements, the following steps can be followed:

  - Analyze the problem statement and identify the main goals and objectives of the software system.
  - Identify the stakeholders and their roles, needs, and expectations from the software system.
  - Elicit the functional and non-functional requirements from the stakeholders using various techniques, such as interviews, questionnaires, surveys, observation, prototyping, etc.
  - Prioritize the requirements based on their importance, urgency, and feasibility.
  - Document the requirements using appropriate formats, such as natural language, use cases, user stories, etc.
  - Validate and verify the requirements with the stakeholders and resolve any conflicts or ambiguities.
  - Manage and update the requirements throughout the software development life cycle, as new information or changes arise.

- Some examples of problem statements and their corresponding requirements are:

  - Problem statement: A library management system that allows librarians to manage the books and the borrowers, and allows the borrowers to search, reserve, and borrow books online.
  - Requirements:
    - Functional requirements:
      - The system shall allow librarians to add, update, delete, and view the details of books and borrowers in the database.
      - The system shall allow librarians to issue, return, and renew books for the borrowers.
      - The system shall allow librarians to generate reports on the books and the borrowers, such as overdue books, popular books, etc.
      - The system shall allow borrowers to register, login, and update their profiles online.
      - The system shall allow borrowers to search, reserve, and borrow books online, subject to availability and borrowing limits.
      - The system shall send notifications to the borrowers via email or SMS about their reservations, borrowings, and due dates.
    - Non-functional requirements:
      - The system shall be user-friendly and easy to use for both librarians and borrowers.
      - The system shall be secure and protect the privacy and confidentiality of the books and the borrowers' data.
      - The system shall be reliable and available 24/7 for online access.
      - The system shall be scalable and able to handle a large number of books and borrowers.
      - The system shall be compatible with various browsers and devices.

  - Problem statement: A hotel booking system that allows customers to search, compare, and book hotels online, and allows hotel owners to manage their hotels and bookings.
  - Requirements:
    - Functional requirements:
      - The system shall allow customers to search for hotels based on various criteria, such as location, price, rating, amenities, etc.
      - The system shall allow customers to compare the features and prices of different hotels and view the reviews and ratings from other customers.
      - The system shall allow customers to book hotels online, subject to availability and payment confirmation.
      - The system shall allow customers to cancel or modify their bookings online, subject to cancellation and modification policies.
      - The system shall send confirmations and reminders to the customers via email or SMS about their bookings and check-in and check-out dates.
      - The system shall allow hotel owners to register, login, and update their hotel details and availability online.
      - The system shall allow hotel owners to view and manage their bookings and payments online.
      - The system shall allow hotel owners to receive feedback and ratings from the customers and respond to them online.
    - Non-functional requirements:
      - The system shall be user-friendly and easy to use for both customers and hotel owners.
      - The system shall be secure and protect the privacy and confidentiality of the hotels and the customers' data.
      - The system shall be reliable and available 24/7 for online access.
      - The system shall be scalable and able to handle a large number of hotels and customers.
      - The system shall be compatible with various browsers and devices.



## Estimation of Project Metrics for the notes of the Software Engineering Mapping with Virtual Lab Lab in the subject of Software Engineering

- Estimation of project metrics is the process of predicting the values of key parameters that affect the performance and quality of a software project, such as cost, effort, duration, scope, quality, and risk.
- Estimation of project metrics is important for software engineering because it helps to plan, monitor, and control the software development process, as well as to communicate with stakeholders and manage expectations.
- Estimation of project metrics is challenging because software projects are complex, uncertain, and dynamic, and involve human factors and external dependencies.
- Estimation of project metrics can be done at different levels of granularity, such as project, phase, activity, task, or resource.
- Estimation of project metrics can be done using different techniques, such as expert judgment, analogy, parametric, algorithmic, or machine learning.
- Estimation of project metrics can be done using different models, such as COCOMO, Function Point Analysis, Use Case Points, or Story Points.
- Estimation of project metrics can be improved by using historical data, calibration, validation, feedback, and adjustment.
- Estimation of project metrics can be supported by using tools, such as spreadsheets, estimation software, or project management software.

: https://savvycomsoftware.com/blog/software-project-estimation-in-software-engineering/
: https://www.geeksforgeeks.org/software-engineering-project-size-estimation-techniques/
: https://www.projectmanager.com/blog/software-development-estimation



## Modeling UML Use Case Diagrams and Capturing Use Case Scenarios

- UML stands for Unified Modeling Language, which is a standard way of visualizing and documenting the design of a software system.
- Use case diagrams are one of the types of UML diagrams that show the behavior and requirements of a system from the perspective of the users or actors.
- Use cases are the goals or tasks that the users want to achieve by interacting with the system. They describe **what** the system does, not **how** it does it.
- Use case diagrams consist of the following elements:
  - Actors: The external entities that interact with the system. They can be people, organizations, or other systems. They are represented by stick figures or icons.
  - Use cases: The functions or services that the system provides to the actors. They are represented by ovals with names inside.
  - System boundary: The scope or boundary of the system under consideration. It is represented by a rectangle that encloses the use cases.
  - Associations: The relationships between the actors and the use cases. They are represented by solid lines with optional multiplicity indicators.
  - Generalizations: The relationships that indicate that one actor or use case inherits the characteristics of another actor or use case. They are represented by dashed lines with empty arrowheads.
  - Include relationships: The relationships that indicate that one use case includes the behavior of another use case as a part of its normal execution. They are represented by dashed lines with the keyword "include" and an arrowhead pointing to the included use case.
  - Extend relationships: The relationships that indicate that one use case extends the behavior of another use case under certain conditions. They are represented by dashed lines with the keyword "extend" and an arrowhead pointing to the extended use case.
  - Packages: The logical grouping of related elements in a use case diagram. They are represented by tabbed rectangles with names inside.

- An example of a use case diagram for an online shopping system is shown below:

Use case diagram example

- Capturing use case scenarios is the process of describing the steps or interactions that occur between the actors and the system for each use case.
- Use case scenarios can be captured in different ways, such as:
  - Textual descriptions: The simplest way of capturing use case scenarios is by writing them in natural language, using a template or a format that specifies the name, description, preconditions, postconditions, main flow, alternative flows, and exceptions of each use case.
  - Activity diagrams: A graphical way of capturing use case scenarios is by using activity diagrams, which show the sequence of actions and decisions that occur within a use case. They use symbols such as circles, arrows, diamonds, and bars to represent the elements of a use case scenario.
  - Sequence diagrams: Another graphical way of capturing use case scenarios is by using sequence diagrams, which show the interactions and messages that occur between the actors and the system for a use case. They use symbols such as boxes, lines, arrows, and lifelines to represent the elements of a use case scenario.

- An example of a textual description for the use case "Place Order" in the online shopping system is shown below:

| Name | Place Order |
| --- | --- |
| Description | The customer places an order for the items in the shopping cart. |
| Preconditions | The customer has logged in and has items in the shopping cart. |
| Postconditions | The order is confirmed and the payment is processed. |
| Main flow | 1. The customer clicks on the "Checkout" button. <br> 2. The system displays the order summary and the payment options. <br> 3. The customer selects a payment option and enters the payment details. <br> 4. The system validates the payment details and processes the payment. <br> 5. The system confirms the order and sends a confirmation email to the customer. |
| Alternative flows | 3a. The customer cancels the order. <br> 3a1. The system returns to the shopping cart page. <br> 4a. The payment details are invalid or the payment is declined. <br> 4a1. The system displays an error message and asks the customer to enter the payment details again. |
| Exceptions | 2a. The shopping cart is empty. <br> 2a1. The system displays a message that the shopping cart is empty and redirects the customer



## E-R Modeling from the Problem Statements

- Entity-Relationship (ER) model is a high-level data model that represents the logical design of a database.
- ER model abstracts real-world objects (or concepts) as entities, and their associations as relationships.
- ER model helps to identify the possible entity sets, their attributes, and the cardinality and participation constraints of the relationships among them.
- ER model can be represented pictorially as an ER diagram, using graphical notations for entities, attributes, and relationships.
- ER diagram can be used to design, analyze, or troubleshoot a relational database.
- ER diagram can also be used to communicate the business information systems and requirements.
- Enhanced Entity-Relationship (EER) model is an extension of ER model that supports more complex and detailed design.
- EER model uses UML notation and incorporates concepts such as subclasses, superclasses, inheritance, and specialization.



## Identifying Domain Classes from the Problem Statements for the notes of the Software Engineering Mapping with Virtual Lab Lab in the subject of Software Engineering

- A domain class is a representation of a concept or an entity that is relevant to the problem domain and the system's requirements.
- A domain class has attributes (properties or characteristics) and operations (behaviors or actions) that describe its state and behavior.
- A domain class diagram is a graphical notation that shows the domain classes and their relationships in the problem domain.
- Identifying domain classes from the problem statements is a process of extracting the relevant concepts or entities from the textual description of the problem and representing them as domain classes.
- The steps for identifying domain classes from the problem statements are:

  - Read the problem statement carefully and identify the nouns and noun phrases that represent the concepts or entities in the problem domain.
  - Eliminate the irrelevant, vague, or ambiguous nouns and noun phrases that are not related to the problem domain or the system's requirements.
  - For each remaining noun or noun phrase, determine if it is a domain class or an attribute of another domain class.
  - For each domain class, identify its attributes and operations based on the problem statement and the system's requirements.
  - Draw the domain class diagram using the appropriate notation and symbols. Show the domain classes, their attributes and operations, and their relationships with other domain classes. Use multiplicity, association names, and role names to indicate the nature and direction of the relationships.



## Statechart and Activity Modeling for the notes of the Software Engineering Mapping with Virtual Lab Lab in the subject of Software Engineering

- A statechart diagram is a kind of diagram used in computer science and related fields to describe the behavior of a system or an object over time.
- A statechart diagram shows the possible states of an object and the transitions between them. A state is a condition or situation that an object can be in, and a transition is a change from one state to another triggered by an event or a condition.
- A statechart diagram can have nested states, parallel states, entry and exit actions, guards, events, and actions.
- An activity diagram is a special kind of statechart diagram that focuses on the flow of actions and activities within a system or a process.
- An activity diagram shows the sequence and concurrency of actions, the synchronization and branching of flows, the use of swimlanes to partition activities by actors or objects, and the input and output of data.
- An activity diagram can have initial and final nodes, action nodes, control nodes, object nodes, pins, partitions, edges, and signals.
- Statechart diagrams and activity diagrams are two popular UML diagrams to visualize the dynamic behavior of an information system.
- Statechart diagrams and activity diagrams can be used to model the states and activities of classes, use cases, components, subsystems, or the whole system .
- Statechart diagrams and activity diagrams can be used for system analysis, design, simulation, testing, and documentation  .



## Modeling UML Class Diagrams and Sequence Diagrams

- UML stands for Unified Modeling Language, which is a standard way of representing the structure and behavior of a software system using graphical diagrams.
- UML class diagrams and sequence diagrams are two types of diagrams that can be used to model a software system from different perspectives.
- A class diagram shows the static structure of the system, such as the classes, interfaces, attributes, operations, and relationships among them.
- A sequence diagram shows the dynamic behavior of the system, such as the interactions among objects and the messages they exchange over time.
- Class diagrams and sequence diagrams can work together to allow precise modeling and communication of the system design and functionality.

### Class Diagrams

- A class diagram consists of the following elements:
  - Classes: A class is a blueprint for an object, which defines its attributes and operations. A class is represented by a rectangle with the class name on the top, followed by the attributes and operations in separate compartments.
  - Interfaces: An interface is a collection of abstract operations that a class can implement. An interface is represented by a circle with the interface name inside, or a rectangle with the stereotype <<interface>> above the interface name.
  - Attributes: An attribute is a property or characteristic of a class, such as name, age, or color. An attribute is represented by a line of text in the attribute compartment of the class, with the following syntax: visibility name : type [multiplicity] = default {property}
    - Visibility: The visibility of an attribute indicates who can access it. It can be public (+), protected (#), private (-), or package (~).
    - Name: The name of the attribute is a unique identifier within the class.
    - Type: The type of the attribute specifies the data type or class of the attribute value, such as int, String, or Student.
    - Multiplicity: The multiplicity of an attribute specifies how many instances of the attribute can exist for a single object. It can be a single value (1), a range (1..*), or a set of values (1,2,4).
    - Default: The default value of an attribute is the initial value assigned to the attribute when an object is created.
    - Property: The property of an attribute is a modifier that specifies additional constraints or behaviors of the attribute, such as readonly, derived, or unique.
  - Operations: An operation is a function or method that a class can perform, such as calculate, print, or save. An operation is represented by a line of text in the operation compartment of the class, with the following syntax: visibility name (parameter list) : return type {property}
    - Visibility: The visibility of an operation indicates who can invoke it. It can be public (+), protected (#), private (-), or package (~).
    - Name: The name of the operation is a unique identifier within the class.
    - Parameter list: The parameter list of an operation specifies the input and output parameters of the operation, separated by commas. Each parameter has the following syntax: direction name : type [multiplicity] = default {property}
      - Direction: The direction of a parameter indicates whether it is an input (in), output (out), or input/output (inout) parameter.
      - Name: The name of the parameter is a unique identifier within the operation.
      - Type: The type of the parameter specifies the data type or class of the parameter value, such as int, String, or Student.
      - Multiplicity: The multiplicity of a parameter specifies how many instances of the parameter can exist for a single invocation of the operation. It can be a single value (1), a range (1..*), or a set of values (1,2,4).
      - Default: The default value of a parameter is the value assigned to the parameter when the operation is invoked without specifying the parameter value.
      - Property: The property of a parameter is a modifier that specifies additional constraints or behaviors of the parameter, such as readonly, derived, or unique.
    - Return type: The return type of an operation specifies the data type or class of the value returned by the operation, such as int, String, or Student. If the operation does not return any value, the return type can be omitted.
    - Property: The property of an operation is a modifier that specifies additional constraints or behaviors of the operation, such as abstract, static, or query.
  - Relationships: A relationship is a connection or association between two or more classes or interfaces. There are different types of relationships, such as inheritance,



## Modeling Data Flow Diagrams for the notes of the Software Engineering Mapping with Virtual Lab Lab in the subject of Software Engineering

- A data flow diagram (DFD) is a graphical representation of the flow of data and information in a system or process. 
- DFDs are used to model the logical aspects of a system, such as what data is input, output, stored, and processed, and how data flows between different components. 
- DFDs are also used to identify the functional requirements, constraints, and dependencies of a system, and to facilitate communication and collaboration among stakeholders. 
- DFDs can be drawn at different levels of abstraction, from a high-level overview of the entire system (context diagram) to a detailed description of a specific function or process (level-n diagram). 
- DFDs use a set of standard symbols and notations, such as rectangles for external entities, circles for processes, arrows for data flows, and open-ended rectangles for data stores. 
- DFDs follow some basic rules and conventions, such as naming each element clearly and uniquely, balancing the inputs and outputs of each process, and avoiding crossing lines and loops. 
- DFDs can be created using various tools and software, such as EdrawMax, Lucidchart, Visio, and others.  
- DFDs can be verified and validated using techniques such as structured walkthroughs, inspections, reviews, and testing. 
- DFDs can be used to document, analyze, design, and improve software systems and processes in various fields and domains.



## Estimation of Test Coverage Metrics and Structural Complexity

- Test coverage metrics are used to measure and monitor the testing activity of a software program. They help to assess the thoroughness, effectiveness and efficiency of testing techniques.
- Structural complexity is a measure of how complex a program is in terms of its control flow and logic. It can be estimated by using control flow graphs (CFGs) and cyclomatic complexity.
- A CFG is a visual representation of the flow of control within a program. It consists of nodes and edges, where nodes represent basic blocks and edges represent transitions between them.
- A basic block is a sequence of statements that has a single entry point and a single exit point. It does not contain any branches or jumps.
- Cyclomatic complexity is a metric that counts the number of linearly independent paths in a CFG. It can be calculated by using the formula: `V(G) = E - N + 2`, where `V(G)` is the cyclomatic complexity, `E` is the number of edges, and `N` is the number of nodes in the CFG.
- Cyclomatic complexity can be used to estimate the minimum number of test cases required to achieve 100% branch coverage, which is a test coverage metric that ensures that every edge in the CFG is executed at least once.
- Other test coverage metrics include statement coverage, which ensures that every statement in the program is executed at least once, and path coverage, which ensures that every path in the CFG is executed at least once.
- Test coverage metrics can be used to identify the areas of the program that need more testing, to compare the quality of different testing techniques, and to evaluate the test adequacy.
- Test coverage metrics can be measured and reported by using software tools that analyze the source code and the test cases, and generate reports and graphs.
- Test coverage metrics and structural complexity are important concepts in software engineering, as they help to improve the reliability, maintainability and security of software programs.



## Designing Test Suites for the notes of the Software Engineering Mapping with Virtual Lab Lab in the subject of Software Engineering

- Test design is a significant step in the Software Development Life Cycle (SDLC), also known as creating test suites or testing a program.
- A test suite is a collection of test cases that are intended to be used as input to a software program to show that it has some specified set of behaviors (i.e., the behaviors listed in its specification).
- Test suites are created after the test plan. They include a number of tests and test cases. They describe the goals and objectives of test cases. They have test parameters, such as application, environment, version, etc.
- Test suites can be created on the basis of the test cycle as well as the test scope.
- Test suites can contain test cases for different levels of testing, such as unit, integration, system, and acceptance testing .
- Test suites can be organized in a logical order, such as the order of the user scenarios or the order of the software modules.
- Test suites can be executed manually or automatically, depending on the availability of test tools and test scripts .
- Test suites can be evaluated by comparing the actual outputs with the expected outputs, and by measuring the test coverage, test effectiveness, and test efficiency .

