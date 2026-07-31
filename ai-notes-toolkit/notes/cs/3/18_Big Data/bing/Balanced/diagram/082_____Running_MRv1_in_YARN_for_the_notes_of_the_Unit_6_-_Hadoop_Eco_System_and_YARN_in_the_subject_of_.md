### Running MRv1 in YARN

- MRv1 is the original version of MapReduce that consists of interfaces and classes from the Java package org.apache.hadoop.mapred.
- YARN is the newer version of MapReduce that consists of interfaces and classes from the Java package org.apache.hadoop.mapreduce.
- YARN is also known as MRv2 or Yet Another Resource Negotiator .
- YARN separates the resource management and processing components of MapReduce, allowing multiple types of applications to run on the same cluster.
- MRv1 applications can run on YARN with minor changes in the submission and monitoring commands .
- To submit MRv1 applications on YARN, use the yarn command in the Hadoop-YARN bin folder rather than hadoop.
- For example, to run the wordcount example on YARN, use the following command:

```bash
yarn jar /usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar wordcount input output
```

- To monitor MRv1 applications on YARN, use the ResourceManager web interface that shows the basic cluster metrics, list of applications, and nodes associated with the cluster.
- The ResourceManager web interface can be accessed at http://<ResourceManager-Host>:8088/.
- YARN also supports different schedulers such as FIFO, Fair, and Capacity that allocate resources to applications based on different criteria.