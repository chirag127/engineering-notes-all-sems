Unit tests with MR unit are a way of testing Hadoop MapReduce jobs using a Java library called MRUnit. MRUnit allows you to create test input and output for your mapper and reducer classes, and verify that they work as expected. You can also test the whole MapReduce workflow using a MapReduceDriver or a PipelineMapReduceDriver.

#### Unit tests with MR unit

The following diagram illustrates the basic architecture of a unit test with MR unit using ASCII art:

```
+----------------+    +----------------+    +----------------+
| Test input     |    | Mapper         |    | Test output    |
| (key, value)   | -> | (key, value)   | -> | (key, value)   |
| pairs          |    | class          |    | pairs          |
+----------------+    +----------------+    +----------------+

+----------------+    +----------------+    +----------------+
| Test input     |    | Reducer        |    | Test output    |
| (key, list     | -> | (key, list     | -> | (key, value)   |
| of values)     |    | of values)     |    | pairs          |
| pairs          |    | class          |    |                |
+----------------+    +----------------+    +----------------+

+----------------+    +----------------+    +----------------+    +----------------+    +----------------+
| Test input     |    | Mapper         |    | Reducer        |    | Mapper         |    | Test output    |
| (key, value)   | -> | (key, value)   | -> | (key, list     | -> | (key, value)   | -> | (key, value)   |
| pairs          |    | class          |    | of values)     |    | class          |    | pairs          |
+----------------+    +----------------+    +----------------+    +----------------+    +----------------+
                                   |         |                                   |         |
                                   |         |                                   |         |
                                   |         |                                   |         |
                                   v         v                                   v         v
                            +----------------+                            +----------------+
                            | Combiner       |                            | Reducer        |
                            | (key, list     |                            | (key, list     |
                            | of values)     |                            | of values)     |
                            | class          |                            | class          |
                            +----------------+                            +----------------+
```