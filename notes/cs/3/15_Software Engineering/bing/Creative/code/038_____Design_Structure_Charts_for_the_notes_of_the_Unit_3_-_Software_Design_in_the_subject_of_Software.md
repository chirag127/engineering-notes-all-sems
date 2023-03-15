### Design Structure Charts

- A design structure chart (DSC) is a diagram that shows the hierarchical decomposition of a software system into its modules and their relationships  .
- A DSC is a useful tool for software design because it helps to identify the main functions of the system, the data flow between them, the cohesion and coupling of the modules, and the potential for reuse and testing.
- A DSC can be drawn using different notations, such as boxes, circles, arrows, lines, etc. The most common notation is the one proposed by Edward Yourdon and Larry Constantine, which uses boxes for modules, arrows for data flow, and lines for control flow .
- A DSC can be classified into two types: transform centered and transaction centered.
  - A transform centered DSC is designed for the systems that receive an input which is transformed by a sequence of operations carried out by one module. The input and output data are shown at the top and bottom of the diagram, respectively, and the modules are arranged in a vertical hierarchy.
  - A transaction centered DSC is designed for the systems that process a number of different types of transactions. The transactions are shown at the top of the diagram, and the modules are arranged in a horizontal hierarchy. Each module handles one or more transactions, and may call other modules for subtasks.
- A DSC can be refined by adding more details, such as the data types, the parameters, the return values, the error handling, the conditions, etc. The refinement can be done by using different levels of abstraction, such as the conceptual, the specification, and the implementation level .
- A DSC can be verified by checking its consistency, completeness, correctness, and clarity. Some of the criteria for verification are :
  - The DSC should match the requirements and the specifications of the system.
  - The DSC should have a clear and logical structure, with no unnecessary or redundant modules.
  - The DSC should have high cohesion and low coupling, meaning that each module should perform a single and well-defined task, and the dependencies between modules should be minimal.
  - The DSC should have balanced fan-in and fan-out, meaning that each module should have a reasonable number of inputs and outputs, and avoid excessive branching or calling.
  - The DSC should have clear and consistent naming conventions, symbols, and labels for the modules and the data.
- A DSC can be used as a basis for other software engineering activities, such as coding, testing, debugging, documentation, maintenance, etc. A DSC can also be converted into other types of diagrams, such as flowcharts, pseudocode, state diagrams, etc .
- A DSC is an example of a software architecture diagram, which is a high-level representation of the structure and behavior of a software system. There are other types of software architecture diagrams, such as component diagrams, deployment diagrams, class diagrams, etc., which show different aspects of the system, such as the physical, logical, static, or dynamic views .