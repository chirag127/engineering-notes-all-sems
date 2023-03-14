Formulating a network model in SPM is the process of representing the activities and their interrelationships as a graph. There are two common ways of doing this: activity-on-node and activity-on-link. In activity-on-node, the nodes (boxes) represent the activities and the links (arrowed lines) represent the dependencies between them. In activity-on-link, the links represent the activities and the nodes represent the events of activities starting and finishing. Here is an example of a network model for a software project using activity-on-node:

```
+------------------+      +------------------+      +------------------+
| Specify overall  |      | Specify module A |      | Specify module B |
| system           |----->|                  |----->|                  |
+------------------+      +------------------+      +------------------+
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       v                         v                         v
+------------------+      +------------------+      +------------------+
| Specify module C |      | Specify module D |      | Check            |
|                  |----->|                  |----->| specifications   |
+------------------+      +------------------+      +------------------+
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       v                         v                         v
+------------------+      +------------------+      +------------------+
| Design module A  |      | Design module B  |      | Design module C  |
|                  |----->|                  |----->|                  |
+------------------+      +------------------+      +------------------+
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       v                         v                         v
+------------------+      +------------------+      +------------------+
| Code/test module |      | Code/test module |      | Code/test module |
| A                |----->| B                |----->| C                |
+------------------+      +------------------+      +------------------+
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       v                         v                         v
+------------------+      +------------------+      +------------------+
| Code/test module |      | Integrate/test   |      | Deliver system   |
| D                |----->| system           |----->|                  |
+------------------+      +------------------+      +------------------+
```