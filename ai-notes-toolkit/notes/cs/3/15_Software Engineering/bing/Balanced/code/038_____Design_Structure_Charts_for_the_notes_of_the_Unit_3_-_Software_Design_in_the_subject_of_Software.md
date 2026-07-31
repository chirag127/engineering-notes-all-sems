### Design Structure Charts

- A design structure chart (DSC) is a diagram that shows the hierarchical decomposition of a software system into its modules and their relationships  .
- A DSC is useful for representing the top-down design of a software system, as well as the data flow and control flow between the modules  .
- A DSC consists of the following elements  :
  - Modules: Rectangular boxes that represent the functional units of the software system. Each module has a name and a number that indicates its level in the hierarchy. The top-level module is numbered 0, and the lower-level modules are numbered according to their parent module. For example, module 1.2 is a child of module 1, and a sibling of module 1.1 and 1.3.
  - Calls: Arrows that connect the modules and show the direction of control flow. A call from module A to module B means that module A invokes module B as a subroutine. A call can have a label that indicates the condition or frequency of the invocation.
  - Data couples: Lines that connect the modules and show the direction of data flow. A data couple from module A to module B means that module A passes some data to module B as a parameter or a return value. A data couple can have a label that indicates the name and type of the data.
  - Libraries: Circles that represent the external modules or libraries that are used by the software system. A library can have a name and a number that indicates its level in the hierarchy. A library can be connected to a module by a call or a data couple, depending on the nature of the interaction.
  - Fan-in and fan-out: Numbers that indicate the degree of coupling of a module. Fan-in is the number of modules that call a given module, and fan-out is the number of modules that are called by a given module. A low fan-in and fan-out means that the module is loosely coupled and has high cohesion, which is desirable for software design.
- A DSC can be drawn using different notations and conventions, such as Yourdon/Constantine, Warnier/Orr, or Nassi/Shneiderman  . However, the basic principles and elements are the same across different styles.
- A DSC can be derived from the requirements specification of the software system, using techniques such as functional decomposition, data flow analysis, or structured analysis  . Alternatively, a DSC can be reverse-engineered from the source code of the software system, using tools such as static analyzers, parsers, or diagram generators  .
- A DSC can be used for various purposes, such as  :
  - Communicating the design of the software system to the developers, testers, managers, and stakeholders.
  - Verifying the correctness, completeness, consistency, and feasibility of the design.
  - Evaluating the quality, maintainability, modularity, reusability, and testability of the design.
  - Refining, improving, or modifying the design based on feedback, changes, or new requirements.
  - Documenting the design of the software system for future reference, maintenance, or reuse.

: Structure chart - Wikipedia
: Structure charts in Software Engineering - Infinity Lectures
: Problem Solving: Structure Charts - Wikibooks
: Software Engineering | Structure Charts - GeeksforGeeks
: How to draw 5 types of architectural diagrams - Lucidchart
: How to design software architecture: Top tips and best practices - Lucidchart