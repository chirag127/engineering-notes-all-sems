#### Function Oriented Design in Software Design

- Function Oriented Design is an approach to software design where the design is decomposed into a set of interacting units or modules where each unit or module has a clearly defined function .
- The design process for software systems often has two levels. At the first level, the focus is on deciding which modules are needed for the system on the basis of SRS (Software Requirement Specification) and how the modules should be interconnected.
- The design can be represented graphically or mathematically by the following notations:
  - Data Flow Diagram (DFD): A data flow diagram (DFD) maps out the flow of information for any process or system. It uses defined symbols like rectangles, circles and arrows, plus short text labels, to show data inputs, outputs, storage points and the routes between each destination .
  - Data Dictionaries: Data dictionaries are simply repositories to store information about all data items defined in DFDs. At the requirement stage, data dictionaries contains data items. Data dictionaries include Name of the item, Aliases (Other names for items), Description / purpose, Related data items, Range of values, Data structure definition / form .
  - Structure Charts: It is the hierarchical representation of system which partitions the system into black boxes (functionality is known to users but inner details are unknown). Components are read from top to bottom and left to right. When a module calls another, it views the called module as black box, passing required parameters and receiving results.
  - Pseudo Code: Pseudo Code is system description in short English like phrases describing the function. It use keyword and indentation. Pseudo codes are used as replacement for flow charts. It decreases the amount of documentation required.
- The advantages of Function Oriented Design are:
  - It is easy to understand and implement.
  - It is suitable for small and simple systems.
  - It supports top-down design and modularization.
  - It facilitates testing and maintenance.
- The disadvantages of Function Oriented Design are:
  - It does not model the real world well.
  - It does not support reusability and abstraction.
  - It does not handle complex data structures and relationships.
  - It does not cope well with changes in requirements and functionality.