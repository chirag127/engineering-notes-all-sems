#### Running MRv1 in YARN

- MRv1 is the original version of MapReduce that consists of interfaces and classes from the Java package org.apache.hadoop.mapred.
- YARN is the newer version of MapReduce that consists of interfaces and classes from the Java package org.apache.hadoop.mapreduce.
- YARN is also known as MRv2 or Yet Another Resource Negotiator .
- YARN separates the resource management and processing components of MapReduce, allowing multiple types of applications to run on the same cluster.
- MRv1 applications can run on YARN with minor changes in the configuration and command syntax .
- To run MRv1 applications on YARN, the following steps are required:
  - Set the mapreduce.framework.name property to yarn in the mapred-site.xml file.
  - Use the yarn command in the Hadoop-YARN bin folder rather than the hadoop command to submit applications.
  - Use the ResourceManager web interface to monitor applications running on YARN.
- YARN supports different schedulers to allocate resources to applications, such as FIFO, Fair, and Capacity.
- YARN provides better scalability, performance, and flexibility than MRv1.