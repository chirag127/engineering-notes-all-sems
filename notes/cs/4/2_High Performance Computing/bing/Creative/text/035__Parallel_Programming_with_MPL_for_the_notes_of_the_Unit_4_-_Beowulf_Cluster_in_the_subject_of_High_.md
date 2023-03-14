### Parallel Programming with MPL

MPL is a compiler for parallel programming on shared-memory multicore machines. The MPL language is essentially Standard ML (SML) with extensions for parallelism. This tutorial provides an introduction to using MPL for the Beowulf Cluster in the subject of High Performance Computing.

Some of the main topics covered in this tutorial are:

- Setup: running with docker and/or installing the compiler
- Hello World: a simple example of parallel programming with MPL
- Parallel For and ForEach: how to use the Parallel class to execute loops in parallel
- Tasks: how to create and manage asynchronous operations with the Task class
- PLINQ: how to use Parallel LINQ to perform parallel queries on collections
- Data Structures: how to use thread-safe collections, synchronization types, and lazy initialization
- Parallel Diagnostic Tools: how to use Visual Studio debugger windows and the Concurrency Visualizer to debug and optimize parallel code
- Custom Partitioners: how to configure or create partitioners to control how data is distributed among parallel workers
- Task Schedulers: how to configure or create schedulers to control how tasks are executed on threads
- Lambda Expressions: how to use anonymous functions in PLINQ and TPL

Each topic will include some code examples and exercises to help you learn and practice parallel programming with MPL. You can find all the source code in the mpl-tutorial repository on GitHub.

To get started, you need to clone the repository and run the tutorial in a Docker container using the top-level Dockerfile. Alternatively, you can install the MPL compiler on your own machine following the instructions on the mpl repository.

References:

: https://github.com/MPLLang/mpl-tutorial
: https://learn.microsoft.com/en-us/dotnet/standard/parallel-programming/
: https://github.com/MPLLang/mpl