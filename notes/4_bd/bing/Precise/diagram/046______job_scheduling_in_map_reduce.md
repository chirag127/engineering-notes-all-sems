#### Job scheduling in MapReduce

Here is an ASCII diagram that illustrates the process of job scheduling in MapReduce:

```
       +------------+
       |            |
       |   Client   |
       |            |
       +------+-----+
              |
              |
              v
       +------+-----+
       |            |
       |   JobTracker   |
       |            |
       +------+-----+
              |
              |
              v
       +------+-----+
       |            |
       |   TaskTracker   |
       |            |
       +------+-----+
              |
              |
              v
       +------+-----+
       |            |
       |   DataNode   |
       |            |
       +------+-----+
```

In this diagram, the client submits a job to the JobTracker, which is responsible for scheduling the job and assigning tasks to TaskTrackers. The TaskTrackers then execute the tasks and communicate with the DataNodes to read and write data.
