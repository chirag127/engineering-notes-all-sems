Various size oriented measures are derived by normalizing quality and productivity measures by considering the size of the software that has been produced. Size is a direct and easily measurable attribute of software. However, size can be measured in different ways, such as lines of code, function points, object points, etc. Each of these measures has its own advantages and disadvantages, and may be suitable for different types of software projects.

The following diagram illustrates the basic architecture of a size oriented measure in software design:

```
+------------------+    +------------------+    +------------------+
| Quality Measure  |    | Productivity     |    | Size Measure     |
| (e.g. defects    |    | Measure          |    | (e.g. LOC, FP,   |
| per KLOC)        |    | (e.g. KLOC per   |    | OP)              |
|                  |    | person-month)    |    |                  |
+------------------+    +------------------+    +------------------+
          |                     |                     |
          |                     |                     |
          +---------------------+---------------------+
                                |
                                |
                                v
                    +-------------------------+
                    | Size Oriented Measure   |
                    | (e.g. defects per FP,   |
                    | KLOC per OP)            |
                    +-------------------------+
```