#### MRv2 in Hadoop ecosystem

- MRv2, also known as Hadoop 2, is a version of Hadoop where the resource management and scheduling tasks are separated from MapReduce by YARN (Yet Another Resource Negotiator) .
- In Hadoop 2, the resource management and scheduling layer lies beneath the MapReduce layer .
- MRv2 is an application framework that runs within YARN .
- In Hadoop 1, all DataNodes are dedicated to Map and Reduce tasks and cannot be used for other processing .
- In Hadoop 1, the cluster’s capacity is measured in MapReduce slots .
- In Hadoop version 1, MapReduce was responsible for both processing and cluster resource management .
- In Apache Hadoop version 2, cluster resource management has been moved from MapReduce into YARN, thus enabling other application engines to utilize YARN and Hadoop, while also improving the performance of MapReduce .
- Hadoop 2 has undergone a complete change in terms of architecture and components compared to Hadoop 1 .