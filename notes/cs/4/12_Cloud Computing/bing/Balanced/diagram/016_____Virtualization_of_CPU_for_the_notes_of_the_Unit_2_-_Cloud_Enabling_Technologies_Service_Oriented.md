### Virtualization of CPU

- CPU virtualization is a technique that creates multiple versions of various system resources, including your CPU, server, storage, etc. 
- CPU virtualization involves a single CPU acting as if it were multiple separate CPUs. The most common reason for doing this is to run multiple different operating systems on one machine. 
- CPU virtualization emphasizes performance and runs directly on the available CPUs whenever possible. 
- CPU virtualization can be classified into two types: full virtualization and paravirtualization. 
- Full virtualization allows the guest operating system to run unmodified on the virtual machine, as if it were running on a physical machine. The virtual machine monitor (VMM) or hypervisor provides the necessary abstraction and isolation between the guest and the host. 
- Paravirtualization requires the guest operating system to be modified to run on the virtual machine, as it is aware of the presence of the VMM or hypervisor. The guest operating system can communicate directly with the VMM or hypervisor, which improves performance and efficiency. 
- CPU virtualization can be enabled in the BIOS settings of the host machine, by finding and selecting the CPU configuration option and choosing the appropriate mode (such as SVM, VT-x, VT-d, etc.)  
- CPU virtualization can provide various benefits, such as:
  - Increased utilization and efficiency of the CPU resources. 
  - Reduced costs and energy consumption by consolidating multiple physical machines into one. 
  - Enhanced security and isolation by preventing malware and attacks from affecting other virtual machines or the host. 
  - Improved flexibility and scalability by allowing the creation, deletion, migration, and backup of virtual machines as needed. 
  - Expanded compatibility and functionality by enabling the use of different operating systems and applications on one machine.