## Unit 2 - Hadoop and Map Reduce

Hadoop and Map Reduce are two components of the Hadoop framework that allow processing large amounts of data in parallel on a cluster of commodity hardware. Map Reduce is a programming model that consists of two phases: map and reduce. The map phase takes the input data and transforms it into intermediate key-value pairs. The reduce phase takes the intermediate key-value pairs and aggregates them to produce the final output. The Hadoop framework takes care of distributing the data and the tasks across the cluster, as well as handling failures and optimizations.

The following diagram illustrates the basic architecture of a Map Reduce job:

```
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|     Client     |       |     Master     |       |     Worker     |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|   Submit job   |       |  Split job     |       |  Run map task  |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|                |       |  Assign tasks  |       |  Run reduce    |
|                |       |                |       |  task          |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|                |       |  Monitor tasks |       |  Report status |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|                |       |  Return output |       |                |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
```

The client is the one who submits the job to the master, which is responsible for splitting the job into smaller tasks and assigning them to the workers. The workers are the nodes that run the map and reduce tasks on the data. The master also monitors the tasks and handles failures and optimizations. The output of the job is returned to the client by the master.