 Here is the content in Markdown format for the topic ### YARN for the notes of the Unit 6 - Hadoop Eco System and YARN in the subject of Big Data:

### YARN

- YARN stands for Yet Another Resource Negotiator. It is a cluster management technology for Hadoop.
- It was introduced in Hadoop 2.0 in 2012. It replaced the JobTracker and TaskTracker of MapReduce with ResourceManager and NodeManager respectively.
- The main purpose of YARN is to turn Hadoop from a batch processing system into a distributed operating system that can handle multiple applications.
- YARN has a central ResourceManager and per-node NodeManager(s). The ResourceManager arbitrates resources in the cluster and manages contention for resources. The NodeManager(s) take care of containers, monitoring their resource usage (cpu, memory, disk, network), and reporting back to the ResourceManager.
- The key components of YARN are:
    - ResourceManager (RM): It is the master that manages resources and schedules applications. There is one RM per cluster.
    - NodeManager (NM): It is the per-node slave that manages resources and executes/monitors containers. There is one NM per node.
    - ApplicationMaster (AM): It is the per-application master that negotiates resources from the RM and coordinates task execution on the NMs. There is one AM per application.
- The basic steps in a YARN application are:
    1. Client submits an application to the RM
    2. RM requests resources from NMs to start the AM
    3. AM requests resources from RM to run tasks
    4. AM requests NMs to run tasks/containers
    5. Containers execute tasks and send progress/status updates to the AM
    6. AM sends progress/status updates to the RM
    7. Application completes/fails and RM shuts down the AM
- Advantages of YARN:
    - Scalability: It can scale to handle a huge number of applications/users.
    - Multi-tenancy: It supports running multiple applications simultaneously in a cluster.
    - Interfaces: It has well-defined interfaces that allows for different frameworks/tools to be built on top of YARN.
    - Reliability: It has features like resource preemption and application high availability that improve reliability.
- Disadvantages of YARN:
    - Complexity: YARN has a more complex architecture than the original MapReduce system which makes it harder to understand and tune.
    - Debugging: The additional complexity also makes debugging applications on YARN more difficult.
- YARN enables running a variety of distributed applications on Hadoop including batch processing with MapReduce, real-time processing with Spark, graph processing with Giraph, streaming with Storm, machine learning with MLlib etc. This makes it a powerful platform for Big Data processing.