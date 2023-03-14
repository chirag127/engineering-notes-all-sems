## Unit 5 - Cloud Technologies And Advancements Hadoop

- Hadoop is an open-source software framework for storing and processing large-scale data sets across clusters of computers using simple programming models.  
- Hadoop was originally designed for computer clusters built from commodity hardware, which is still the common use.  It has since also found use on clusters of higher-end hardware.  
- Hadoop is designed to scale up from a single computer to thousands of clustered computers, with each machine offering local computation and storage.  
- Hadoop can efficiently store and process large datasets ranging in size from gigabytes to petabytes of data.   
- Hadoop consists of a storage part, known as Hadoop Distributed File System (HDFS), and a processing part, which is a MapReduce programming model.  
- Hadoop splits files into large blocks and distributes them across nodes in a cluster. It then transfers packaged code into nodes to process the data in parallel.  
- Hadoop takes advantage of data locality, where nodes manipulate the data they have access to. This allows the dataset to be processed faster and more efficiently than it would be in a more conventional supercomputer architecture that relies on a parallel file system where computation and data are distributed via high-speed networking.   
- Hadoop also includes other modules, such as Hadoop Common, Hadoop YARN, and Hadoop Ozone, that provide libraries, utilities, resource management, and object storage for the framework.  
- Hadoop has a rich ecosystem of additional software packages that can be installed on top of or alongside Hadoop, such as Apache Pig, Apache Hive, Apache HBase, Apache Phoenix, Apache Spark, Apache ZooKeeper, Apache Impala, Apache Flume, Apache Sqoop, Apache Oozie, and Apache Storm.   
- Hadoop is widely used by many organizations for various applications, such as data warehousing, data mining, data analysis, machine learning, web indexing, and recommendation systems.   

### Mnemonics and learning tricks for Hadoop

- To remember the main components of Hadoop, you can use the acronym **HDMY** (Hadoop Distributed File System, MapReduce, YARN, and Ozone).
- To remember the difference between Hadoop and a conventional supercomputer, you can use the phrase **Hadoop is local, supercomputer is remote**. This refers to the data locality principle of Hadoop, where data is processed by the nodes that store it, rather than being transferred over a network to a central processor.
- To remember some of the common applications of Hadoop, you can use the acronym **WARM** (Web indexing, Analysis, Recommendation, and Machine learning).