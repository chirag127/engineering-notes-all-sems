 Here is the content in markdown format:

### Virtualization of CPU for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing

Virtualization of CPU refers to the creation of virtual machines that share the resources of a single physical machine. The key benefits of CPU virtualization are:

- Increased utilization: By sharing the resources of a single physical CPU across multiple virtual CPUs, the utilization of the physical CPU can be increased.
- Isolation: The virtual CPUs are isolated from each other and act as independent units. If one virtual CPU crashes, the others continue to function.
- Flexibility: Virtual CPUs can be added or removed dynamically to match the changing compute requirements.

Some key concepts in CPU virtualization are:

- Hypervisor: A hypervisor is a software layer that enables virtualization. It allows multiple operating systems to run on a single physical machine and manages the resources between the virtual machines.
- Guest OS: The operating system running within a virtual machine is called the guest OS.
- Host OS: The operating system running on the physical machine and hosting the virtual machines is called the host OS.

The two main types of hypervisors are:

- Type 1 or bare-metal hypervisor: Runs directly on the hardware and controls the hardware resources. Examples are VMware ESXi and Microsoft Hyper-V.
- Type 2 hypervisor: Runs on top of a host OS and the host OS interacts with the hardware. Examples are Oracle VirtualBox and VMware Workstation.

Some tips and mnemonics for learning CPU virtualization:

- "Hypervisor is the manager of the virtual clan" - To remember that the hypervisor manages the virtual machines
- "Guest comes to the host's feast" - To remember the relationship between guest OS and host OS
- "Type 1 is direct, Type 2 goes via route" - To remember the difference between Type 1 and Type 2 hypervisors

CPU virtualization enables efficient utilization of physical resources and is a key enabling technology for cloud computing. It powers the on-demand scalability and elasticity of cloud platforms.