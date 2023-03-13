Iterative Enhancement Models in SDLC are a way to create software by breaking down the build into manageable components. Each component is implemented, tested and integrated in an iterative cycle until the complete system is ready. The iterative model allows for feedback and changes in the requirements during the development process. The following diagram illustrates the basic architecture of an iterative enhancement model in SDLC  :

### Iterative Enhancement Models in SDLC
```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Requirement    |    |  Requirement    |    |  Requirement    |
|  Analysis       |    |  Analysis       |    |  Analysis       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         V                     V                     V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Design         |    |  Design         |    |  Design         |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         V                     V                     V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Implementation |    |  Implementation |    |  Implementation |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         V                     V                     V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Testing        |    |  Testing        |    |  Testing        |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         V                     V                     V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Integration    |    |  Integration    |    |  Integration    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         V                     V                     V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Evaluation     |    |  Evaluation     |    |  Evaluation     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         V                     V                     V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Feedback       |    |  Feedback       |    |  Feedback       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         +---------------------+---------------------+
                               |
                               |
                               V
                      +-----------------+
                      |                 |
                      |  Final Product  |
                      |                 |
                      +-----------------+
```