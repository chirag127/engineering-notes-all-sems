### Execution Modes of Pig

Pig is a high-level data analysis platform that allows users to write programs in a language called Pig Latin, which is then translated into MapReduce jobs that run on Hadoop. Pig has two main execution modes: local and MapReduce.

- Local mode: In this mode, Pig runs on a single machine using the local file system. This mode is useful for testing and debugging Pig scripts, as it does not require a Hadoop cluster. To run Pig in local mode, use the `-x local` option when invoking the `pig` command.
- MapReduce mode: In this mode, Pig runs on a Hadoop cluster using the Hadoop Distributed File System (HDFS). This mode is suitable for processing large-scale data sets, as it leverages the parallelism and fault-tolerance of Hadoop. To run Pig in MapReduce mode, use the `-x mapreduce` option when invoking the `pig` command, or omit the `-x` option as MapReduce is the default mode.

Pig also has three execution mechanisms: interactive, batch, and embedded.

- Interactive mode: In this mode, Pig is executed in the Grunt shell, which is a command-line interface that allows users to enter Pig Latin statements and see the results. To invoke the Grunt shell, run the `pig` command without any arguments. You can also specify the execution mode in the Grunt shell using the `exec` or `run` commands.
- Batch mode: In this mode, Pig runs a script file that contains Pig Latin commands. The script file has a `.pig` extension and can be executed using the `-f` option when invoking the `pig` command. You can also specify the execution mode in the script file using the `%declare` or `%default` directives.
- Embedded mode: In this mode, Pig can be embedded in a Java program as a library. This mode allows users to define their own functions, operators, and data types using Java. To use Pig in embedded mode, you need to include the `pig.jar` file in your Java classpath and use the `PigServer` class to interact with Pig.