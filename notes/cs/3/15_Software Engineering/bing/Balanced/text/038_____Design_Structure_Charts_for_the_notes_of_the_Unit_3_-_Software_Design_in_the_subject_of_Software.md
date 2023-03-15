### Design Structure Charts

- A design structure chart (DSC) is a diagram that shows the hierarchical decomposition of a software system into modules and their interconnections.
- A DSC is a top-down modular design tool that helps to identify the main functions of the system, the subfunctions that support them, and the data flow between them.
- A DSC can be used to specify the high-level design or architecture of a software system, as well as to document and communicate the design decisions and rationale.
- A DSC consists of squares representing the modules, lines representing the data flow, and symbols representing the type and direction of the data flow.
- A DSC can be classified into three types based on the nature of the system: transform centered, transaction centered, and call and return centered.

#### Transform Centered DSC

- A transform centered DSC is designed for a system that receives an input, transforms it through a sequence of operations, and produces an output.
- A transform centered DSC has a clear input and output module, and a central transform module that contains the main logic of the system.
- A transform centered DSC can be further divided into horizontal and vertical partitions, depending on the level of abstraction and cohesion of the modules.
- A horizontal partition separates the modules into different levels of abstraction, such as input, output, control, and processing.
- A vertical partition separates the modules into different functional areas, such as validation, calculation, and formatting.

#### Transaction Centered DSC

- A transaction centered DSC is designed for a system that processes a number of different types of transactions, each with its own logic and data flow.
- A transaction centered DSC has a central dispatcher module that receives the transactions, identifies their type, and invokes the appropriate handler module for each transaction.
- A transaction centered DSC can have multiple input and output modules, depending on the sources and destinations of the transactions.
- A transaction centered DSC can also have common modules that are shared by different handler modules, such as database access, error handling, and logging.

#### Call and Return Centered DSC

- A call and return centered DSC is designed for a system that consists of a main module that calls and returns from other modules, which may in turn call and return from other modules.
- A call and return centered DSC has a hierarchical structure that reflects the nesting and scope of the module calls.
- A call and return centered DSC can have multiple input and output modules, depending on the user interface and data sources of the system.
- A call and return centered DSC can also have library modules that provide common services and functions to other modules, such as mathematical operations, string manipulation, and sorting.