# Execution Modes of Pig

Pig is a high-level data analysis platform that allows users to write programs in a language called Pig Latin, which is then translated into MapReduce jobs that run on Hadoop. Pig has two main execution modes: local and MapReduce.

- Local mode: In this mode, Pig runs on a single machine using the local file system. This mode is useful for testing and debugging Pig scripts, as it does not require a Hadoop cluster. To run Pig in local mode, use the `-x local` option when invoking the `pig` command.
- MapReduce mode: In this mode, Pig runs on a Hadoop cluster using the Hadoop Distributed File System (HDFS). This mode is suitable for processing large-scale data sets, as it leverages the parallelism and fault-tolerance of Hadoop. To run Pig in MapReduce mode, use the `-x mapreduce` option when invoking the `pig` command, or omit the `-x` option as MapReduce is the default mode.

Pig also supports three execution mechanisms: interactive, batch, and embedded.

- Interactive mode: In this mode, Pig is executed in the Grunt shell, which is a command-line interface that allows users to enter Pig Latin statements and see the results. The Grunt shell can be invoked by running the `pig` command without any arguments. This mode is useful for ad-hoc data exploration and syntax checking.
- Batch mode: In this mode, Pig is executed from a script file that contains Pig Latin commands. The script file must have a `.pig` extension and can be passed as an argument to the `pig` command. This mode is useful for running predefined and reusable Pig scripts.
- Embedded mode: In this mode, Pig is executed from a Java program that embeds Pig Latin commands using the PigServer class. This mode allows users to define their own functions and operators in Java and use them in Pig scripts. This mode also enables integration with other Java applications and frameworks.