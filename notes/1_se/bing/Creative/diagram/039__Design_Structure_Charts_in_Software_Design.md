A design structure chart (DSC) is a diagram that shows the hierarchical decomposition of a software system into its modules and the data flow between them. It is a tool for top-down design and functional decomposition of a software system. It helps to identify the modules, their interfaces, and the data they exchange.

A DSC consists of the following symbols:

- A rectangle represents a module, which is a unit of functionality in the system. The name of the module is written inside the rectangle.
- A line with an empty circle at the end represents a data flow, which is the movement of data between modules. The direction of the data flow is indicated by the arrow. The name of the data is written above or below the line.
- A line with a filled circle at the end represents a control flow, which is the transfer of control between modules. The direction of the control flow is indicated by the arrow. The name of the condition or event that triggers the control flow is written above or below the line.
- A dashed line with an empty circle at the end represents a library module, which is a reusable module that can be invoked from any module. The name of the library module is written inside the rectangle.
- A diamond represents a conditional call, which is a branching of control flow based on a condition. The condition is written inside the diamond. The lines that emanate from the diamond represent the alternative control flows based on the condition.
- A curved arrow represents a loop, which is a repetition of control flow. The loop condition is written above or below the arrow. The modules that are enclosed by the loop are executed repeatedly until the loop condition is false.

#### Design Structure Charts in Software Design

The following diagram illustrates the basic architecture of a word processor:

```
+-----------------+
|  Word Processor |
+-----------------+
       |  |
       |  | Document
       |  V
+-----------------+
|  File Manager   |
+-----------------+
       |  |
       |  | File
       |  V
+-----------------+
|  Disk Manager   |
+-----------------+
       |  |
       |  | Disk
       |  V
+-----------------+
|  Operating Sys. |
+-----------------+
```

The following diagram illustrates a transform-centered structure chart for a system that converts a text file into a PDF file:

```
+-----------------+
|  Text to PDF    |
+-----------------+
       |  |
       |  | Text File
       |  V
+-----------------+
|  Parse Text     |
+-----------------+
       |  |
       |  | Text Elements
       |  V
+-----------------+
|  Format PDF     |
+-----------------+
       |  |
       |  | PDF Elements
       |  V
+-----------------+
|  Generate PDF   |
+-----------------+
       |  |
       |  | PDF File
       |  V
+-----------------+
|  Save PDF       |
+-----------------+
```

The following diagram illustrates a transaction-centered structure chart for a system that processes different types of bank transactions:

```
+-----------------+
|  Bank System    |
+-----------------+
       |  |
       |  | Transaction
       |  V
+-----------------+
|  Validate Trans.|
+-----------------+
       |  |
       |  | Valid Trans.
       |  V
+-----------------+
|  Process Trans. |
+-----------------+
       |  |
       |  | Result
       |  V
+-----------------+
|  Update Account |
+-----------------+
       |  |
       |  | Balance
       |  V
+-----------------+
|  Display Result |
+-----------------+
```

The following diagram illustrates a structure chart with a library module, a conditional call, and a loop:

```
+-----------------+
|  Calculator     |
+-----------------+
       |  |
       |  | Expression
       |  V
+-----------------+
|  Evaluate Exp.  |
+-----------------+
       |  |
       |  | Result
       |  V
+-----------------+
|  Display Result |
+-----------------+
       |  |
       |  | Continue?
       |  V
+-----------------+
|  Get Input      |
+-----------------+
       |  |
       |  | Expression
       |  V
+-----------------+
|  Validate Input |
+-----------------+
       |  |
       |  | Valid Input
       |  V
+-----------------+    +----------------