### Spark

Spark is a general term that can refer to different technologies, such as:

- Apache Spark, an open-source unified analytics engine for large-scale data processing. It supports multiple languages, such as Scala, Java, Python, R, SQL, C#, and F#. It also provides libraries for SQL analytics, streaming data, machine learning, and graph processing. Apache Spark is based on the concept of resilient distributed datasets (RDDs), which are immutable collections of data that can be processed in parallel and recovered from failures. Apache Spark can run on various platforms, such as Hadoop, Kubernetes, Mesos, or standalone clusters.   

- Spark Framework, a simple and expressive web framework for Kotlin and Java. It allows developers to create web applications with minimal boilerplate code and a domain-specific language (DSL) that is easy to read and write. Spark Framework does not impose any restrictions on how to structure the application, and supports microservices architecture. Spark Framework is not related to Apache Spark, and uses a different logo and website.  

- SPARK Framework, a guidance tool for making choices between structure and innovation in leadership. It consists of five inter-related dimensions: System mapping, Problem identification, Analytics, Research, and Knowledge translation and scale. SPARK Framework helps leaders to understand the context, identify the challenges, use evidence, and scale up the solutions. SPARK Framework is not related to Apache Spark or Spark Framework, and uses a different logo and website. 

Some mnemonics and learning tricks for Apache Spark are:

- Remember the acronym RDD for Resilient Distributed Dataset, the core abstraction of Apache Spark. RDD stands for:
  - Resilient: able to recover from failures and errors.
  - Distributed: spread across multiple nodes in a cluster.
  - Dataset: a collection of data items, such as records, tuples, or objects.

- Remember the acronym DAG for Directed Acyclic Graph, the execution model of Apache Spark. DAG stands for:
  - Directed: having a direction from the source to the destination.
  - Acyclic: having no cycles or loops in the graph.
  - Graph: a representation of the data and the operations on it.

- Remember the four types of operations that can be performed on RDDs: transformations, actions, accumulators, and broadcast variables. You can use the following sentences to memorize them:
  - Transformations change the RDD into another RDD, such as map, filter, or join. They are lazy, meaning they are not executed until an action is called.
  - Actions return a value to the driver program or write data to an external storage, such as count, collect, or save. They are eager, meaning they are executed immediately.
  - Accumulators are variables that can be added to by the workers and read by the driver, such as counters or sums. They are useful for aggregating information across the cluster.
  - Broadcast variables are read-only variables that can be cached by the workers, such as lookup tables or dictionaries. They are useful for reducing network traffic and data transfer.