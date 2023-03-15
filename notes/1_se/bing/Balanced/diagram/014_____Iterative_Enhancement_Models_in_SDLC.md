The Iterative Enhancement Model is a type of Incremental Model in Software Engineering, where each increment is treated as a sub-project and goes through all phases of the SDLC . The model starts with a simple implementation of a small set of the software requirements and iteratively enhances the evolving versions until the complete system is implemented and ready to be deployed .

### Iterative Enhancement Models in SDLC

The following diagram shows the basic structure of the Iterative Enhancement Model in SDLC:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Initial        |    |  Increment 1    |    |  Increment 2    |
|  Requirements   |    |  Requirements   |    |  Requirements   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         V                     V                     V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Initial        |    |  Increment 1    |    |  Increment 2    |
|  Design         |    |  Design         |    |  Design         |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         V                     V                     V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Initial        |    |  Increment 1    |    |  Increment 2    |
|  Implementation |    |  Implementation |    |  Implementation |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         V                     V                     V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Initial        |    |  Increment 1    |    |  Increment 2    |
|  Testing        |    |  Testing        |    |  Testing        |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         V                     V                     V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Initial        |    |  Increment 1    |    |  Increment 2    |
|  Deployment     |    |  Deployment     |    |  Deployment     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         V                     V                     V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Initial        |    |  Increment 1    |    |  Increment 2    |
|  Evaluation     |    |  Evaluation     |    |  Evaluation     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         V                     V                     V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Initial        |    |  Increment 1    |    |  Increment 2    |
|  Feedback       |    |  Feedback       |    |  Feedback       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         V                     V                     V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Final          |    |  Final          |    |  Final          |
|  System         |    |  System         |    |  System         |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

Each arrow