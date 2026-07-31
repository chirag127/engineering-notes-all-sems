#### MRv2 in Hadoop ecosystem

- MRv2, also known as Hadoop 2, is a version of Hadoop where the resource management and scheduling tasks are separated from MapReduce by YARN (Yet Another Resource Negotiator). The resource management and scheduling layer lies beneath the MapReduce layer.
- MRv2 is an application framework that runs within YARN.
- In Hadoop version 1, MapReduce was responsible for both processing and cluster resource management. In Apache Hadoop version 2, cluster resource management has been moved from MapReduce into YARN, thus enabling other application engines to utilize YARN and Hadoop, while also improving the performance of MapReduce.
- Apache Hadoop MapReduce 2.x (MRv2) supports backward compatibility of org.apache.hadoop.mapred APIs. Binary compatibility here means that the compiled binaries should be able to run without any modification on the new framework.