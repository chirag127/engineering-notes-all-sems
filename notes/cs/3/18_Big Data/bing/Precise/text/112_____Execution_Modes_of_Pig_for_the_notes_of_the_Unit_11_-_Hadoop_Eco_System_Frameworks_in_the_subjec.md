### Execution Modes of Pig

Apache Pig can be executed in several modes, depending on where the Pig script is going to run and where the data is residing. The data can be stored on a single machine or in a distributed environment like clusters. The different modes to run Pig programs are:

1. **Interactive Mode (Grunt shell)**: In this mode, the Pig is executed in the Grunt shell. To invoke Grunt shell, run the pig command.
2. **Batch Mode (Script)**: In this mode, we can run a script file having a .pig extension. These files contain Pig Latin commands.
3. **Embedded Mode (UDF)**: In this mode, we can define our own functions.
4. **Local Mode**: It executes in a single JVM and is used for development experimenting and prototyping. Here, files are installed and run using localhost.
5. **MapReduce Mode**: This mode is used to run Pig on a Hadoop cluster.
6. **Tez Local Mode**: To run Pig in Tez local mode.

These are the different execution modes of Pig that can be used depending on the requirements of the user.