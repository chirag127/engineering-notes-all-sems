Applications on Big Data using Pig

Pig is a high-level platform or tool which is used to process large datasets. It provides a high level of abstraction for processing over MapReduce. It provides a high-level scripting language, known as Pig Latin which is used to develop the data analysis codes.

Some of the applications of Pig in big data are:

- For exploring large datasets Pig Scripting is used .
- Provides supports across large data sets for Ad-hoc queries .
- In the prototyping of large data-sets processing algorithms.
- Required to process the time-sensitive data loads.
- For collecting large amounts of datasets in form of search logs and web crawls.
- Used where the analytical insights are needed using the sampling.
- Utilized by telecom organizations to de-identify the customer call data information.
- Handles a wide range of data, both unstructured as well as structured.
- Provides the ability to create user-defined functions in other programming languages like Java and embed or invoke them in Pig Scripts.

The following diagram illustrates the basic architecture of a Pig application:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Pig Script   |       |    Pig Latin    |       |    MapReduce    |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Pig Scripting  |       |  Pig Execution  |       |  Hadoop Cluster |
|    Language     |       |    Engine       |       |                 |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Pig Latin    |       |    MapReduce    |       |    HDFS         |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```

The Pig Scripting Language is used to write the Pig Script, which is a sequence of data transformations and operations. The Pig Script is then compiled into Pig Latin, which is an intermediate representation of the script. The Pig Execution Engine then converts the Pig Latin into MapReduce jobs, which are executed on the Hadoop Cluster. The Hadoop Cluster consists of the HDFS, which is the distributed file system that stores the data, and the MapReduce framework, which is the parallel processing engine that performs the data analysis. The output of the MapReduce jobs is then stored back in the HDFS or returned to the user.