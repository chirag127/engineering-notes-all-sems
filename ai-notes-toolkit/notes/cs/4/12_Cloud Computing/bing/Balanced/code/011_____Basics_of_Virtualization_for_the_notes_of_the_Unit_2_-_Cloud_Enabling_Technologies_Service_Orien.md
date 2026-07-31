### Basics of Virtualization

Virtualization is a process that allows for more efficient utilization of physical computer hardware by creating multiple virtual computers, called virtual machines (VMs), that run on a single physical computer or server . Virtualization uses software to create an abstraction layer over computer hardware that allows the hardware elements, such as processors, memory, storage, and network, to be divided and shared among the VMs  .

Virtualization has many benefits, such as:

- Reducing the cost and complexity of managing and maintaining physical hardware and infrastructure.
- Increasing the availability and reliability of applications and services by enabling load balancing, failover, backup, and recovery.
- Improving the performance and scalability of applications and services by allowing dynamic allocation and reallocation of resources.
- Enhancing the security and isolation of applications and services by preventing interference and attacks from other VMs or the host system.
- Enabling the portability and compatibility of applications and services by abstracting the underlying hardware and operating system.
- Supporting the development and testing of applications and services by allowing the creation and deletion of VMs on demand.
- Facilitating the migration and transition to cloud computing by allowing the deployment and management of VMs across different cloud platforms and providers.

There are different types of virtualization, such as:

- Hardware virtualization: The most common type of virtualization, where a software layer, called a hypervisor or a virtual machine monitor (VMM), is installed on top of the physical hardware and creates and manages the VMs. Each VM has its own operating system and applications, and can run different operating systems from the host system or other VMs. Examples of hypervisors are VMware ESXi, Microsoft Hyper-V, and Oracle VM VirtualBox  .
- Operating system virtualization: A type of virtualization where a single operating system kernel is shared among multiple isolated user-space instances, called containers. Each container has its own file system, processes, network, and applications, and can run different applications from the host system or other containers. Examples of container platforms are Docker, Kubernetes, and LXC .
- Application virtualization: A type of virtualization where an application is separated from the underlying operating system and hardware, and runs in a virtualized environment that provides the necessary resources and dependencies. This allows the application to run on different devices and platforms without installation or modification. Examples of application virtualization methods are local application virtualization, application streaming, and remote desktop services.