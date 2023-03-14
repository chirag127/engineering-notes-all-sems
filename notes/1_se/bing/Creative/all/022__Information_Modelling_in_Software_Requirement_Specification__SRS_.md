### Information Modelling in Software Requirement Specification (SRS)

- Information modelling is a process of representing the concepts, relationships, constraints, rules, and operations of a domain of interest in an abstract and formal way. 
- Information modelling helps to specify the data semantics and structure for a chosen domain, such as a software system, a facility, a building, a plant, etc. 
- Information modelling can provide a sharable, stable, and organized way of expressing the information requirements or knowledge for the domain context. 
- Information modelling is independent of any implementation details, such as database design, programming language, or platform. It can be mapped to different data models, such as object models, entity-relationship models, or XML schemas. 
- Information modelling is usually done using a graphical notation, such as the Entity-Relationship (ER) diagram, the Integration Definition for Information Modeling (IDEF1X), the EXPRESS language, or the Unified Modeling Language (UML).  
- Information modelling can also be done using a linguistic approach, such as the Fact Oriented Modeling (FOM) languages, which are based on propositions rather than entities. FOM languages include Object-Role Modeling (ORM) and Fully Communication Oriented Information Modeling (FCO-IM). 
- Information modelling is an essential part of the Software Requirement Specification (SRS) document, which describes what the software will do and how it will perform. 
- The SRS document is an official and formal document that defines the scope, functionality, quality, and constraints of the software system. 
- The SRS document is created before starting the development work, and it serves as a single source of truth for all the stakeholders involved in the software project, such as developers, testers, customers, users, etc. 
- The SRS document helps to ensure that the software system meets the needs and expectations of the stakeholders, and that the software development process is aligned with the business goals and user requirements. 
- The SRS document can also help to estimate the time, cost, and resources needed for the software project, and to make decisions about the software lifecycle, such as when to add, modify, or retire features. 
- The SRS document typically consists of four main sections: 
  - Introduction: This section provides the background, purpose, scope, and overview of the software system, and identifies the stakeholders, assumptions, dependencies, and risks involved in the project. 
  - System Description: This section describes the general characteristics and features of the software system, such as the system context, the system architecture, the system functions, the system interfaces, the system modes, the system states, the system data, etc. 
  - System Requirements: This section specifies the functional and non-functional requirements of the software system, such as the user requirements, the performance requirements, the reliability requirements, the security requirements, the usability requirements, the maintainability requirements, the compatibility requirements, the legal requirements, etc. 
  - System Validation: This section defines the criteria and methods for verifying and validating that the software system meets the specified requirements, such as the test cases, the test procedures, the test tools, the test environment, the test results, the test reports, etc. 

- A mnemonic to remember the four main sections of the SRS document is: **ISRS** (Introduction, System Description, System Requirements, System Validation). 

- An example of an information model for a CD collection database using the ER diagram notation is shown below: 

```
+----------------+       +----------------+       +----------------+
|    Artist      |       |     Album      |       |     Track      |
+----------------+       +----------------+       +----------------+
| Artist_ID (PK) |<----->| Artist_ID (FK) |       | Track_ID (PK)  |
| Artist_Name    |       | Album_ID (PK)  |<----->| Album_ID (FK)  |
+----------------+       | Album_Title    |       | Track_Title    |
                         | Album_Year     |       | Track_Duration |
                         +----------------+       +----------------+
```

- An example of an information model for the same CD collection database using the FCO-IM notation is shown below: [^2