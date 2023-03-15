Various size oriented measures are derived by normalizing quality and productivity measures by considering the size of the software that has been produced. Size is usually measured in lines of code (LOC) or function points (FP). Some examples of size oriented measures are:

- Errors per KLOC (thousand lines of code)
- Defects per FP (function point)
- Cost per LOC or FP
- Effort per LOC or FP
- Duration per LOC or FP

A possible ASCII diagram for various size oriented measures in software design is:

```
+---------------------+      +---------------------+
| Quality Measures    |      | Productivity        |
|                     |      | Measures            |
| - Errors per KLOC   |      | - Cost per LOC or FP|
| - Defects per FP    |      | - Effort per LOC or |
|                     |      |   FP                |
+---------------------+      | - Duration per LOC  |
                            |   or FP             |
                            +---------------------+
                                   |
                                   |
                                   v
                            +---------------------+
                            | Size Measures       |
                            |                     |
                            | - LOC               |
                            | - FP                |
                            +---------------------+
```