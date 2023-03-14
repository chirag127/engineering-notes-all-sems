### Iterative Enhancement Models in SDLC

The Iterative Enhancement Models in SDLC are a way to create software by breaking down the build into manageable components and enhancing them iteratively until the complete system is ready. Each iteration consists of four phases: requirements, design, implementation and testing. The following diagram illustrates the basic architecture of an Iterative Enhancement Model in SDLC:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Requirements   |---->|    Design       |---->| Implementation  |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                       |                       |
       |                       |                       |
       V                       V                       V
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Testing        |<----|  Verification   |<----|  Validation     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                       |                       |
       |                       |                       |
       +-----------------------+-----------------------+
                               |
                               |
                               V
                       +-----------------+
                       |                 |
                       |  Deployment     |
                       |                 |
                       +-----------------+
```

Each iteration produces a new version of the software that adds functionality to the previous version. The process continues until the software meets all the requirements and is ready to be deployed. The key to a successful use of an Iterative Enhancement Model is rigorous validation of requirements and verification and testing of each version of the software.