### Draw the component diagram for the notes of the Unit 1 - Introduction of Software Engineering Lab in the subject of Software Engineering Lab

- A component diagram is a type of UML diagram that shows the structure and dependencies of software components in a system.
- A component is a modular, reusable, and replaceable part of a software system that encapsulates its behavior and data and exposes its interfaces.
- A component diagram consists of the following elements:
  - Components: represented by rectangles with two small rectangles on the left side. They have a name and optionally a stereotype, such as <<executable>> or <<library>>.
  - Interfaces: represented by circles or lollipops. They have a name and optionally a stereotype, such as <<required>> or <<provided>>.
  - Dependencies: represented by dashed arrows with an open arrowhead. They show the relationship between components or interfaces, such as <<use>>, <<call>>, or <<import>>.
  - Associations: represented by solid lines with an optional arrowhead. They show the structural connection between components or interfaces, such as aggregation, composition, or generalization.
  - Ports: represented by small squares on the border of a component. They show the point of interaction between a component and its environment, such as a socket or a plug.
  - Delegation connectors: represented by dashed lines with a closed arrowhead. They show the relationship between a port and an interface, such as <<delegate>> or <<connect>>.

- An example of a component diagram for the notes of the Unit 1 - Introduction of Software Engineering Lab is shown below:

```markdown
+---------------------+        +---------------------+
|                     |        |                     |
|  Notes Generator    |        |  Notes Viewer       |
|                     |        |                     |
|  <<executable>>     |        |  <<executable>>     |
|                     |        |                     |
+---------------------+        +---------------------+
|                     |        |                     |
|  +---------------+  |        |  +---------------+  |
|  |               |  |        |  |               |  |
|  |  Markdown     |  |        |  |  HTML         |  |
|  |  <<provided>> |  |        |  |  <<required>> |  |
|  |               |  |        |  |               |  |
|  +---------------+  |        |  +---------------+  |
|                     |        |                     |
+---------------------+        +---------------------+
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
+---------------------+        +---------------------+
|                     |        |                     |
|  Markdown Parser    |        |  HTML Renderer     |
|                     |        |                     |
|  <<library>>        |        |  <<library>>       |
|                     |        |                     |
+---------------------+        +---------------------+
|                     |        |                     |
|  +---------------+  |        |  +---------------+  |
|  |               |  |        |  |               |  |
|  |  Markdown     |  |        |  |  HTML         |  |
|  |  <<required>> |  |        |  |  <<provided>> |  |
|  |               |  |        |  |               |  |
|  +---------------+  |        |  +---------------+  |
|                     |        |                     |
+---------------------+        +---------------------+
```

- The diagram shows that the Notes Generator component provides a Markdown interface, which is used by the Markdown Parser component. The Markdown Parser component requires a Markdown interface and provides an HTML interface, which is used by the HTML Renderer component. The HTML Renderer component requires an HTML interface and provides an HTML interface, which is used by the Notes Viewer component. The Notes Viewer component requires an HTML interface and provides an HTML interface, which is used by the user. The diagram also shows the stereotypes of the components and the interfaces, and the dependencies between them.