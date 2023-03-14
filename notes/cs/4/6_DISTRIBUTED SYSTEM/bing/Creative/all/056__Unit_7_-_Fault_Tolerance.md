## Unit 7 - Fault Tolerance

- Fault tolerance is the property that enables a system to continue operating properly in the event of the failure of one or more faults within some of its components.
- Fault tolerance can be achieved by using backup components that automatically take the place of failed components, ensuring no loss of service. These include:
  - Hardware systems that are backed up by identical or equivalent systems. For example, a server can be made fault tolerant by using an identical server running in parallel, with all operations mirrored to the backup server.
  - Software systems that are backed up by other software instances. For example, a database with customer information can be continuously replicated to another machine. If the primary database goes down, operations can be automatically redirected to the second database.
  - Power sources that are made fault tolerant using alternative sources. For example, many organizations have power generators that can take over in case main line electricity fails.
- Fault tolerance can play a role in a disaster recovery strategy. For example, fault-tolerant systems with backup components in the cloud can restore mission-critical systems quickly, even if a natural or human-induced disaster destroys on-premise IT infrastructure.
- Fault tolerance is different from high availability, which refers to a system’s ability to avoid loss of service by minimizing downtime. High availability is expressed in terms of a system’s uptime, as a percentage of total running time. Fault tolerance is more concerned with maintaining functionality in the face of failures, regardless of the downtime.
- Some important considerations when creating fault tolerant and high availability systems in an organizational setting include:
  - The cost of redundancy and backup components, which may increase the complexity and maintenance of the system.
  - The performance and scalability of the system, which may be affected by the overhead of replication and synchronization of data and operations.
  - The reliability and availability of the system, which may depend on the type and frequency of failures, the recovery time and the recovery point objectives, and the testing and monitoring of the system.
  - The security and compliance of the system, which may require encryption, authentication, authorization, auditing, and backup of sensitive data and operations.

- A mnemonic to remember the difference between fault tolerance and high availability is: **Fault Tolerance = Functionality, High Availability = Uptime**.