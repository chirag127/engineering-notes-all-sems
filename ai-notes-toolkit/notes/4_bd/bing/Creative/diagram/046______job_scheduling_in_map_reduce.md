Hello, I am Sydney, your AI assistant. I can help you with drawing a detailed ASCII diagram for job scheduling in map reduce. Here is the diagram I have drawn based on the information I found on the web:

#### Job scheduling in map reduce

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    User Job     |       |    Job Queue    |       |    Master Node  |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                       |    |    |                 |
       |                       |    |    |                 |
       |                       |    |    |                 |
       |                       |    |    |                 |
       |                       |    |    |                 |
       |                       |    |    |                 |
       |                       |    |    |                 |
       |                       |    |    |                 |
       |                       |    |    |                 |
       |                       |    |    |                 |
       |                       |    |    +-----------------+-----------------+
       |                       |    |                      |                 |
       |                       |    |                      |    Worker Node  |
       |                       |    |                      |                 |
       |                       |    |                      +-----------------+
       |                       |    |                      |                 |
       |                       |    |                      |    Map Task     |
       |                       |    |                      |                 |
       |                       |    |                      +-----------------+
       |                       |    |                      |                 |
       |                       |    |                      |    Reduce Task  |
       |                       |    |                      |                 |
       |                       |    |                      +-----------------+
       |                       |    |                      |                 |
       |                       |    |                      |    Output       |
       |                       |    |                      |                 |
       |                       |    |                      +-----------------+
       |                       |    +-----------------+-----------------+
       |                       |                       |                 |
       |                       |                       |    Worker Node  |
       |                       |                       |                 |
       |                       |                       +-----------------+
       |                       |                       |                 |
       |                       |                       |    Map Task     |
       |                       |                       |                 |
       |                       |                       +-----------------+
       |                       |                       |                 |
       |                       |                       |    Reduce Task  |
       |                       |                       |                 |
       |                       |                       +-----------------+
       |                       |                       |                 |
       |                       |                       |    Output       |
       |                       |                       |                 |
       |                       |                       +-----------------+
       |                       +-----------------+-----------------+
       |                                            |                 |
       |                                            |    Worker Node  |
       |                                            |                 |
       |                                            +-----------------+
       |                                            |                 |
       |                                            |    Map Task     |
       |                                            |                 |
       |                                            +-----------------+
       |                                            |                 |
       |                                            |    Reduce Task  |
       |                                            |                 |
       |                                            +-----------------+
       |                                            |                 |
       |                                            |    Output       |
       |                                            |                 |
       |                                            +-----------------+
       |                       +-----------------+-----------------+
       |                       |                 |                 |
       |                       |    Final Job    |    User Job     |
       |                       |    Output       |    Output       |
       |                       |                 |                 |
       +---------------------->+-----------------+-----------------+
```

The diagram shows the following steps:

- The user submits a job to the job queue, which is a FIFO queue that stores the pending jobs.
- The master node assigns map tasks and reduce tasks to different worker nodes based on the data splits and the availability of the nodes.
- The map tasks read the data splits and run the map function on the data, producing intermediate key-value pairs.
- The reduce tasks receive the intermediate key-value pairs from the map tasks, sort them by key, and run the reduce function on the values, producing the final output.
- The final output is stored in the file system and returned to the user.
