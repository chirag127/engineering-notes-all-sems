 Here is the content in formal tone without emojis or external links in markdown format:

#### Execution Modes of Pig

1. Local Mode: In local mode, Pig Latin scripts are executed on the same machine where Pig is installed. No Hadoop daemons are involved. This mode is used for debugging and testing Pig Latin scripts on small data sets.
2. MapReduce Mode: In this mode, Pig Latin scripts are translated into MapReduce jobs which are executed on a Hadoop cluster. This is the primary mode of running Pig Latin scripts and is used for processing large data sets stored in HDFS.
3. Tez Mode: Tez is an alternative execution engine to MapReduce. Pig can compile Latin scripts into Tez DAGs (Directed Acyclic Graphs) instead of MapReduce jobs. Tez has the potential to execute Pig Latin scripts much faster than MapReduce as it removes some of the redundancies of MapReduce. Tez mode must be explicitly enabled in Pig's configuration to use this execution mode.
4. Spark Mode: Similar to Tez, Pig can compile Latin scripts into Spark applications for execution instead of MapReduce jobs. This has the potential for even greater performance gains than Tez mode. Like Tez, Spark mode must be explicitly enabled in Pig's configuration to use this execution mode.

The points are written in a formal tone with no emojis or external links as markdown format. Let me know if you would like me to modify or expand the answer.