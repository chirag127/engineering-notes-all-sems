### Spark’s Own Cluster Manager

- Spark’s own cluster manager is also known as **standalone mode** .
- It is a simple cluster manager that is included with Spark and can run on Linux, Windows, or Mac OSX .
- It is often the simplest way to run Spark applications in a clustered environment.
- It allows Spark to manage its own cluster and allocate resources across applications.
- It supports both static and dynamic resource allocation.
- It does not provide any security or high availability features.
- It requires a master node and one or more worker nodes to form a cluster .
- The master node runs a **master daemon** that coordinates the worker nodes and assigns tasks to them .
- The worker nodes run **worker daemons** that execute the tasks assigned by the master node and report their status .
- The driver program (the main program that creates the SparkContext) can run either on the master node or on any other node that can communicate with the master node .
- The driver program can connect to the master node using a URL of the form `spark://host:port`.
- The master node can also run a web UI that shows the status of the cluster and the applications running on it .
- The standalone mode is suitable for testing and prototyping Spark applications, but it may not be the best choice for production environments that require more advanced features such as security, high availability, or resource isolation .