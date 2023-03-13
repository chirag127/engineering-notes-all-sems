Software Configuration Management (SCM) is a process to systematically manage, organize, and control the changes in the documents, codes, and other entities during the Software Development Life Cycle. SCM practices include revision control, baselines, configuration audits, change management, and release management.

The following diagram illustrates the basic architecture of a SCM system using ASCII art:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Development   |      |  Repository    |      |  Production    |
|  Environment   |      |  Environment   |      |  Environment   |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
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
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  SCM Tools    |      |  SCM Tools     |      |  SCM Tools     |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
```

The development environment is where the software developers create, modify, and test the software components. The repository environment is where the software components are stored, versioned, and tracked. The production environment is where the software components are deployed, executed, and maintained. The SCM tools are the software applications that support the SCM activities in each environment.