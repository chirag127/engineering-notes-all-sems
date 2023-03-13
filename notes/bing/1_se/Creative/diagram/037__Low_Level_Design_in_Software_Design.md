Low-level design (LLD) is a component-level design process that follows a step-by-step refinement process. This process can be used for designing data structures, required software architecture, source code and ultimately, performance algorithms.

A low-level design document (LLD) typically contains the following sections:

- Introduction: This section provides an overview of the system or component, its purpose, scope, objectives, and assumptions.
- Architecture: This section describes the overall architecture of the system or component, its components, interfaces, dependencies, and interactions.
- Modules: This section describes each module of the system or component in detail, including its name, description, inputs, outputs, functionality, algorithms, data structures, and pseudocode.
- Test cases: This section describes the test cases that will be used to verify the functionality and performance of the system or component, including the test inputs, expected outputs, and test steps.

A low-level design diagram is a graphical representation of the system or component, showing its components, interfaces, dependencies, and interactions. It can be drawn using various tools or notations, such as UML, ERD, or ASCII art.

The following is an example of a low-level design diagram for a simple calculator application, drawn using ASCII art:

```
+-----------------+        +-----------------+
| User Interface  |        | Business Logic  |
+-----------------+        +-----------------+
| - display       |        | - add           |
| - buttons       |        | - subtract      |
| - input         |        | - multiply      |
| - output        |        | - divide        |
+-----------------+        +-----------------+
       |  |                      |  |
       |  +----------------------+  |
       |        input/output        |
       +----------------------+  |
       |        events        |  |
       |  +----------------------+  |
       |  |                      |  |
+-----------------+        +-----------------+
| Data Access     |        | Data Storage    |
+-----------------+        +-----------------+
| - read          |        | - history       |
| - write         |        | - settings      |
+-----------------+        +-----------------+
```

: Low-level design - Wikipedia