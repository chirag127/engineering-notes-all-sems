# Package Diagram

- A package diagram is a **structural diagram** that shows the **arrangement and organization** of model elements in a **large-scale project** .
- A package is a **namespace** that contains diagrams, documents, classes, components, and other elements that are related by a common purpose or theme .
- A package diagram can be used to **simplify complex class diagrams**, to **group classes into packages**, and to **show dependencies** between packages, classes, and other elements .
- A package diagram can also be used to **model the logical architecture** of a system, to **show the subsystems** and their interactions, and to **organize the system into layers** .
- A package diagram consists of **packages** and **dependencies**. A package is represented by a **tabbed folder** with the package name on the tab. A dependency is represented by a **dashed arrow** with an optional stereotype indicating the type of relationship .
- Some common types of dependencies are:
  - **import**: indicates that a package or an element uses the public elements of another package .
  - **access**: indicates that a package or an element accesses the protected or private elements of another package .
  - **merge**: indicates that a package or an element merges with another package or element, combining their definitions .
  - **use**: indicates that a package or an element requires another package or element for its specification or implementation .
  - **trace**: indicates that a package or an element traces to another package or element, showing the origin or the rationale of the former .
- A package diagram can also include **nested packages**, **classes**, **components**, **interfaces**, and other elements to show more details of the system structure .
- A package diagram can also show the **visibility** of the elements within a package using the following symbols:
  - **+**: public, visible to all other packages .
  - **-**: private, visible only within the package .
  - **#**: protected, visible to the package and its descendants .
  - **~**: package, visible to the package and its nested packages .

- Here is an example of a package diagram for a banking system:

![Package diagram example](https://www.visual-paradigm.com/servlet/editor-content/tutorials/what-is-package-diagram/banking-system-package-diagram.png)

: https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-package-diagram/
: https://softwareengineering.stackexchange.com/questions/200379/what-is-a-package-diagram-and-what-is-a-sequence-diagram
: https://www.lucidchart.com/pages/uml-package-diagram
: https://en.wikipedia.org/wiki/Object-oriented_design