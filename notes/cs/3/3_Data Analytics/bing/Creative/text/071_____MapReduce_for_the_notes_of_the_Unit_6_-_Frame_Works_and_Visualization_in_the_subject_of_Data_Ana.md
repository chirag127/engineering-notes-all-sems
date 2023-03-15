### MapReduce

- MapReduce is a **programming model** and an **associated implementation** for processing and generating **big datasets** with a parallel, distributed algorithm on a cluster .
- MapReduce enables **massive scalability** across hundreds or thousands of servers in a Hadoop cluster. As the processing component, MapReduce is the **heart of Apache Hadoop**.
- The term "MapReduce" refers to two separate and distinct tasks that Hadoop programs perform:
  - The **map** job takes a set of data and converts it into another set of data, where individual elements are broken down into **tuples** (key/value pairs).
  - The **reduce** job takes the output from a map as input and combines those data tuples into a smaller set of tuples.
- The MapReduce framework consists of a single master **ResourceManager**, one worker **NodeManager** per cluster-node, and **MRAppMaster** per application.
- The MapReduce framework operates on **key-value pairs**, that is, the framework views the input to the job as a set of **key-value pairs** and produces a set of **key-value pairs** as the output of the job, conceivably of different types.
- The MapReduce framework relies on the **FileSystem** to provide a way to **store** the input to and the output from the job.
- The MapReduce framework provides a number of **features** such as:
  - **Automatic parallelization and distribution** of the data and computation across the cluster.
  - **Fault-tolerance** and **recovery** of failed tasks and nodes.
  - **Load balancing** and **locality optimization** of data and computation.
  - **Abstraction** and **simplicity** of the programming interface.
  - **Extensibility** and **customization** of the data types, formats, and functions.