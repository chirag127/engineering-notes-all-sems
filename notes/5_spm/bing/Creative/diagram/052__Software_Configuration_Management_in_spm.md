Software configuration management (SCM) is the process of controlling and tracking changes in the software, part of the larger cross-disciplinary field of configuration management. SCM practices include revision control and the establishment of baselines.

The following diagram illustrates the basic architecture of a software configuration management system:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Configuration  |    |  Configuration  |    |  Configuration  |
|  Identification |    |  Control        |    |  Status         |
|                 |    |                 |    |  Accounting     |
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
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Configuration  |    |  Configuration  |    |  Configuration  |
|  Repository     |    |  Audit          |    |  Review         |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

The diagram shows the main components and activities of SCM:

- Configuration identification: the process of determining the scope of the software system and identifying the configuration items (CIs) that make up the system.
- Configuration control: the process of managing the changes to the CIs and ensuring that only authorized and consistent versions of the CIs are used in the system.
- Configuration status accounting: the process of recording and reporting the status and history of the CIs and the changes made to them.
- Configuration repository: the storage location where the CIs and their versions are kept and accessed.
- Configuration audit: the process of verifying that the CIs and their versions conform to the specifications and requirements of the system.
- Configuration review: the process of evaluating the quality and performance of the CIs and their versions and providing feedback and recommendations for improvement.