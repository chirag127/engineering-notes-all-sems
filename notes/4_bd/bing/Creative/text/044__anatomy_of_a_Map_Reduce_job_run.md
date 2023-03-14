#### Anatomy of a Map Reduce job run

- A Map Reduce job is a program that processes a large amount of data in parallel on a cluster of machines using the Map Reduce framework.
- A Map Reduce job consists of two phases: the map phase and the reduce phase.
- The map phase takes an input dataset and splits it into smaller chunks called input splits. Each input split is assigned to a map task, which runs on a node in the cluster and applies a user-defined map function to each record in the input split. The map function transforms the input records into intermediate key-value pairs and writes them to a local disk.
- The reduce phase takes the intermediate key-value pairs from the map phase and groups them by key. Each group of values with the same key is assigned to a reduce task, which runs on a node in the cluster and applies a user-defined reduce function to the values. The reduce function aggregates the values and produces the final output records, which are written to a distributed file system (such as HDFS).
- The Map Reduce framework handles the coordination, scheduling, distribution, fault tolerance, and monitoring of the map and reduce tasks on the cluster.
- The Map Reduce framework consists of several components, such as:

  - Client: The program that submits the Map Reduce job to the cluster.
  - Yarn resource manager: The master node that manages the allocation and coordination of computing resources on the cluster.
  - Yarn node manager: The worker node that monitors and launches the compute containers on machines.
  - Map Reduce application master: The process that facilitates the execution of the Map Reduce job on the cluster.
  - Distributed file system: The system that shares the job files and the output files with other entities on the cluster.

- The following diagram illustrates the anatomy of a Map Reduce job run:

![Anatomy of a Map Reduce job run](https://www.edureka.co/blog/wp-content/uploads/2014/03/MapReduce-Job-Execution-Flow.png)

- The following steps describe the anatomy of a Map Reduce job run in detail:

  - The client submits the Map Reduce job to the resource manager by calling the submit() method on a Job object. The client also specifies the input and output locations, the map and reduce functions, the number of map and reduce tasks, and other configuration parameters.
  - The resource manager assigns an application ID to the job and launches an application master for the job on a node manager.
  - The application master requests the resource manager for containers to run the map and reduce tasks. A container is a unit of computation that has a fixed amount of memory and CPU resources.
  - The resource manager allocates containers to the application master based on the availability of resources on the cluster.
  - The application master contacts the node managers that have the containers and instructs them to launch the map and reduce tasks.
  - The node managers launch the map and reduce tasks in the containers and report their status and progress to the application master.
  - The map tasks read the input splits from the distributed file system and apply the map function to each record. The map tasks partition the intermediate key-value pairs by a hash function and write them to a local disk.
  - The reduce tasks request the application master for the locations of the intermediate key-value pairs for their assigned keys. The application master uses the partition information from the map tasks to determine the locations.
  - The reduce tasks fetch the intermediate key-value pairs from the local disks of the map tasks and sort them by key. The reduce tasks apply the reduce function to each group of values with the same key and write the output records to the distributed file system.
  - The application master monitors the status and progress of the map and reduce tasks and handles any failures or stragglers. If a map or reduce task fails, the application master requests the resource manager for a new container and re-launches the task. If a map or reduce task is slow, the application master may launch a speculative task on another node manager to speed up the job execution.
  - The application master notifies the resource manager and the client when the job is completed. The client can then access the output files from the distributed file system.