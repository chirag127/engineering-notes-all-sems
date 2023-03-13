Virtualization is a process that allows for more efficient utilization of physical computer hardware by dividing it into multiple virtual computers, called virtual machines (VMs). Virtualization is the foundation of cloud computing, which enables the delivery of computing services over the internet.

The following ASCII diagram illustrates the basic architecture of virtualization:

+------------------------+
|       Hypervisor       |
+------------------------+
|   +----------------+   |
|   |     VM 1       |   |
|   | +------------+ |   |
|   | | Application | |   |
|   | +------------+ |   |
|   | +------------+ |   |
|   | |   OS 1     | |   |
|   | +------------+ |   |
|   +----------------+   |
|   +----------------+   |
|   |     VM 2       |   |
|   | +------------+ |   |
|   | | Application | |   |
|   | +------------+ |   |
|   | +------------+ |   |
|   | |   OS 2     | |   |
|   | +------------+ |   |
|   +----------------+   |
|   +----------------+   |
|   |     VM 3       |   |
|   | +------------+ |   |
|   | | Application | |   |
|   | +------------+ |   |
|   | +------------+ |   |
|   | |   OS 3     | |   |
|   | +------------+ |   |
|   +----------------+   |
+------------------------+
|    Physical Hardware   |
+------------------------+

The hypervisor is a software layer that creates and manages the VMs. It allocates the hardware resources, such as CPU, memory, disk, and network, to the VMs. The VMs run their own operating systems and applications, isolated from each other. The physical hardware is the actual machine that hosts the hypervisor and the VMs.