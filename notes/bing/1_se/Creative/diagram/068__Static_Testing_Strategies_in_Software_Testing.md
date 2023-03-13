Static testing is a software testing technique that checks the defects in software without executing the code. It can be done in two ways: review and static analysis. Review is a manual process of finding and removing errors and ambiguities in the supporting documents, such as requirements, design and test cases. Static analysis is an automated process of finding and removing errors and anomalies in the code, such as syntax, logic and complexity.

### Static Testing Strategies in Software Testing

The following diagram illustrates the basic architecture of a static testing process:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Requirements   |----->|     Design      |----->|      Code       |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
       | ^                     | ^                     | ^
       | |                     | |                     | |
       v |                     v |                     v |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
| Requirements    |      | Design          |      | Code            |
| Review          |      | Review          |      | Review          |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
       | ^                     | ^                     | ^
       | |                     | |                     | |
       v |                     v |                     v |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
| Requirements    |      | Design          |      | Code            |
| Static Analysis |      | Static Analysis |      | Static Analysis |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

The diagram shows that static testing can be applied at different stages of the software development life cycle, from requirements to code. The output of each stage is the input of the next stage, and the feedback of each stage is the input of the previous stage. The goal of static testing is to ensure the quality and consistency of the software artifacts and to detect and correct the defects as early as possible.