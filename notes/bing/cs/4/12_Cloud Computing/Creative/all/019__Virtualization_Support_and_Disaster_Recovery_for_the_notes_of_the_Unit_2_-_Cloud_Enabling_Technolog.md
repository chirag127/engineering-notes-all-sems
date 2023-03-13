### Virtualization Support and Disaster Recovery for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing

- Virtualization is the process of creating a virtual version of something, such as a server, a storage device, a network, or an operating system, that can run on a physical hardware platform.
- Virtualization enables multiple virtual machines (VMs) to run on a single physical machine, sharing the resources of that machine across multiple environments.
- Virtualization in cloud computing is the use of virtualization to create and manage cloud services, such as infrastructure as a service (IaaS), platform as a service (PaaS), and software as a service (SaaS).
- Virtualization in cloud computing has many benefits, such as:
  - Reducing the cost and complexity of managing physical hardware and software.
  - Increasing the efficiency and utilization of resources by allowing dynamic allocation and scaling of VMs according to the demand.
  - Enhancing the security and isolation of data and applications by creating separate virtual environments for different users and purposes.
  - Improving the availability and reliability of services by enabling fast recovery and migration of VMs in case of failures or disasters.
  - Supporting the agility and flexibility of development and deployment of applications by enabling rapid provisioning and configuration of VMs.

- Virtualization support and disaster recovery are two important aspects of virtualization in cloud computing that ensure the continuity and resilience of cloud services in the event of disruptions or failures.
- Virtualization support refers to the tools and mechanisms that enable the creation, management, and monitoring of VMs in a virtualized environment. Some examples of virtualization support are:
  - Hypervisors: The software layer that runs on a physical machine and allows multiple VMs to run on it. Hypervisors can be classified into two types: Type 1 or bare-metal hypervisors, which run directly on the hardware, and Type 2 or hosted hypervisors, which run on top of an operating system.
  - Virtual machine monitors (VMMs): The software component that controls and manages the VMs on a hypervisor. VMMs can perform functions such as creating, deleting, starting, stopping, suspending, resuming, migrating, and cloning VMs.
  - Virtual machine managers (VMMs): The software component that provides a user interface for accessing and managing the VMs on a hypervisor. VMMs can also provide features such as performance monitoring, resource allocation, and security policies for VMs.
  - Virtualization-aware applications: The applications that can detect and adapt to the virtualized environment they are running on. Virtualization-aware applications can optimize their performance and functionality by leveraging the features and capabilities of the virtualization layer.

- Disaster recovery refers to the process of restoring the normal operation of cloud services after a disaster, such as a power outage, a network failure, a hardware malfunction, a software bug, a cyberattack, or a natural calamity. Disaster recovery involves the following steps:
  - Backup: The process of creating and storing copies of data and applications on a secondary location, such as another cloud provider, a remote data center, or an external storage device. Backup can be performed periodically or continuously, depending on the frequency and volume of data changes.
  - Recovery: The process of retrieving and restoring the data and applications from the backup location to the primary location, or to a new location, in case the primary location is unavailable or damaged. Recovery can be performed manually or automatically, depending on the level of automation and orchestration of the backup and recovery processes.
  - Failover: The process of switching the operation of cloud services from the primary location to the backup location, or to a new location, in case the primary location is unavailable or damaged. Failover can be performed manually or automatically, depending on the level of automation and orchestration of the backup and recovery processes.
  - Failback: The process of switching the operation of cloud services back to the primary location from the backup location, or from a new location, after the primary location is restored or repaired. Failback can be performed manually or automatically, depending on the level of automation and orchestration of the backup and recovery processes.

- Virtualization in disaster recovery enables more efficient and flexible backup and recovery of cloud services by leveraging the features and capabilities of the virtualization layer. Some examples of virtualization in disaster recovery are:
  - VM replication: The process of creating and maintaining identical copies of VMs on different physical machines or locations. VM replication can be performed by the hypervisor or by a third-party software. VM replication enables fast and easy recovery