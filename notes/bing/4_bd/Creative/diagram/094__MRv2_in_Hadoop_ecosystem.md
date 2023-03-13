MRv2 is an application framework that runs within YARN, which is a resource management layer in Hadoop 2. MRv2 separates the resource management and scheduling tasks from the MapReduce logic, allowing other applications to run on YARN as well. The following is a detailed ASCII diagram for MRv2 in Hadoop ecosystem:

```
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Client Machine  |    |  Resource Manager|    |  Node Manager 1  |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Submit Job      |    |  Allocate        |    |  Launch          |
|  Request         |    |  Resources       |    |  Containers      |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Get Application |    |  Application     |    |  Application     |
|  Master Address  |    |  Master          |    |  Master          |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Communicate     |    |                  |    |  Communicate     |
|  with            |    |                  |    |  with            |
|  Application     |    |                  |    |  Application     |
|  Master          |    |                  |    |  Master          |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Get Job Status  |    |                  |    |  Run MapReduce   |
|  and Report      |    |                  |    |  Tasks           |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Get Job Output  |    |                  |    |  Send Heartbeats |
|                  |    |                  |    |  and Status      |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|                  |    |                  |    |  Node Manager 2  |
|                  |    |                  |    |                  |
|                  |    |                  |    +------------------+
|                  |    |                  |    |                  |
|                  |    |                  |    |  Launch          |
|                  |    |                  |    |  Containers      |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|                  |    |                  |    |  Application     |
|                  |    |                  |    |  Master          |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|                  |    |                  |    |  Communicate     |
|                  |    |                  |    |  with            |
|                  |    |                  |    |  Application     |
|                  |    |                  |    |  Master          |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|                  |    |                  |    |  Run MapReduce   |
|                  |    |                  |    |  Tasks           |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|                  |    |                  |    |  Send Heartbeats |
|                  |    |                  |    |  and Status      |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
```