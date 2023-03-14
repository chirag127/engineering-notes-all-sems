COCOMO II in SPM is a software cost estimation model that consists of three sub-models: Application Composition, Early Design, and Post-Architecture. Each sub-model is used at a different stage of the software development life cycle, depending on the amount of information available. The following diagram illustrates the basic architecture of COCOMO II in SPM using ASCII art:

```
+-----------------+    +-----------------+    +-----------------+
| Application     |    | Early Design    |    | Post-Architecture |
| Composition     |    |                 |    |                   |
| Model           |    | Model           |    | Model             |
+-----------------+    +-----------------+    +-----------------+
| Used for        |    | Used for        |    | Used for          |
| prototyping     |    | early design    |    | detailed design   |
| and end-user    |    | stage of the    |    | and coding        |
| programming     |    | project         |    |                   |
+-----------------+    +-----------------+    +-----------------+
| Estimates       |    | Estimates       |    | Estimates         |
| effort based on |    | effort based on |    | effort based on   |
| object points   |    | scaling drivers |    | cost drivers      |
| and reuse       |    | and function    |    | and source lines  |
|                 |    | points          |    | of code           |
+-----------------+    +-----------------+    +-----------------+
| Supports        |    | Supports        |    | Supports          |
| application     |    | application     |    | application       |
| generators and  |    | generators,     |    | generators,       |
| composition     |    | infrastructure, |    | infrastructure,   |
| aids            |    | and system      |    | and system        |
|                 |    | integration     |    | integration       |
+-----------------+    +-----------------+    +-----------------+
```