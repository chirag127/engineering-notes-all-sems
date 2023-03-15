### Running MRv1 in YARN

- MRv1 is the original version of MapReduce that consists of interfaces and classes from the Java package org.apache.hadoop.mapred.
- YARN is the newer version of MapReduce that consists of interfaces and classes from the Java package org.apache.hadoop.mapreduce.
- YARN is also known as MRv2 or Yet Another Resource Negotiator .
- YARN separates the resource management and processing components of MapReduce, allowing multiple types of applications to run on the same cluster.
- MRv1 applications can run on YARN with some minor changes in the configuration and command syntax .
- To run MRv1 applications on YARN, the following steps are required:
  - Set the mapreduce.framework.name property to yarn in the mapred-site.xml file.
  - Use the yarn command in the Hadoop-YARN bin folder rather than the hadoop command to submit the applications.
  - For example, to run the wordcount example, use the following command: `yarn jar hadoop-mapreduce-examples-2.x.x.jar wordcount input output`
- To monitor MRv1 applications on YARN, the ResourceManager web interface can be used.
  - The ResourceManager UI shows the basic cluster metrics, list of applications, and nodes associated with the cluster.
  - The ResourceManager UI can be accessed at http://<ResourceManager-Host>:8088
  - The ApplicationMaster UI can be accessed from the ResourceManager UI by clicking on the application ID link.
  - The ApplicationMaster UI shows the details of the application, such as the job status, counters, tasks, and logs.