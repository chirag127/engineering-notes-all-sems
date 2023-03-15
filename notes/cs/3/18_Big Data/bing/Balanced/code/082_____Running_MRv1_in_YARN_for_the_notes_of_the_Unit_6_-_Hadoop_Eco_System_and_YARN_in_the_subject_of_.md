### Running MRv1 in YARN

- MRv1 is the original version of MapReduce that consists of interfaces and classes from the Java package org.apache.hadoop.mapred.
- YARN is the newer version of MapReduce that consists of interfaces and classes from the Java package org.apache.hadoop.mapreduce.
- YARN is also known as MRv2 or Yet Another Resource Negotiator .
- YARN separates the resource management and processing components of MapReduce, allowing multiple types of applications to run on the same cluster.
- MRv1 applications can run on YARN with some minor changes in the configuration and command syntax .
- To run MRv1 applications on YARN, the following steps are required:
  - Set the mapreduce.framework.name property to yarn in the mapred-site.xml file.
  - Use the yarn command in the Hadoop-YARN bin folder rather than the hadoop command to submit applications.
  - For example, to run the wordcount example, use the following command: `yarn jar hadoop-mapreduce-examples-2.x.x.jar wordcount input output`
- To monitor MRv1 applications on YARN, the following options are available :
  - Use the ResourceManager web interface that shows the basic cluster metrics, list of applications, and nodes associated with the cluster. The default URL is http://<ResourceManager-Host>:8088.
  - Use the ApplicationMaster web interface that shows the details of a specific application, such as the job status, counters, tasks, and logs. The URL can be obtained from the ResourceManager web interface or the console output of the application.
  - Use the MapReduce JobHistory web interface that shows the history of completed jobs, such as the job configuration, summary, counters, tasks, and logs. The default URL is http://<JobHistory-Host>:19888.
  - Use the YARN or MapReduce command-line tools to get information about the cluster, applications, and jobs. For example, use the following commands: `yarn application -list`, `yarn application -status <application_id>`, `mapred job -list`, `mapred job -status <job_id>`.