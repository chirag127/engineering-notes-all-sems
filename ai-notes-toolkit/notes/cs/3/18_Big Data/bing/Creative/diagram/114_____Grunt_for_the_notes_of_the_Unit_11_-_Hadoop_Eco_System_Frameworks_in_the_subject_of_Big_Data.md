### Grunt

- Grunt is Pig's interactive shell that allows users to enter Pig Latin statements and commands interactively and provides a shell for users to interact with HDFS .
- Grunt can be invoked by typing the `pig` command with no script or command to run.
- Grunt supports the following types of commands:
  - Pig Latin statements: These are the statements that define the data processing logic using Pig Latin operators and functions. They must end with a semicolon (;).
  - Shell commands: These are the commands that are executed by the underlying shell (such as bash or cmd). They must be prefixed with a backslash (\).
  - Utility commands: These are the commands that provide various utilities for Pig and Hadoop, such as setting properties, listing files, killing jobs, etc. They must be prefixed with a percent sign (%).
- Grunt also supports the following features:
  - Line continuation: A statement can be continued on the next line by ending the current line with a backslash (\).
  - Comments: A comment can be added by starting a line with two dashes (--).
  - History: The history of the commands entered in Grunt can be accessed by using the up and down arrow keys.
  - Scripting: A Grunt script can be executed by using the `run` or `exec` commands. The `run` command executes the script in the current Grunt session, while the `exec` command starts a new Grunt session to execute the script.
  - Embedded execution: A Grunt script can be embedded in a Java program by using the `PigServer` class. This allows the Java program to control the execution of the script and access the results.
- Grunt can be used in two modes: local mode and Hadoop mode .
  - Local mode: In this mode, Grunt runs on a single machine and accesses the local file system. This mode is useful for testing and debugging purposes. To run Grunt in local mode, use the `-x local` option when invoking the `pig` command.
  - Hadoop mode: In this mode, Grunt runs on a cluster of machines and accesses the HDFS. This mode is useful for processing large-scale data. To run Grunt in Hadoop mode, use the `-x mapreduce` option when invoking the `pig` command. Alternatively, this option can be omitted if the `PIG_CLASSPATH` environment variable is set to include the Hadoop configuration files.
- Grunt can be configured by setting various properties for Pig and Hadoop .
  - Pig properties: These are the properties that control the behavior and performance of Pig, such as the output format, the parallelism, the memory usage, etc. They can be set by using the `set` command in Grunt, or by using the `-D` option in the `PIG_OPTS` environment variable, or by using the `-P` option and a property file when invoking the `pig` command.
  - Hadoop properties: These are the properties that control the behavior and performance of Hadoop, such as the number of reducers, the compression codec, the task profile, etc. They can be set by using the `set` command in Grunt, or by using the `-D` option in the `PIG_OPTS` environment variable, or by using the `-P` option and a property file when invoking the `pig` command, or by using the Hadoop configuration files (such as `core-site.xml` and `mapred-site.xml`).