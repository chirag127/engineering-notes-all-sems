### Data Flow Diagrams

- A data flow diagram (DFD) is a graphical representation of the flow of data and information in a system or process.
- A DFD shows the sources and destinations of data, the processes that transform data, the data stores that hold data, and the data flows that connect them.
- A DFD can be used to model the logical or physical aspects of a system, or both.
- A DFD can be used for analysis or design of software systems, business processes, or any other system that involves data processing.
- A DFD can help software engineers to understand the operation and limitations of a system, to identify the requirements and specifications of a system, and to communicate and document the system design.

### Types of Data Flow Diagrams

- There are two main types of data flow diagrams: context diagrams and levelled diagrams.
- A context diagram is the highest-level DFD, which shows the system as a single process and its interaction with external entities (such as users, customers, or other systems).
- A levelled diagram is a DFD that decomposes the system into multiple levels of detail, showing the sub-processes and data flows within each process.
- A levelled diagram can use different notations, such as Yourdon and Coad, Gane and Sarson, or UML, to represent the processes, data stores, data flows, and external entities.
- A levelled diagram can use different numbering schemes, such as balanced, exploded, or partitioned, to indicate the hierarchy and relationship of the processes.

### Symbols and Notations of Data Flow Diagrams

- The common symbols and notations used in data flow diagrams are:

  - Process: A process is a transformation or manipulation of data, such as calculation, sorting, or filtering. A process is represented by a circle, a rectangle, or a rounded rectangle, with a name or a number inside.
  - Data store: A data store is a place where data is stored or retrieved, such as a database, a file, or a memory. A data store is represented by two parallel lines, with a name or a number above or between them.
  - Data flow: A data flow is a movement or transfer of data from one point to another, such as input, output, or feedback. A data flow is represented by an arrow, with a name or a label above or along it.
  - External entity: An external entity is a source or destination of data that is outside the system boundary, such as a user, a customer, or another system. An external entity is represented by a square, a rectangle, or an oval, with a name inside.

### Example of Data Flow Diagram

- Here is an example of a data flow diagram for an online shopping system, using the Yourdon and Coad notation and the balanced numbering scheme:

![DFD Example](https://www.edrawmax.com/images/article/data-flow-diagram-in-software-engineering-1.png)

- The context diagram shows the system as a single process (Online Shopping System) and its interaction with four external entities (Customer, Bank, Delivery Service, and Supplier).
- The level 1 diagram shows the main sub-processes of the system (Customer Registration, Product Browsing, Order Processing, Payment Processing, Delivery Processing, and Inventory Management) and the data flows between them and the external entities.
- The level 2 diagram shows the further decomposition of one of the sub-processes (Order Processing) into four sub-processes (Order Confirmation, Order Fulfillment, Order Cancellation, and Order Tracking) and the data flows between them and the data stores (Customer Database, Product Database, and Order Database).