
#### Execution Modes of Pig

Pig provides two execution modes:

1. **Local Mode**: In local mode, Pig runs in a single JVM process on the local host. This mode is suitable for small data sets and is useful for debugging purposes.

2. **MapReduce Mode**: In MapReduce mode, Pig translates the Pig Latin script into a series of MapReduce jobs and submits them to the Hadoop cluster for execution. This mode is suitable for large data sets.

Mnemonic for Pig Execution Modes:

* Local Mode: **L**et's **O**perate **C**omputer **A**t **L**ocal.
* MapReduce Mode: **M**ap **R**educe **E**xecution **M**ode.

Advantages of Pig Execution Modes:

* Local Mode:
  * It is suitable for small data sets.
  * It is useful for debugging purposes.

* MapReduce Mode:
  * It is suitable for large data sets.
  * It is faster than Local Mode, as it makes use of distributed computing.

Disadvantages of Pig Execution Modes:

* Local Mode:
  * It is not suitable for large data sets.

* MapReduce Mode:
  * It is not suitable for small data sets.
  * It is slower than Local Mode.

Examples of Pig Execution Modes:

* Local Mode:
  * Processing a small data set of student records.

* MapReduce Mode:
  * Processing a large data set of customer records.

Applications of Pig Execution Modes:

* Local Mode:
  * Debugging Pig Latin scripts.

* MapReduce Mode:
  * Processing large data sets for analytics purposes.