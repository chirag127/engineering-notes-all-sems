A desktop grid is a type of grid computing that uses the idle CPU time of desktop computers to perform high-throughput computing tasks. A desktop grid consists of a central server that distributes work units to a large number of volunteer computers that are connected over a general-purpose network, such as the Internet. The volunteer computers execute the work units and return the results to the server. A desktop grid can provide a substantial computational resource when aggregated, and can be used to solve various scientific problems.

The following diagram illustrates the basic architecture of a desktop grid:

```
+-----------------+        +-----------------+
|                 |        |                 |
|   Work Unit     |        |   Work Unit     |
|   Generator     |        |   Validator     |
|                 |        |                 |
+-----------------+        +-----------------+
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         +------------------------+
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
+-----------------+        +-----------------+
|                 |        |                 |
|   Volunteer     |        |   Volunteer     |
|   Computer      |        |   Computer      |
|                 |        |                 |
+-----------------+        +-----------------+
```