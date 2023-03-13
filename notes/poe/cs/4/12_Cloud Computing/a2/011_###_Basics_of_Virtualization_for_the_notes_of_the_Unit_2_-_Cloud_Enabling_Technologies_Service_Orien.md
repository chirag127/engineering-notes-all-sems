 Here is the content in markdown format for the topic ### Basics of Virtualization for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing:

### Basics of Virtualization

Virtualization is a technique where a software is used to simulate a physical computer system. This allows running multiple virtual machines with different operating systems on a single physical computer.

Key points about Virtualization:

- It allows abstraction of physical resources and presents a logical/virtual view of the resources to the user.
- The physical system is called host and the virtual systems are called guests. The software which creates and runs the virtual systems is called hypervisor or virtual machine monitor.
- Hypervisor allows the guest systems to access the hardware resources allocated to them and provides isolation between the guest systems.
- The key benefits of virtualization are optimum utilization of resources, reduced costs, increased scalability and flexibility, high availability, etc.
- The types of virtualization are full virtualization, para-virtualization and operating system-level virtualization. Full virtualization provides more isolation between guests but para-virtualization and OS-level virtualization have better performance due to lesser overhead.
- Uses of virtualization include server consolidation, sandboxing, operating system deployment, cloud computing, software testing, etc.

Mnemonics for key points:

- VIRTUAL: Virtual view, Isolation, Resources, Type of virtualization, Uses of virtualization
- HYPER: Hypervisor, Hardware access, Guest systems

Applications of virtualization in cloud computing:

- It enables the cloud provider to provide elastic and scalable infrastructure to the users on demand. The physical servers can be optimally utilized by hosting multiple virtual machines.
- It allows creation and deletion of virtual machines easily which enables the cloud users to scale up and down their resources flexibly.
- The isolation provided by virtualization enhances the security of applications and data of different users on the same physical infrastructure.
- The virtual machines can be migrated between physical servers to balance the load or during maintenance activities without impacting the running applications. This increases availability.

Advantages and disadvantages:

Advantages:

- Optimum utilization of resources
- Reduced costs
- Increased scalability and flexibility
- High availability

Disadvantages:

- Performance overhead due to virtualization
- Complexity in management
- vendor lock-in for proprietary virtualization technologies