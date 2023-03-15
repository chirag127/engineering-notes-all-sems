Static testing is a software testing technique that checks the defects in software without executing the code. Static testing can be done in two ways: review and static analysis. Review is a manual process of finding and removing errors and ambiguities in the supporting documents, such as requirements, design and test cases. Static analysis is an automated process of finding and removing errors and anomalies in the code, such as syntax, logic and complexity.

### Static Testing Strategies in Software Testing

The following diagram shows the static testing strategies in software testing:

```
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
| Requirements   |    | Design         |    | Code           |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       v                     v                     v
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
| Review         |    | Review         |    | Static Analysis|
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       v                     v                     v
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
| Defects       |    | Defects        |    | Defects        |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
```