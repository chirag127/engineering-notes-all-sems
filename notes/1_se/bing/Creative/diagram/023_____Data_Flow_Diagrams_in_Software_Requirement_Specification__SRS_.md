A data flow diagram (DFD) is a graphical representation of the flow of data through a software system. It shows how data is input, processed, stored, and output by different components of the system. A DFD can be used to document the requirements of a software system and to communicate them to the stakeholders.

To draw a DFD in a software requirement specification (SRS) document, you can follow these steps:

1. Identify the main processes and data flows in the system. A process is an activity that transforms data, and a data flow is a movement of data between processes, data stores, or external entities. You can use circles or rounded rectangles to represent processes, and arrows to represent data flows. Label each process and data flow with a descriptive name.
2. Draw a context-level DFD that shows the system as a single process and its interactions with external entities. An external entity is a source or destination of data outside the system boundary. You can use squares or rectangles to represent external entities. Label each external entity with a descriptive name. The context-level DFD should provide an overview of the system scope and boundaries.
3. Draw a level-1 DFD that shows the main sub-processes and data flows within the system. You can decompose the system process into more detailed sub-processes and show how they interact with each other, data stores, and external entities. A data store is a place where data is stored for later use. You can use parallel lines or cylinders to represent data stores. Label each data store with a descriptive name. The level-1 DFD should provide a high-level view of the system functionality and data flow.
4. Draw level-2 or lower-level DFDs if needed to show more details of each sub-process and data flow. You can further decompose each sub-process into more specific sub-processes and show how they interact with each other, data stores, and data flows. You can use the same symbols and labels as in the previous levels. The lower-level DFDs should provide a detailed view of the system logic and data flow.

Here is an example of a DFD for a library management system:

### Data Flow Diagrams in Software Requirement Specification (SRS)

```
+----------------+       +-----------------+       +----------------+
|                |       |                 |       |                |
|  Library User  +------>+  Borrow Book    +------>+  Book Catalog  |
|                |       |                 |       |                |
+----------------+       +-----------------+       +----------------+
       ^                         |                         |
       |                         |                         |
       |                         v                         |
       |                  +-----------------+              |
       |                  |                 |              |
       +------------------+  Return Book    +--------------+
                          |                 |
                          +-----------------+
```