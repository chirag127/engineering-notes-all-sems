 Here is the content in markdown format for the topic -

### Resource Management and Scheduling for the notes of the Unit 3 - Overview of Cluster Computing in the subject of High Performance Computing

- Resource Management involves allocating and scheduling available resources (CPU, memory, storage, etc.) to various applications and users in an efficient manner.
- Scheduling is the process of assigning tasks to resources based on the availability and requirements. Efficient scheduling is crucial for optimizing resource utilization and application performance in clusters.
- Some key points about resource management and scheduling in clusters:

- Multiple users and applications contend for finite resources. Effective resource allocation and scheduling is required.
- Resources are heterogeneous and applications have varied requirements. Scheduling has to account for resource capabilities and application needs.
- Resources can get fragmented. Compaction and consolidation techniques are used to reduce fragmentation and waste.
- Data locality needs to be considered while scheduling to reduce data transfer overheads. Scheduling data-intensive applications close to the data can improve performance.
- Handling failures gracefully without affecting running applications is an important goal of resource management. Fault tolerance and high availability methods are employed.
- Trade-offs exist between resource utilization, performance, and fairness. Resource management policies tackle these trade-offs.

- Some common resource management and scheduling techniques for clusters:

- First-Come-First-Served (FCFS): Simple but can lead to resource under-utilization and starvation.
- Round-Robin (RR): Prevents starvation but does not consider application resource needs.
- Weighted Round-Robin (WRR): Assigns weights to users/applications and allocates resources proportionally.
- Minimum Share Scheduling: Guarantees a minimum percentage of resources to users/applications.
- Hierarchical Scheduling: Resources are managed and scheduled at multiple levels (cluster, node, core).
- Advance Reservations: Resources can be reserved in advance to ensure availability.
- Data-aware Scheduling: Places data-intensive applications close to the data based on data locations.
- Checkpointing: Application state is saved periodically so that applications can restart from the last checkpoint in case of failures.

- Mnemonics:
First Come First Serve = FCFS
Round Robin = RR (imagine students taking turns to speak in a circle)
Weighted Round Robin = WRR (speakers get varied time slices based on weights)
Hierarchical = top-down management
Reservations = booking resources in advance
Data-aware = considering data locations
Checkpointing = saving progress intermittently