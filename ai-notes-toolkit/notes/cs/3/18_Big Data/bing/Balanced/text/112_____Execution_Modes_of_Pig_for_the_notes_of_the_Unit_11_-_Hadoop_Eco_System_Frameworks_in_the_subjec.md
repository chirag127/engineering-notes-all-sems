### Execution Modes of Pig

Apache Pig is a high-level platform for analyzing large data sets using a scripting language called Pig Latin. Pig can run on a single machine or on a distributed environment like Hadoop. Pig has different execution modes or run modes depending on where the Pig script is going to run and where the data is residing. The three different modes to run Pig programs are:

- **Local Mode**: In this mode, Pig runs in a single JVM and accesses the local file system. This mode is useful for development, experimenting and prototyping. To run Pig in local mode, we need to specify the `-x local` flag in the command line or set the `pig.exec.mode` property to `local` in the `pig.properties` file. For example:

  ```bash
  pig -x local
  ```

- **MapReduce Mode**: In this mode, Pig runs on a Hadoop cluster and accesses the Hadoop Distributed File System (HDFS). This mode is useful for processing large data sets in parallel. To run Pig in MapReduce mode, we need to specify the `-x mapreduce` flag in the command line or set the `pig.exec.mode` property to `mapreduce` in the `pig.properties` file. For example:

  ```bash
  pig -x mapreduce
  ```

- **Embedded Mode**: In this mode, Pig can be embedded in a Java program and can define custom functions using User Defined Functions (UDFs). This mode is useful for extending the functionality of Pig and integrating it with other applications. To run Pig in embedded mode, we need to use the `PigServer` class and the `PigRunner` class in the Java program. For example:

  ```java
  import org.apache.pig.PigServer;
  import org.apache.pig.PigRunner;
  ...
  PigServer pigServer = new PigServer("local");
  pigServer.registerScript("script.pig");
  PigRunner.run(pigServer, null);
  ```