Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on the execution modes of Pig for your notes.

### Execution Modes of Pig

- Pig is a high-level language that can process large-scale data on Hadoop clusters.
- Pig can run in two execution modes: local mode and MapReduce mode.
- Local mode: Pig runs on a single machine using the local file system. This mode is useful for development, testing and debugging of Pig scripts. To run Pig in local mode, use the `-x local` flag in the command line or set the `pig.exec.mode` property to `local` in the configuration file.
- MapReduce mode: Pig runs on a Hadoop cluster using the Hadoop Distributed File System (HDFS). This mode is useful for production and processing of large-scale data. To run Pig in MapReduce mode, use the `-x mapreduce` flag in the command line or set the `pig.exec.mode` property to `mapreduce` in the configuration file.
- Pig can also run in other execution modes using different execution engines, such as Tez, Spark or Storm. These modes require additional configuration and dependencies. For more details, refer to the official documentation of Pig.

### Execution Mechanisms of Pig

- Pig can execute Pig scripts in three different ways: interactive mode, batch mode and embedded mode.
- Interactive mode: Pig can execute Pig Latin commands interactively using the Grunt shell. The Grunt shell is a command-line interface that allows the user to enter Pig Latin commands and see the results. To invoke the Grunt shell, run the `pig` command without any arguments or with the `-x` flag to specify the execution mode.
- Batch mode: Pig can execute Pig Latin commands in a batch mode by reading them from a script file. A script file is a text file that contains Pig Latin commands and comments. The script file must have a `.pig` extension. To run a script file, use the `-f` flag followed by the file name in the command line. For example, `pig -x local -f script.pig`.
- Embedded mode: Pig can execute Pig Latin commands in an embedded mode by embedding them in a Java program. This mode allows the user to define custom functions and operators in Java and use them in Pig scripts. To run Pig in embedded mode, the user must create a Java class that extends the `org.apache.pig.PigServer` class and use its methods to execute Pig scripts. For more details, refer to the official documentation of Pig.