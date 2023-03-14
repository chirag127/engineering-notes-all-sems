### Hadoop

- Hadoop is an open-source software framework for storing and processing large-scale data sets across clusters of computers using simple programming models.  
- Hadoop was originally designed for computer clusters built from commodity hardware, which is still the common use.  It has since also found use on clusters of higher-end hardware.  
- Hadoop is designed to scale up from a single computer to thousands of clustered computers, with each machine offering local computation and storage.   This allows the data set to be processed faster and more efficiently than it would be in a more conventional supercomputer architecture that relies on a parallel file system where computation and data are distributed via high-speed networking. 
- Hadoop splits files into large blocks and distributes them across nodes in a cluster. It then transfers packaged code into nodes to process the data in parallel. This approach takes advantage of data locality, where nodes manipulate the data they have access to.  
- Hadoop consists of a storage part, known as Hadoop Distributed File System (HDFS), and a processing part which is a MapReduce programming model.  
- Hadoop also includes other modules, such as Hadoop Common, Hadoop YARN, and Hadoop Ozone, that provide libraries, utilities, resource management, and object storage for the framework.  
- Hadoop can also be integrated with other software packages that can be installed on top of or alongside Hadoop, such as Apache Pig, Apache Hive, Apache HBase, Apache Phoenix, Apache Spark, Apache ZooKeeper, Apache Impala, Apache Flume, Apache Sqoop, Apache Oozie, and Apache Storm. These packages provide additional features and functionalities for data analysis, querying, streaming, machine learning, and workflow management.  

#### Advantages of Hadoop

- Hadoop provides massive storage for any kind of data, whether structured, unstructured, or semi-structured.  
- Hadoop provides enormous processing power and the ability to handle virtually limitless concurrent tasks or jobs.  
- Hadoop is cost-effective, as it can run on commodity hardware and use open-source software.  
- Hadoop is fault-tolerant, as it can automatically handle failures at the application layer, and replicate data blocks across multiple nodes for redundancy.  
- Hadoop is flexible, as it can be customized and extended with various modules and packages to suit different use cases and requirements.  

#### Disadvantages of Hadoop

- Hadoop has a steep learning curve, as it requires knowledge of various components, tools, and programming models.  
- Hadoop has a high latency, as it is based on batch processing and not suitable for real-time or interactive applications.  
- Hadoop has a low security, as it does not provide encryption, authentication, or authorization by default, and relies on external mechanisms or third-party solutions.  
- Hadoop has a limited support, as it is dependent on the community and the availability of skilled developers and administrators.  

#### Examples of Hadoop Applications

- Hadoop can be used for data warehousing, where large volumes of historical data can be stored and analyzed for business intelligence and decision making.  
- Hadoop can be used for data mining, where patterns, trends, and insights can be discovered from large and complex data sets using various algorithms and techniques.  
- Hadoop can be used for data processing, where data can be transformed, filtered, aggregated, and enriched for various purposes and applications.  
- Hadoop can be used for data science, where data can be explored, visualized, and modeled using statistical and machine learning methods.  

#### Mnemonics and Learning Tricks for Hadoop

- A possible mnemonic to remember the core components of Hadoop is **HYMN**: Hadoop YARN, H