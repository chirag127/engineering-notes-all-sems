Failures in MapReduce can occur at different levels: task, tasktracker, node manager, application master, and resource manager. Each level has a different way of handling failures and recovering from them. The following diagram illustrates the basic architecture of a MapReduce job and the possible failure points:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Resource       |    |  Resource       |    |  Resource       |
|  Manager        |    |  Manager        |    |  Manager        |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
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
       |                      |                      |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Node           |    |  Node           |    |  Node           |
|  Manager        |    |  Manager        |    |  Manager        |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
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
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Application    |    |  Application    |    |  Application    |
|  Master         |    |  Master         |    |  Master         |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Tasktracker    |    |  Tasktracker    |    |  Tasktracker    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Task           |    |  Task           |    |  Task           |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

#### Failures in MapReduce

- Task failure: This can happen when the user code in the map or reduce task throws a runtime exception, or when the task JVM exits suddenly or hangs. The task JVM reports the error back to its parent application master before it exits, or the node manager notices that the process has exited or stopped sending progress updates. The application master marks the task attempt as failed, and frees up the container so its resources are available for another task. The application master will try to avoid rescheduling the task on a node manager where it has previously failed, and will also limit the number of retries for a task before aborting the job. The user can configure the maximum number of attempts and the maximum percentage of failures allowed for map and reduce tasks separately. The user can also use counters and logs to track the number and cause of task failures.    

- Tasktracker failure: This can happen when the tasktracker process crashes or the node manager loses contact with it. The node manager will report the tasktracker as unhealthy to the resource manager, and the resource manager will mark the tasktracker as lost. The resource manager will also inform