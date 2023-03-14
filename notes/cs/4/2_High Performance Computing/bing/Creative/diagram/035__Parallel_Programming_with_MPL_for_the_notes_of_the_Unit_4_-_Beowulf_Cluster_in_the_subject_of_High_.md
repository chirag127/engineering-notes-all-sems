According to the GitHub repository of MPLLang/mpl-tutorial, MPL is a compiler for parallel programming on shared-memory multicore machines. The MPL language is essentially Standard ML (SML) with extensions for parallelism. The following diagram illustrates the basic architecture of a parallel program written in MPL:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Process 1    |    |    Process 2    |    |    Process 3    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Thread 1     |    |    Thread 2     |    |    Thread 3     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Thread 4     |    |    Thread 5     |    |    Thread 6     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Thread 7     |    |    Thread 8     |    |    Thread 9     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Thread 10    |    |    Thread 11    |    |    Thread 12    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Thread 11    |    |    Thread 12    |    |    Thread 13    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Thread 12    |    |    Thread 13    |    |    Thread 14    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Thread 13    |    |    Thread 14    |    |    Thread 15    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Thread 14    |    |    Thread 15    |    |    Thread 16    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Thread 15    |    |    Thread 16    |    |    Thread 17    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Thread 16    |    |    Thread 17    |    |    Thread 18    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Thread 17    |    |    Thread 18    |    |    Thread 19    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Thread 18    |    |    Thread 19    |    |    Thread 20    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Thread 19    |    |    Thread 20    |    |    Thread 21    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Thread 20    |    |    Thread 21    |    |    Thread 22    |
|                 |    |                 |    |