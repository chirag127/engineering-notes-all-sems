#### Running MRv1 in YARN

- MRv1 is the original version of MapReduce that consists of interfaces and classes from the Java package org.apache.hadoop.mapred.
- YARN is the newer version of MapReduce that consists of interfaces and classes from the Java package org.apache.hadoop.mapreduce. YARN is also known as MRv2 or Yet Another Resource Negotiator.
- YARN separates the resource management and processing components of MapReduce, allowing multiple types of applications to run on the same cluster.
- MRv1 applications can run on YARN with minimal changes, as YARN provides backward compatibility for MRv1 applications .
- To run MRv1 applications on YARN, the following steps are required:
  - Set the mapreduce.framework.name property to yarn in the mapred-site.xml file.
  - Use the yarn command in the Hadoop-YARN bin folder rather than the hadoop command to submit the applications.
  - Use the ResourceManager web interface to monitor the applications running on the YARN cluster. The ResourceManager UI shows the basic cluster metrics, list of applications, and nodes associated with the cluster.
- The advantages of running MRv1 applications on YARN are :
  - Improved resource utilization and scalability, as YARN can dynamically allocate resources to applications based on demand and availability.
  - Enhanced fault tolerance and reliability, as YARN can recover from application and node failures without affecting the entire cluster.
  - Increased flexibility and extensibility, as YARN can support multiple types of applications and frameworks besides MapReduce, such as Spark, Hive, Pig, etc.