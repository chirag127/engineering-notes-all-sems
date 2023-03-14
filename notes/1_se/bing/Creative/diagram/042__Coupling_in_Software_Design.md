Coupling in software engineering is the degree of interdependence between software modules; a measure of how closely connected two routines or modules are; the strength of the relationships between modules. Coupling affects the quality of a software system's design, as high coupling can make a system difficult to change and test, while low coupling can make a system easier to maintain and improve.

There are different types of coupling, such as data coupling, stamp coupling, control coupling, common coupling, content coupling, and external coupling . Each type of coupling represents a different level of dependency and complexity between modules.

The following diagram illustrates the basic concept of coupling in software design using ASCII art:

```
+-----------------+    +-----------------+    +-----------------+
| Module A        |    | Module B        |    | Module C        |
|                 |    |                 |    |                 |
| +-------------+ |    | +-------------+ |    | +-------------+ |
| | Data        | |    | | Data        | |    | | Data        | |
| +-------------+ |    | +-------------+ |    | +-------------+ |
| | Function    | |    | | Function    | |    | | Function    | |
| +-------------+ |    | +-------------+ |    | +-------------+ |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       +---------------------->                      |
       |                      |                      |
       |                      +----------------------+
       |                      |                      |
       |                      |                      |
       +--------------------------------------------->

```

In this diagram, module A is data coupled with module B, as it passes only data to it. Module B is control coupled with module C, as it passes control information to it. Module A is content coupled with module C, as it directly accesses or modifies the data or function of it. Data coupling is the lowest level of coupling, while content coupling is the highest level of coupling.