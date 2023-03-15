### Design Structure Charts

- A design structure chart (DSC) is a diagram that shows the hierarchical decomposition of a software system into its modules and their relationships  .
- A DSC is useful for representing the top-down design of a software system, as well as the data flow and control flow between the modules  .
- A DSC consists of the following elements  :
  - Modules: Rectangular boxes that represent the functional units of the software system. Each module has a name and a number that indicates its level in the hierarchy. The main module is at level 0, and the submodules are at level 1, 2, and so on.
  - Calls: Arrows that connect the modules and show the direction of the control flow. A call from module A to module B means that A invokes B as a subroutine. A call can have a label that indicates the condition or frequency of the invocation.
  - Data couples: Circles that connect the modules and show the direction of the data flow. A data couple from module A to module B means that A passes some data to B as a parameter. A data couple can have a label that indicates the name or type of the data.
  - Flags: Triangles that connect the modules and show the direction of the status information flow. A flag from module A to module B means that A sends some status information to B as a return value or an exception. A flag can have a label that indicates the name or type of the status information.
  - Libraries: Ellipses that represent external modules or libraries that are used by the software system. A library can have a name and a number that indicates its level in the hierarchy. A library can be connected to other modules by calls, data couples, or flags.
- A DSC can be drawn using different types of notations, such as Yourdon/Constantine, Ward/Mellor, or Hatley/Pirbhai  . The choice of notation depends on the preference and convention of the software engineers.
- A DSC can be used to communicate the design of a software system to the developers, testers, and stakeholders, as well as to verify the consistency, completeness, and correctness of the design  .
- A DSC can be complemented by other types of diagrams, such as data flow diagrams, entity-relationship diagrams, or state transition diagrams, to show different aspects of the software system .

: Structure chart - Wikipedia
: Structure charts in Software Engineering - Infinity Lectures
: Problem Solving: Structure Charts - Wikibooks
: Software Engineering | Structure Charts - GeeksforGeeks
: How to draw 5 types of architectural diagrams - Lucidchart
: How to design software architecture: Top tips and best practices - Lucidchart