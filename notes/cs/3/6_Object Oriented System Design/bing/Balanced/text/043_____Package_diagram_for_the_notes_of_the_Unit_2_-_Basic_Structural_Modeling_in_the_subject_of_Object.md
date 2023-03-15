### Package diagram for the notes of the Unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design

- A package diagram is a type of structural diagram in UML that shows the organization and arrangement of various model elements in the form of packages .
- A package is a grouping of related UML elements, such as diagrams, documents, classes, or even other packages  .
- The main goal of package diagrams is to simplify the complex class diagrams that can be used to group classes into packages. These groups help define the hierarchy and dependencies among the packages .
- A package diagram can also show the layered architecture of a software system, where each package represents a different layer or module .
- The basic notation for a package diagram is a rectangle with a tab at the top, where the name of the package is written . The contents of the package can be shown inside the rectangle, or the rectangle can be empty and the contents can be shown in another diagram .
- The dependencies between the packages can be shown using dashed arrows with different stereotypes, such as <<import>>, <<merge>>, <<access>>, <<use>>, <<include>>, or <<extend>>  . These stereotypes indicate the nature and direction of the dependency  .
- An example of a package diagram for a banking system is shown below:

![Package diagram for a banking system](https://www.lucidchart.com/publicSegments/view/9f9c0c9f-5a5f-4a2a-8a0c-9a0a0a0a0a0a/image.png)