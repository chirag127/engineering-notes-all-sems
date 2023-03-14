## Unit - 2 - Project Life Cycle and Effort Estimation

This unit covers the following topics:

- Software process and process models
- Choice of process models
- Incremental delivery
- Rapid application development
- Agile methods
- Extreme programming
- Scrum
- Managing interactive processes
- Basics of software estimation
- Effort and cost estimation techniques
- COSMIC full function points
- COCOMO II model
- Staffing pattern
- Project evaluation

The following diagram illustrates the basic architecture of a software project life cycle:

```
+----------------+    +----------------+    +----------------+    +----------------+
|                |    |                |    |                |    |                |
|  Initiation    |    |  Planning      |    |  Execution     |    |  Closure       |
|                |    |                |    |                |    |                |
+----------------+    +----------------+    +----------------+    +----------------+
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        V                    V                      V                      V
+----------------+    +----------------+    +----------------+    +----------------+
|                |    |                |    |                |    |                |
|  Feasibility   |    |  Scope         |    |  Design        |    |  Delivery      |
|  study         |    |  definition    |    |  and           |    |  and           |
|                |    |                |    |  development   |    |  evaluation    |
+----------------+    +----------------+    +----------------+    +----------------+
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        V                    V                      V                      V
+----------------+    +----------------+    +----------------+    +----------------+
|                |    |                |    |                |    |                |
|  Requirements  |    |  Schedule      |    |  Testing       |    |  Maintenance   |
|  analysis      |    |  and           |    |  and           |    |  and           |
|                |    |  budgeting     |    |  debugging     |    |  support       |
+----------------+    +----------------+    +----------------+    +----------------+
```

The following diagram illustrates the basic architecture of a software effort estimation process:

```
+----------------+    +----------------+    +----------------+    +----------------+
|                |    |                |    |                |    |                |
|  Project       |    |  Size          |    |  Effort        |    |  Cost          |
|  definition    |    |  estimation    |    |  estimation    |    |  estimation    |
|                |    |                |    |                |    |                |
+----------------+    +----------------+    +----------------+    +----------------+
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        |                    |                      |                      |
        V                    V                      V                      V
+----------------+    +----------------+    +----------------+    +----------------+
|                |    |                |    |                |    |                |
|  Project       |    |  Function      |    |  Productivity  |    |  Cost          |
|  scope         |    |  point         |    |  factor        |    |  drivers