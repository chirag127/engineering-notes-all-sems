### Execution Modes of Pig

Apache Pig is a high-level platform for analyzing large data sets using a scripting language called Pig Latin. Pig can run on a single machine or on a distributed environment like Hadoop. Pig has different execution modes depending on where the Pig script is going to run and where the data is residing. The three main execution modes of Pig are:

- **Local Mode**: In this mode, Pig runs in a single Java Virtual Machine (JVM) and accesses the local file system. This mode is useful for development, testing and prototyping. To run Pig in local mode, we need to specify the `-x local` flag in the command line or set the `pig.exec.mode` property to `local` in the configuration file. For example:

  ```bash
  pig -x local script.pig
  ```

- **MapReduce Mode**: In this mode, Pig runs on a Hadoop cluster and accesses the Hadoop Distributed File System (HDFS). This mode is suitable for processing large data sets in parallel. To run Pig in MapReduce mode, we need to specify the `-x mapreduce` flag in the command line or set the `pig.exec.mode` property to `mapreduce` in the configuration file. For example:

  ```bash
  pig -x mapreduce script.pig
  ```

- **Embedded Mode**: In this mode, Pig can be embedded in a Java application and can invoke Pig Latin commands using the PigServer class. This mode allows us to define our own functions and extend the functionality of Pig. To run Pig in embedded mode, we need to include the `pig.jar` file in the classpath and create an instance of the PigServer class. For example:

  ```java
  import org.apache.pig.PigServer;
  ...
  PigServer pigServer = new PigServer("local");
  pigServer.registerScript("script.pig");
  ...
  ```