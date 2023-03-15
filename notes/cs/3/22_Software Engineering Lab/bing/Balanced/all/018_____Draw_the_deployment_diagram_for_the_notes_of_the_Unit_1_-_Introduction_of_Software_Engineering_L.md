# Deployment Diagram for the Notes of the Unit 1 - Introduction of Software Engineering Lab

- A deployment diagram is a type of UML diagram that shows the physical arrangement of software components and hardware nodes in a system.
- A deployment diagram can be used to model the distribution of software artifacts to different devices, the communication links between them, and the properties of the nodes and links.
- A deployment diagram consists of the following elements:
  - Nodes: represent physical devices or machines that host software components. Nodes can be nested to show hierarchical structures. Nodes can have stereotypes to indicate their types, such as <<device>>, <<server>>, <<client>>, <<database>>, etc.
  - Components: represent modular units of software that provide some functionality or service. Components can be deployed to nodes and communicate with each other through interfaces and ports. Components can have stereotypes to indicate their types, such as <<application>>, <<web>>, <<ejb>>, <<dll>>, etc.
  - Artifacts: represent physical files or documents that are produced or used by software components. Artifacts can be deployed to nodes and associated with components. Artifacts can have stereotypes to indicate their types, such as <<source>>, <<executable>>, <<script>>, <<image>>, etc.
  - Links: represent physical connections or channels between nodes. Links can have properties to specify their characteristics, such as bandwidth, latency, protocol, etc.
  - Dependencies: represent logical relationships or dependencies between components or artifacts. Dependencies can have stereotypes to indicate their types, such as <<use>>, <<call>>, <<create>>, <<derive>>, etc.

- A possible deployment diagram for the notes of the Unit 1 - Introduction of Software Engineering Lab is shown below:

```mermaid
graph TD
  subgraph Node1[<<device>> Laptop]
    C1[<<application>> SE Lab Notes] --> A1[<<source>> Unit 1.docx]
    C1 --> A2[<<executable>> Unit 1.pdf]
    C1 --> A3[<<image>> Unit 1.png]
  end
  subgraph Node2[<<device>> Printer]
    A2 --> C2[<<application>> Print Service]
  end
  subgraph Node3[<<device>> Smartphone]
    C3[<<application>> SE Lab App] --> A4[<<source>> Unit 1.html]
    C3 --> A5[<<executable>> Unit 1.apk]
    C3 --> A6[<<image>> Unit 1.jpg]
  end
  Node1 -- USB --> Node2
  Node1 -- Wi-Fi --> Node3
  C1 ..> C3 : <<use>>
  A1 ..> A4 : <<derive>>
  A2 ..> A5 : <<derive>>
  A3 ..> A6 : <<derive>>
```