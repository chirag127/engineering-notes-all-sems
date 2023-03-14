 Here is the content in markdown format for the topic -

### Resource sharing for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Distributed systems allow resources (hardware and software) to be shared over a network. This provides benefits such as reduced cost, increased reliability through redundancy, and increased accessibility.
- Some key characteristics of distributed systems that enable resource sharing are:
    - Access transparency: The location of a resource should be transparent to the user. The system should provide a consistent interface to access the resource regardless of its physical location.
    - Location transparency: The system should hide the physical location of resources from the user. The user should be able to access resources without knowing where they are located physically.
    - Migration transparency: Resources should be able to be moved to different locations without disrupting system operation or affecting users. The system should hide the fact that a resource has migrated to a new location.
    - Concurrency transparency: The system should hide the concurrency or parallelism in the system from the user. The user should not have to deal with coordination between multiple resources or processes.
    - Failure transparency: The system should hide failures from the user and recover from failures without disrupting the user. The user should not have to deal with failure detection, recovery, or migration.
    - Scalability: The system should continue to operate efficiently as resources are added or removed, or as load changes. Adaptation to changes should be transparent to users.
- Advantages of resource sharing:
    - Increased resource utilization: Resources can be shared, leading to higher utilization and lower cost.
    - Increased reliability: Resources can be replicated or migrated to prevent loss of access due to failures or disruptions.
    - Increased accessibility: Resources can be accessed from multiple locations, and users have access to more resources.
- Disadvantages of resource sharing:
    - Increased complexity: The system is more complex due to the need to coordinate resource sharing, deal with concurrency and failures, and provide transparency.
    - Reduced performance: There may be overhead for resource sharing, such as delay due to network latency or resource contention. Performance may depend on load and resource availability.
    - Security issues: There are risks of unauthorized access, leakage of information, and abuse of resources. Special security mechanisms may be required to prevent these issues.