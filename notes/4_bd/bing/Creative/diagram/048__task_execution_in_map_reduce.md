Task execution in MapReduce is the process of running the map and reduce tasks on the input data in a distributed and parallel manner. The task execution is controlled by two types of entities: a single master called JobTracker or ResourceManager, and multiple workers called TaskTrackers or NodeManagers. The master is responsible for scheduling the tasks, monitoring them, and re-executing the failed tasks. The workers execute the tasks as directed by the master and report their progress and status.

The following diagram illustrates the basic architecture of a MapReduce task execution using ASCII characters:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Job Client    |     |   JobTracker    |     |   TaskTracker   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
| Submit job jar  |---->| Distribute jar  |---->| Execute map     |
| and config      |     | and config      |     | tasks           |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|                 |     | Schedule tasks  |---->| Report task     |
|                 |     |                 |     | progress and    |
|                 |     |                 |     | status          |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|                 |     | Monitor tasks   |<----| Execute reduce  |
|                 |     |                 |     | tasks           |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|                 |     |                 |<----| Output results  |
|                 |     |                 |     | to HDFS         |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|                 |<----| Provide status  |     |                 |
|                 |     | and diagnostic  |     |                 |
|                 |     | information     |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```