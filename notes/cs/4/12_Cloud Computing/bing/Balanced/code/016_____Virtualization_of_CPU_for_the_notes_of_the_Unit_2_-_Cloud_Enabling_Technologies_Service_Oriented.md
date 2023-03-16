### Virtualization of CPU

- CPU virtualization is a technique that creates multiple versions of various system resources, including your CPU, server, storage, etc. 
- CPU virtualization involves a single CPU acting as if it were multiple separate CPUs. The most common reason for doing this is to run multiple different operating systems on one machine. 
- CPU virtualization emphasizes performance and runs directly on the available CPUs whenever possible. 
- CPU virtualization can be classified into two types: full virtualization and paravirtualization. 
- Full virtualization allows the guest operating system to run unmodified on the virtual machine, as if it were running on a physical machine. The virtual machine monitor (VMM) or hypervisor provides the necessary abstraction and isolation between the guest and the host. 
- Paravirtualization requires the guest operating system to be modified to run on the virtual machine. The guest operating system is aware of the virtualization and communicates with the VMM or hypervisor through a special interface. Paravirtualization can improve performance and reduce overhead. 
- CPU virtualization can be enabled or disabled in the BIOS settings of the host machine. The exact steps may vary depending on the manufacturer and model of the machine, but generally involve accessing the Advanced Mode option, finding and selecting CPU configuration, and choosing Enabled or Disabled for the virtualization feature.  
- CPU virtualization can provide many benefits, such as increased efficiency, flexibility, scalability, security, and reliability. CPU virtualization can also reduce costs, energy consumption, and hardware maintenance.