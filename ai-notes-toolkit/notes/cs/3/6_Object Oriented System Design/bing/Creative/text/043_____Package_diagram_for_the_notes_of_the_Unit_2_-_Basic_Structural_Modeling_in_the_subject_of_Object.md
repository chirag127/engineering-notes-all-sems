### Package diagram

- A package diagram is a **structural diagram** that shows the **arrangement and organization** of model elements in a **large-scale project** .
- A package is a **namespace** that contains diagrams, documents, classes, components, and other elements that are related by a common purpose or theme .
- A package diagram can be used to **simplify complex class diagrams**, to **group classes into packages**, and to **show dependencies** between packages, classes, and other elements .
- A package diagram consists of the following elements:
  - **Package**: A rectangle with a small tab at the top left corner. The name of the package is written inside the tab. The contents of the package are shown inside the rectangle .
  - **Dependency**: A dashed line with an arrowhead that indicates the direction of the dependency. The arrowhead can have different symbols to represent different types of dependencies, such as import, access, merge, use, etc .
  - **Element import**: A dependency that indicates that an element from one package is used by another element in another package. The arrowhead has a small circle at the tip .
  - **Package import**: A dependency that indicates that all the elements from one package are used by another package. The arrowhead has a large circle at the tip .
  - **Package merge**: A dependency that indicates that the contents of one package are merged with another package. The arrowhead has a small triangle at the tip .
  - **Package access**: A dependency that indicates that one package can access the public elements of another package. The arrowhead has a small x at the tip .
  - **Package use**: A dependency that indicates that one package uses the functionality of another package. The arrowhead has a small dot at the tip .
- A package diagram can be drawn at different levels of abstraction, depending on the scope and purpose of the diagram. For example, a package diagram can show the **logical view** of the system, which focuses on the functionality and behavior of the system, or the **physical view** of the system, which focuses on the implementation and deployment of the system .
- A package diagram can be used to **model the structure of a system**, to **identify the modules and components** of the system, to **show the relationships and dependencies** between the modules and components, and to **organize the system into layers** of abstraction .

: https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-package-diagram/
: https://softwareengineering.stackexchange.com/questions/200379/what-is-a-package-diagram-and-what-is-a-sequence-diagram
: https://www.lucidchart.com/pages/uml-package-diagram
: https://en.wikipedia.org/wiki/Object-oriented_design