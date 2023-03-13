### Software Quality Assurance (SQA) in SRS

Software Quality Assurance (SQA) is a process that assures that all software engineering processes, methods, activities, and work items are monitored and comply with the defined standards. These defined standards could be one or a combination of any like ISO 9000, CMMI model, ISO15504, etc.

Software Requirement Specification (SRS) is a document that describes the functional and non-functional requirements of a software system. It also defines the scope, assumptions, constraints, and quality attributes of the system.

A Software Quality Assurance Plan (SQAP) is a document that defines the procedures, techniques, and tools that are employed to make sure that a product or service aligns with the requirements defined in the SRS. It also describes the roles and responsibilities, quality metrics, quality audits, quality reviews, and quality improvement actions of the SQA team. 

The following diagram illustrates the basic architecture of a Software Quality Assurance Plan in relation to the Software Requirement Specification:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   SRS Document  |     |  SQA Activities |     |  SQAP Document  |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
| - Scope         |     | - Planning      |     | - Introduction  |
| - Assumptions   |     | - Monitoring    |     | - SQA Team      |
| - Constraints   |     | - Auditing      |     | - SQA Tasks     |
| - Requirements  |     | - Reviewing     |     | - SQA Tools     |
| - Attributes    |     | - Improving     |     | - SQA Metrics   |
|                 |     |                 |     | - SQA Audits    |
+-----------------+     +-----------------+     +-----------------+
          |                     |                         |
          |                     |                         |
          +---------------------+-------------------------+
                                |
                                |
                                v
                      +-----------------+
                      |                 |
                      |  Software System|
                      |                 |
                      +-----------------+
                      |                 |
                      | - Design        |
                      | - Development   |
                      | - Testing       |
                      | - Deployment    |
                      | - Maintenance   |
                      |                 |
                      +-----------------+
```