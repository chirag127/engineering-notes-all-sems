Static Testing Strategies in Software Testing are methods to check the defects in software without actually executing the code. Static testing can be done in two ways: review and static analysis   .

Review is a process of examining the documents and code to find potential defects in the design and requirements of the software. Review can be done in different ways, such as informal, walkthrough, peer review and inspection   .

Static analysis is a process of evaluating the code quality and structure to find defects that may cause errors or failures when the software is executed. Static analysis can be done using different tools and techniques, such as data flow, control flow and cyclomatic complexity   .

The following diagram illustrates the basic architecture of a static testing strategy in software testing:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Requirement    |     |  Design         |     |  Code           |
|  Specification  |     |  Specification  |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
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
       v                      v                      v
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Review         |     |  Review         |     |  Static         |
|                 |     |                 |     |  Analysis       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
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
       v                      v                      v
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Defects        |     |  Defects        |     |  Defects        |
|  Identification  |     |  Identification  |     |  Identification  |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```