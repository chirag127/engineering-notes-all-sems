# Job Scheduling for Map Reduce in Big Data

- Job scheduling is the process of assigning and managing the execution of tasks in a distributed system, such as a Hadoop cluster, that processes large size datasets in parallel using the Map Reduce framework.
- Map Reduce is a programming model that allows users to write applications that can process large amounts of data on multiple nodes by dividing the work into two phases: map and reduce.
- Map phase: The input data is split into fixed-size pieces called input splits, and each split is assigned to a mapper function that transforms the data into intermediate key-value pairs and writes them to a temporary storage.
- Reduce phase: The intermediate key-value pairs are shuffled and sorted by their keys, and then assigned to a reducer function that aggregates the values for each key and produces the final output.
- Job scheduling in Map Reduce involves two main challenges: resource allocation and task assignment.
- Resource allocation: The scheduler has to decide how many and which nodes to allocate for each job, considering the available resources, the job requirements, and the cluster performance.
- Task assignment: The scheduler has to decide how to assign the map and reduce tasks to the allocated nodes, considering the data locality, the load balancing, and the fault tolerance.
- Job scheduling in Map Reduce can have different objectives, such as minimizing the completion time, maximizing the throughput, ensuring the fairness, or optimizing the energy consumption .
- Job scheduling in Map Reduce can use different algorithms, such as FIFO, Fair, Capacity, Deadline, or Multi-objective, depending on the objectives and the constraints  .
- FIFO: The scheduler assigns the jobs in the order of their arrival, and gives each job the maximum number of nodes until it finishes.
- Fair: The scheduler assigns the jobs in a way that each job gets an equal share of the cluster resources over time, and adjusts the allocation dynamically based on the demand.
- Capacity: The scheduler assigns the jobs based on predefined queues that have different capacities and priorities, and allows the jobs to use the idle resources of other queues.
- Deadline: The scheduler assigns the jobs based on their deadlines and tries to minimize the number of missed deadlines by using a heuristic algorithm.
- Multi-objective: The scheduler assigns the jobs based on multiple objectives, such as completion time, throughput, and energy consumption, and uses a genetic algorithm to find the optimal solution.