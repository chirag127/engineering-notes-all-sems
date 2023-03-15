
### Execution Modes of Pig

Pig is a high-level scripting language that is used with Apache Hadoop. It has two execution modes: local mode and MapReduce mode.

##### Local Mode

In local mode, Pig runs in a single JVM process on the local machine. It does not use the Hadoop Distributed File System (HDFS) or the MapReduce framework. This mode is mainly used for testing and debugging.

##### MapReduce Mode

In MapReduce mode, Pig scripts are compiled into MapReduce jobs and executed on a Hadoop cluster. This mode is used for production-level processing.

#### Mnemonics and Learning Tricks

* **L**ocal mode is used for **L**ocal testing and debugging
* **M**apReduce mode is used for **M**assive, production-level processing
* Think of **L**ocal mode as the **L**ightweight version and **M**apReduce mode as the **M**assive version