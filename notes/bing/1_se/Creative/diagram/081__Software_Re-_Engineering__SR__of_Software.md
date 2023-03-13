Software re-engineering is a process of software development which is done to improve the maintainability of a software system. It involves examining and altering an existing system to reconstitute it in a new form. It encompasses a combination of sub-processes such as reverse engineering, forward engineering, reconstructing, etc.

### Software Re- Engineering (SR) of Software

The following diagram illustrates the basic architecture of a software re-engineering process:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Inventory     |     |  Document      |     |  Reverse       |
|  Analysis      |---->|  Reconstructing|---->|  Engineering   |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Data          |     |  Program        |     |  Forward       |
|  Re-engineering|<----|  Re-engineering |<----|  Engineering   |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Testing       |     |  Maintenance   |     |  Reuse         |
|                |---->|                |---->|                |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
```

The main steps of the software re-engineering process are:

- Inventory analysis: This step involves identifying and evaluating all the applications in the software organization's inventory. The goal is to determine which applications are candidates for re-engineering, which ones are obsolete, and which ones are still useful.
- Document reconstructing: This step involves recovering and updating the documentation of the selected applications. Documentation can include user manuals, design specifications, test cases, etc. The goal is to provide accurate and consistent information about the system's functionality and operation.
- Reverse engineering: This step involves extracting the design and structure of the system from its source code and data. The goal is to understand the system's architecture, components, dependencies, interfaces, etc. Reverse engineering can use various techniques such as static analysis, dynamic analysis, data flow analysis, etc.
- Program re-engineering: This step involves modifying the source code of the system to improve its quality, performance, and maintainability. Program re-engineering can use various techniques such as restructuring, refactoring, modularization, etc. The goal is to make the code more readable, understandable, and reusable.
- Data re-engineering: This step involves modifying the data structures and schemas of the system to improve their efficiency, consistency, and integrity. Data re-engineering can use various techniques such as normalization, denormalization, migration, etc. The goal is to make the data more suitable for the system's requirements and operations.
- Forward engineering: This step involves generating a new system from the modified source code and data. The goal is to produce a system that meets the current and future needs of the users and stakeholders. Forward engineering can use various techniques such as code generation, compilation, linking, etc.
- Testing: This step involves verifying and validating the functionality and quality of the new system. Testing can use various techniques such as unit testing, integration testing, system testing, etc. The goal is to ensure that the system meets the specifications and expectations of the users and stakeholders.
- Maintenance: This step involves providing ongoing support and improvement