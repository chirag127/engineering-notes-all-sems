# Design Structure Charts

Design structure charts are graphical representations of the modules and their interactions in a software system. They are used to show the hierarchical decomposition of a system into its components, the data flow between the components, and the functional abstraction of each component  .

Some of the benefits of using design structure charts are:

- They help to identify the main functions and subfunctions of a system and their relationships.
- They help to modularize the system and reduce coupling and complexity.
- They help to document the design and communicate it to other stakeholders.
- They help to verify the correctness and completeness of the design.

Some of the elements of a design structure chart are:

- Modules: Rectangular boxes that represent the components of the system. Each module has a name and a number. The name describes the function of the module and the number indicates its level in the hierarchy. The top-level module is numbered 0 and the lower-level modules are numbered 1, 2, 3, etc.   
- Connections: Lines that connect the modules and show the direction of data flow. The connections can be labeled with the name and type of the data that is passed between the modules. The type of the data can be scalar, array, record, pointer, etc.   
- Control flags: Symbols that indicate the conditions or events that trigger the execution of a module. The control flags can be placed on the connections or on the modules. Some of the common control flags are:   
  - Loop: A circle that indicates that a module is executed repeatedly until a condition is met.
  - Selection: A diamond that indicates that a module is executed only if a condition is true.
  - Case: A hexagon that indicates that a module is executed based on the value of a variable.
  - Interrupt: A lightning bolt that indicates that a module is executed when an external event occurs.
  - Call: An arrow that indicates that a module is executed by another module.
- Coupling: The degree of interdependence between the modules. The coupling can be measured by the number and type of connections between the modules. The lower the coupling, the better the design. Some of the types of coupling are:   
  - Data coupling: The modules exchange only data and not control information.
  - Stamp coupling: The modules exchange composite data structures, such as records or arrays.
  - Control coupling: The modules exchange control information, such as flags or parameters.
  - Common coupling: The modules share global data or variables.
  - Content coupling: The modules directly access or modify the internal data or code of another module.

Some of the types of design structure charts are:

- Transform centered structure: A structure that describes a system that receives an input, transforms it by a sequence of operations, and produces an output. The structure has a clear input-output flow and a single top-level module. 
- Transaction centered structure: A structure that describes a system that processes a number of different types of transactions. The structure has a dispatcher module that selects the appropriate module to handle each transaction. 
- Call and return structure: A structure that describes a system that consists of a main module that calls other modules and returns to the main module after each call. The structure has a linear control flow and a modular design. 
- Object oriented structure: A structure that describes a system that consists of a number of objects that interact with each other by sending and receiving messages. The structure has a dynamic and decentralized control flow and a high degree of encapsulation and abstraction. 
- Layered structure: A structure that describes a system that consists of a number of layers that provide different levels of abstraction and functionality. The structure has a hierarchical and modular design and a clear separation of concerns.