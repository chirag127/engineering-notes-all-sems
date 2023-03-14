### Implementation Levels of Virtualization for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing

Virtualization is the creation of a virtual version of something, such as an operating system, a storage device, or network resources. It is a key technology that enables cloud computing. In this context, virtualization provides the ability to run multiple virtual machines on a single physical machine, which leads to better utilization of resources and cost savings. There are several implementation levels of virtualization, which are discussed below:

1. Full Virtualization:
Full virtualization is the most common implementation level of virtualization. It emulates the complete hardware environment of a physical machine, including the CPU, memory, and peripherals. It allows multiple operating systems to run on a single physical machine. Each virtual machine is isolated from the others and has its own virtual hardware. This level of virtualization is used in cloud environments to provide Infrastructure-as-a-Service (IaaS).

2. Para-Virtualization:
Para-virtualization is similar to full virtualization, but it provides a modified operating system that is aware of the virtual environment. This allows the guest operating system to interact directly with the virtual hardware, which can improve performance. This level of virtualization is used in cloud environments to provide Platform-as-a-Service (PaaS).

3. Hardware Virtualization:
Hardware virtualization, also known as machine virtualization, is the process of creating a virtual machine that runs on a hypervisor. The hypervisor is a software layer that sits between the hardware and the virtual machines. It allows multiple virtual machines to run on a single physical machine, and provides isolation between them. This level of virtualization is used in cloud environments to provide Virtual Desktop Infrastructure (VDI).

4. Operating System-Level Virtualization:
Operating system-level virtualization, also known as containerization, is a lightweight form of virtualization that allows multiple isolated user-space instances to run on a single operating system. Each instance shares the same kernel, but has its own file system and network stack. This level of virtualization is used in cloud environments to provide Software-as-a-Service (SaaS).

Mnemonics and learning tricks for remembering the implementation levels of virtualization include:

- Remember FPHO (Full, Para, Hardware, Operating System) as an acronym for the four levels.
- Visualize a server rack with multiple virtual machines on each physical machine, and imagine the different levels of isolation and sharing that are possible.
- Think of the different virtualization levels as layers of abstraction, with each layer providing a different level of isolation and flexibility.

In conclusion, virtualization is an essential technology for cloud computing, and there are several implementation levels that provide different levels of isolation and sharing. Remembering the different levels and their use cases can help you understand how virtualization enables cloud computing.