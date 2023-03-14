#### Execution Modes of Pig

- Apache Pig can run in two execution modes: local mode and MapReduce mode.
- Local mode: In this mode, Pig runs on a single machine without requiring Hadoop or HDFS. It is useful for testing and prototyping. Pig uses the local file system as input and output. To run Pig in local mode, use the -x local option: `pig -x local`
- MapReduce mode: In this mode, Pig runs on a Hadoop cluster and processes data stored in HDFS. Pig translates the Pig Latin scripts into MapReduce jobs and executes them on the cluster. To run Pig in MapReduce mode, use the -x mapreduce option: `pig -x mapreduce`
- Pig also supports three execution mechanisms: interactive mode, batch mode, and embedded mode.
- Interactive mode: In this mode, Pig runs in the Grunt shell, where users can enter Pig Latin statements and commands and see the results. To invoke the Grunt shell, use the pig command without any arguments: `pig`
- Batch mode: In this mode, Pig runs a script file that contains Pig Latin statements and commands. The script file has a .pig extension and can be executed using the pig command with the file name as an argument: `pig sample_script.pig`
- Embedded mode: In this mode, Pig allows users to define their own functions in Java or other languages and use them in Pig scripts. The user-defined functions can be compiled into a JAR file and registered with Pig using the REGISTER command. The embedded mode also allows users to write Pig scripts in Java using the PigServer class.