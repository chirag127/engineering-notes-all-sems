 Here are the notes for the topic -

Virtualization Support and Disaster Recovery

### What is Virtualization?
- Virtualization is a technology that creates virtual versions of physical resources.
- In virtualization, a software layer is created between the hardware and the operating system that enables running multiple virtual machines with different operating systems on the same physical machine.
- Each virtual machine has its own set of virtual hardware like CPU, memory, storage, and network interfaces. The software layer allocates physical resources dynamically to the virtual machines.
- Key benefits of virtualization are optimum utilization of resources, cost efficiency, agility, and easy scalability.

### Types of Virtualization
- Full Virtualization - A complete simulated hardware is created for the guest OS. Examples are VMware ESXi and VirtualBox.
- Para-virtualization - The guest OS is modified to use a special API to access the virtual hardware. Example is Xen.
- Operating System-level Virtualization - The resources of a single OS kernel are virtualized to run multiple isolated user space instances. Example is Docker and LXC.

### Disaster Recovery using Virtualization
- In virtualized environments, virtual machines can be backed up as images which can be used to quickly restore the service in case of a disaster.
- The virtual machine images can be stored in a remote location and used to spawn the virtual machines on any available hardware in case the primary data center goes down.
- This enables high availability and disaster recovery of services as the backup virtual machines can be quickly brought online to handle user requests.
- The disaster recovery time can be reduced significantly using virtualization as the entire machine state is captured and transferred instead of individual files and configuration.