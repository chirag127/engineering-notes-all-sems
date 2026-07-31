#### Fair and Capacity in Hadoop Ecosystem

- Fair scheduling is a method used to allocate resources in Hadoop ecosystem in a fair manner.
- It allocates resources based on the priority of the job and the available resources.
- The priority of the job is determined by the user who submitted the job.
- Capacity scheduling is another method used to allocate resources in Hadoop ecosystem.
- It allocates resources based on the capacity of the cluster.
- The cluster is divided into multiple queues, and each queue is allocated a certain amount of resources.
- The resources are allocated to the jobs submitted to each queue based on the priority of the job and the available resources.
- Both fair and capacity scheduling can be used together to provide a balanced allocation of resources in a Hadoop ecosystem.
- Fair scheduling ensures that jobs with higher priority get more resources, while capacity scheduling ensures that the cluster is not overloaded.
- The fair and capacity scheduling can be configured using the configuration files in Hadoop ecosystem.
- The configuration files include fair-scheduler.xml and capacity-scheduler.xml.
- The fair-scheduler.xml file is used to configure the fair scheduling, while the capacity-scheduler.xml file is used to configure the capacity scheduling.
- The configuration files can be modified based on the requirements of the cluster and the jobs submitted to it.
- In conclusion, fair and capacity scheduling are important methods used to allocate resources in Hadoop ecosystem in a fair and balanced manner. By using both methods together, clusters can be optimized for performance and efficiency.