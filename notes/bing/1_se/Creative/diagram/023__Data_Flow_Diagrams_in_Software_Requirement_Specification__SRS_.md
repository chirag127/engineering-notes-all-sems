A data flow diagram (DFD) is a graphical representation of the flow of data through a system or process. It shows how data is input, processed, stored, and output in a system or process. A DFD can be used to document the current or desired state of a system or process, to identify problems or opportunities for improvement, or to communicate requirements and specifications.

To draw a data flow diagram, you need to follow these steps:

1. Define the scope and boundary of the system or process you want to model. This can be done by drawing a context DFD, which shows the system or process as a single process with inputs and outputs from external entities (such as users, other systems, or data sources).
2. Decompose the system or process into smaller and more detailed processes. This can be done by drawing a level 1 DFD, which shows the main processes and data flows within the system or process. Each process in the level 1 DFD can be further decomposed into sub-processes in lower level DFDs, until the desired level of detail is reached.
3. Identify the data stores and data flows in the system or process. A data store is a place where data is stored, such as a database, a file, or a memory. A data flow is a movement of data from one process, data store, or external entity to another. Data flows are labeled with the name and description of the data being transferred.
4. Draw the diagram using standard symbols and notation. A DFD consists of four main elements: processes, data stores, data flows, and external entities. Processes are represented by circles or rounded rectangles, data stores are represented by open-ended rectangles, data flows are represented by arrows, and external entities are represented by squares or rectangles. Each element should have a unique name and number, and each data flow should have a descriptive label.

### Data Flow Diagrams in Software Requirement Specification (SRS)

The following diagram illustrates the basic architecture of a web-based online shopping system:

```
+----------------+         +----------------+         +----------------+
|                |         |                |         |                |
|   Customer     |         |   Web Server   |         |   Database     |
|                |         |                |         |                |
+----------------+         +----------------+         +----------------+
     |   ^                      |   ^                      |   ^
     |   |                      |   |                      |   |
     |   |                      |   |                      |   |
     |   |                      |   |                      |   |
     |   |                      |   |                      |   |
     |   |                      |   |                      |   |
     |   |                      |   |                      |   |
     |   |                      |   |                      |   |
     |   |                      |   |                      |   |
     |   |                      |   |                      |   |
     |   |                      |   |                      |   |
     v   |                      v   |                      v   |
+----------------+         +----------------+         +----------------+
|                |         |                |         |                |
|   Register     |         |   Validate     |         |   Store        |
|                |         |   Credentials  |         |   Customer     |
|                |         |                |         |   Data         |
|                |         |                |         |                |
+----------------+         +----------------+         +----------------+
     |   ^                      |   ^                      |   ^
     |   |                      |   |                      |   |
     |   |                      |   |                      |   |
     v   |                      v   |                      v   |
+----------------+         +----------------+         +----------------+
|                |         |                |         |                |
|   Browse       |         |   Display      |         |   Retrieve     |
|   Products     |         |   Products     |         |   Product      |
|                |         |                |         |   Data         |
|                |         |                |         |                |
+----------------+         +----------------+         +----------------+
     |   ^                      |   ^                      |   ^
     |   |                      |   |                      |   |
     |   |                      |   |                      |   |
     v   |                      v   |                      v   |
+----------------+         +----------------+         +----------------+
|                |         |                |         |                |
|   Add to Cart  |         |   Update       |         |   Store        |
|                |         |   Cart         |