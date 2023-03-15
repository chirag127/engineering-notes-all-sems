#### Coupling in Software Design

Coupling refers to the degree of interdependence between software modules. It is a measure of how closely connected two routines or modules are and the strength of the relationships between them. Low coupling is often a sign of a well-structured computer system and a good design, while high coupling is associated with complex and difficult-to-maintain systems.

Here is an ASCII diagram that illustrates the concept of coupling in software design:

```
+----------------+        +----------------+
|     Module A   |        |     Module B   |
|                |        |                |
|  +----------+  |        |  +----------+  |
|  | Routine  |  |        |  | Routine  |  |
|  |    X     |  |        |  |    Y     |  |
|  +----------+  |        |  +----------+  |
|       |        |        |       |        |
|       |        |        |       |        |
|       v        |        |       v        |
|  +----------+  |        |  +----------+  |
|  | Routine  |  |        |  | Routine  |  |
|  |    Y     |  |        |  |    X     |  |
|  +----------+  |        |  +----------+  |
|                |        |                |
+----------------+        +----------------+

```

In this diagram, Module A and Module B are two separate modules in a software system. Routine X in Module A calls Routine Y in Module B, and Routine Y in Module B calls Routine X in Module A. This represents a high degree of coupling between the two modules, as changes in one module may affect the other.
