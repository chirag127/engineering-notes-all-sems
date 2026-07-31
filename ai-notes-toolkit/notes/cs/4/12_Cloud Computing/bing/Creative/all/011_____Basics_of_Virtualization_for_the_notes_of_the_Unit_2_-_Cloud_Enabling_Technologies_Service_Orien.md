# Basics of Virtualization

Virtualization is a process that allows for more efficient utilization of physical computer hardware by creating multiple virtual environments that can run different operating systems and applications. Virtualization is the foundation of cloud computing, which enables the delivery of computing resources as a service over the internet.

There are different types of virtualization, depending on the level of abstraction and the hardware elements that are virtualized. Some of the common types of virtualization are:

- **Hardware virtualization**: This type of virtualization uses a software layer called a hypervisor to create virtual machines (VMs) that can run different operating systems and applications on the same physical machine. The hypervisor manages the allocation of hardware resources such as CPU, memory, disk, and network to the VMs. Hardware virtualization allows for the consolidation of multiple physical servers into fewer machines, reducing the cost and complexity of managing IT infrastructure.

- **Operating system virtualization**: This type of virtualization allows multiple instances of the same or different operating systems to run on the same physical machine, without the need for a hypervisor. Each instance, called a container, is isolated from the others and has its own file system, processes, and network interfaces. Operating system virtualization enables faster and more efficient deployment of applications, as containers can share the same kernel and libraries, reducing the overhead of loading and running them.

- **Application virtualization**: This type of virtualization allows applications to run on different platforms and devices, without requiring installation or configuration. Application virtualization can be achieved by different methods, such as:

  - Local application virtualization: The application runs on the endpoint device but in a runtime environment that isolates it from the underlying operating system and hardware. This allows the application to run on different devices and operating systems, without compatibility issues or conflicts with other applications.

  - Application streaming: The application lives on a server that sends small components of the software to run on the endpoint device, as needed. This reduces the bandwidth and storage requirements of the application, and allows for centralized management and updates.

  - Remote application virtualization: The application runs on a server and is accessed by the endpoint device through a remote display protocol. This allows the application to run on any device that has a network connection and a compatible client, regardless of the device's hardware or operating system.

Virtualization has many benefits for both users and providers of cloud computing services, such as:

- Improved performance and scalability: Virtualization allows for the optimal use of hardware resources, as virtual environments can be created, modified, and deleted on demand, according to the workload and user requirements. Virtualization also enables the distribution and balancing of workloads across multiple physical machines, improving the performance and availability of the services.

- Reduced cost and complexity: Virtualization reduces the need for purchasing and maintaining physical hardware, as well as the power and cooling costs associated with it. Virtualization also simplifies the management and administration of IT infrastructure, as virtual environments can be centrally monitored and controlled, and can be easily migrated, backed up, and restored.

- Enhanced security and reliability: Virtualization provides a layer of isolation and protection for the virtual environments, as they are separated from the physical hardware and from each other. Virtualization also enables the implementation of security policies and mechanisms at different levels, such as encryption, authentication, and access control. Virtualization also improves the reliability and availability of the services, as virtual environments can be easily replicated, recovered, and migrated in case of failures or disasters.