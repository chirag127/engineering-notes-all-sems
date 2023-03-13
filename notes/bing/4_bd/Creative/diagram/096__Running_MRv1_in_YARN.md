#### Running MRv1 in YARN

MRv1 is the original MapReduce framework that was part of Hadoop 1.x. It consists of a JobTracker that coordinates the execution of MapReduce jobs, and a number of TaskTrackers that run the map and reduce tasks on the cluster nodes. MRv1 can run on YARN, which is the resource management layer introduced in Hadoop 2.x. YARN provides a more flexible and scalable platform for running various types of applications, not just MapReduce.

To run MRv1 on YARN, you need to configure the following properties in the mapred-site.xml file:

- mapreduce.framework.name: This should be set to yarn to indicate that YARN is the execution framework for MapReduce jobs.
- yarn.app.mapreduce.am.staging-dir: This specifies the staging directory for the MapReduce ApplicationMaster, which is the process that manages the lifecycle of a MapReduce job on YARN. The default value is /user.
- yarn.app.mapreduce.am.env: This sets the environment variables for the MapReduce ApplicationMaster. You can use this to specify the Java options, such as heap size and garbage collection settings, for the ApplicationMaster process.
- mapreduce.map.env and mapreduce.reduce.env: These set the environment variables for the map and reduce tasks. You can use these to specify the Java options, such as heap size and garbage collection settings, for the task processes.

The following diagram illustrates the basic architecture of running MRv1 on YARN:

```
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Job Client      |    |  Resource Manager|    |  Node Manager    |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Submit job      |    |  Allocate        |    |  Launch          |
|  ----------------+--->|  resources       |    |  ApplicationMaster|
|                  |    |  for Application |    |                  |
|                  |    |  Master          |    |                  |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
                        |                  |    |                  |
                        |                  |    |  Launch          |
                        |                  |    |  containers      |
                        |                  |    |  for map/reduce  |
                        |                  |    |  tasks           |
                        |                  |    |                  |
                        +------------------+    +------------------+
                        |                  |    |                  |
                        |  Monitor         |    |  Monitor         |
                        |  ApplicationMaster|    |  containers      |
                        |                  |    |                  |
                        +------------------+    +------------------+
```

To submit a MapReduce job using MRv1 on YARN, you can use the yarn command in the Hadoop-YARN bin folder, rather than the hadoop command. For example, to run the wordcount example, you can use the following command:

`yarn jar /usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar wordcount /user/hadoop/input /user/hadoop/output`

To monitor the MapReduce job, you can use the ResourceManager web interface, which shows the basic cluster metrics, list of applications, and nodes associated with the cluster. You can also use the ApplicationMaster web interface, which shows the details of the MapReduce job, such as the job configuration, counters, map and reduce tasks, and logs. You can access these web interfaces by using the following URLs:

- ResourceManager web interface: http://<resource_manager_host>:8088
- ApplicationMaster web interface: http://<application_master_host>:<application_master_port>