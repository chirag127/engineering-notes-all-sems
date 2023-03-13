## Part (C):

The following diagram illustrates the basic architecture of a MapReduce program using ASCII characters:

```
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|     Client       |    |    JobTracker    |    |    TaskTracker   |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
| Submit job       |    | Schedule tasks   |    | Run tasks        |
| Monitor progress |    | Monitor progress |    | Report status    |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      +----------------------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        +---------------------->                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        +---------------------->                      |
                           +------------------+
                           |                  |
                           |    HDFS         |
                           |                  |
                           +------------------+
                           |                  |
                           | Store input data |
                           | Store output data|
                           |                  |
                           +------------------+
```

The diagram shows the following components and interactions:

- The **Client** is the program that submits the MapReduce job to the cluster. It also monitors the progress of the job and retrieves the output data from the HDFS.
- The **JobTracker** is the master node that coordinates the execution of the MapReduce job. It receives the job configuration from the client, splits the input data into map tasks and reduce tasks, assigns the tasks to the available TaskTrackers, and monitors their status and progress.
- The **TaskTracker** is the worker node that runs the map and reduce tasks assigned by the JobTracker. It also reports the status and progress of the tasks to the JobTracker.
- The **HDFS** is the distributed file system that stores the input and output data of the MapReduce job. It also provides fault tolerance and high availability of the data.