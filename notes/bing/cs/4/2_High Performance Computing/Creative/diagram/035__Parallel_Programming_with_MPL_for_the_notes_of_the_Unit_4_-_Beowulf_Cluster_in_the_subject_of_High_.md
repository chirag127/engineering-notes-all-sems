### Parallel Programming with MPL

MPL is a compiler for parallel programming on shared-memory multicore machines. The MPL language is essentially Standard ML (SML) with extensions for parallelism. MPL generates executables with excellent multicore performance, utilizing a novel approach to memory management based on the theory of disentanglement .

The following diagram illustrates the basic architecture of a parallel program written in MPL:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Main thread    |    |  Worker thread  |    |  Worker thread  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  SML code       |    |  SML code       |    |  SML code       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  MPL runtime    |    |  MPL runtime    |    |  MPL runtime    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  OS thread      |    |  OS thread      |    |  OS thread      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  CPU core       |    |  CPU core       |    |  CPU core       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

The main thread is the entry point of the program and executes the SML code. The main thread can spawn worker threads using the `par` construct, which takes a list of functions and executes them in parallel. The worker threads also execute SML code and can communicate with the main thread using channels. The MPL runtime handles the memory management, synchronization, and scheduling of the threads. The OS threads are mapped to the CPU cores and run the MPL runtime and the SML code.

For more details on how to use MPL, please refer to the tutorial and the documentation.