#### YARN

YARN stands for Yet Another Resource Negotiator. It is a distributed resource management technology used in Hadoop. It has become the de-facto standard for resource management in Hadoop.

YARN is responsible for managing the resources in a Hadoop cluster and scheduling the jobs that run on the cluster. It provides a way to manage resources that is scalable, flexible, and efficient.

Here are some key points to remember about YARN:

- YARN was introduced in Hadoop 2.0 and is a major improvement over the previous version of Hadoop, which used the MapReduce framework for both resource management and job scheduling.
- YARN separates the resource management and job scheduling functions, which allows for more flexibility and scalability in managing resources in a cluster.
- YARN consists of a ResourceManager, which manages the resources in the cluster, and NodeManagers, which manage the resources on each node in the cluster.
- The ResourceManager is responsible for allocating resources to applications and scheduling tasks on the nodes in the cluster.
- The NodeManagers are responsible for monitoring the resources on each node and reporting back to the ResourceManager.
- YARN supports multiple application types, including MapReduce, Spark, and Tez, among others.
- YARN also supports dynamic resource allocation, which allows for more efficient use of resources in a cluster.
- YARN provides a REST API for managing and monitoring the cluster, which can be used by third-party tools for monitoring and managing the cluster.

In summary, YARN is a powerful resource management technology that is essential for running Hadoop applications. It provides a scalable, flexible, and efficient way to manage resources in a Hadoop cluster and schedule jobs that run on the cluster.