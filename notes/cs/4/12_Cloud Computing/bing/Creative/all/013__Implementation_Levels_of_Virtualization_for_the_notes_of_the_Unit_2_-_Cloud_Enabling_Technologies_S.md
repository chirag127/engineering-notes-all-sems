### Implementation Levels of Virtualization for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing

Virtualization is a computer architecture technology by which multiple virtual machines (VMs) are multiplexed in the same hardware machine. The idea of VMs can be dated back to the 1960s. It aims to improve resource sharing by several users and enhance computer performance in resource utilization and application adaptability. Virtualization also enables cloud providers to serve users with their existing physical computer hardware. It allows cloud users to acquire only the computing resources they need when they need it and scale those resources cost-effectively as their workloads expand.

There are different levels of virtualization implementation in cloud computing, depending on how the hardware resources are abstracted and presented to the virtual machines. These levels are:

- Instruction Set Architecture Level (ISA)
- Hardware Abstraction Level (HAL)
- Operating System Level
- Library Support Level
- User-Application Level

The following table summarizes the main features, advantages, and disadvantages of each level of virtualization implementation.

| Level | Features | Advantages | Disadvantages |
| ----- | -------- | ---------- | ------------- |
| ISA | - Virtualization works through an ISA emulation. <br> - The virtual machine can run legacy code written for different hardware configurations. <br> - The virtual machine is hardware-agnostic. | - High compatibility and portability. <br> - No need to modify the guest OS or applications. | - Low performance due to interpretation overhead. <br> - High complexity and implementation cost. |
| HAL | - Virtualization works at the hardware level. <br> - A bare hypervisor manages the hardware resources and multiplexes them to the virtual machines. <br> - Each hardware component (e.g., processor, memory, I/O devices) can be virtualized. | - High performance and scalability. <br> - High isolation and security. <br> - Support for multiple guest OSes and applications. | - Low compatibility and portability. <br> - Need to modify the guest OS or applications to adapt to the virtual hardware. |
| OS | - Virtualization works at the operating system level. <br> - A host OS creates an abstract layer between the applications and the hardware. <br> - Multiple instances of the same or compatible OS can run on the same hardware. | - Moderate performance and scalability. <br> - Moderate isolation and security. <br> - No need to modify the applications. | - Low compatibility and portability. <br> - Need to modify the host OS to support virtualization. <br> - Limited to the same or compatible OSes. |
| Library | - Virtualization works at the library level. <br> - A library provides a common interface for the applications to access the hardware resources. <br> - Multiple applications can run on the same hardware using the same library. | - Moderate performance and scalability. <br> - Low isolation and security. <br> - No need to modify the OS or the hardware. | - Low compatibility and portability. <br> - Need to modify the applications to use the library. <br> - Limited to the same library. |
| Application | - Virtualization works at the application level. <br> - An application provides a virtual environment for other applications to run on. <br> - Multiple applications can run on the same hardware using the same application. | - Low performance and scalability. <br> - Low isolation and security. <br> - No need to modify the OS, the hardware, or the library. | - Low compatibility and portability. <br> - Need to modify the applications to run on the virtual environment. <br> - Limited to the same application. |

The following diagram illustrates the different levels of virtualization implementation in cloud computing.

```
+-----------------+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |                 |
|  Application 1  |  Application 2  |  Application 3  |  Application 4  |  Application 5  |
|                 |                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |                 |
|  Application    |  Library        |  OS 1           |  HAL            |  ISA            |
|                 |                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+-----------------+
|                 |