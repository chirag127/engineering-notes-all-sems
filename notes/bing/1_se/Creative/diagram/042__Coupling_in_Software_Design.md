Coupling in software engineering is the degree of interdependence between software modules; a measure of how closely connected two routines or modules are; the strength of the relationships between modules. Coupling is usually contrasted with cohesion, which is the degree of how well the elements of a module belong together. Low coupling often correlates with high cohesion, and vice versa .

There are different types of coupling, such as common coupling, content coupling, data coupling, stamp coupling, control coupling, and message coupling. Each type of coupling has a different level of dependency and complexity between modules.

#### Coupling in Software Design

The following diagram illustrates the basic concept of coupling in software design using ASCII characters. The boxes represent modules and the arrows represent dependencies. The direction of the arrow indicates which module depends on which other module. The number of arrows indicates the degree of coupling. More arrows mean higher coupling and less arrows mean lower coupling.

```
+--------+     +--------+     +--------+     +--------+
| Module |     | Module |     | Module |     | Module |
|   A    |     |   B    |     |   C    |     |   D    |
+--------+     +--------+     +--------+     +--------+
    |              |              |              |
    |              |              |              |
    |              |              |              |
    |              |              |              |
    |              |              |              |
    |              |              |              |
    |              |              |              |
    |              |              |              |
    |              |              |              |
    |              |              |              |
    |              |              |              |
    |              |              |              |
    v              v              v              v
+--------+     +--------+     +--------+     +--------+
| Module |     | Module |     | Module |     | Module |
|   E    |     |   F    |     |   G    |     |   H    |
+--------+     +--------+     +--------+     +--------+

Low coupling: Module A depends only on Module E
High coupling: Module B depends on Module E, F, G, and H
```