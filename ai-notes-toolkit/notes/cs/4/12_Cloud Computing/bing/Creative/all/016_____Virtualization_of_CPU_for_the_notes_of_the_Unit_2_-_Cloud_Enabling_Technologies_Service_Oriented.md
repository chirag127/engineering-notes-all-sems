# Virtualization of CPU

- CPU virtualization is a technique that creates multiple versions of various system resources, including your CPU, server, storage, etc. 
- CPU virtualization involves a single CPU acting as if it were multiple separate CPUs. The most common reason for doing this is to run multiple different operating systems on one machine. 
- CPU virtualization emphasizes performance and runs directly on the available CPUs whenever possible. 
- CPU virtualization is one of the cloud-computing technologies that requires a single CPU to work, which acts as multiple machines working together. 
- CPU virtualization can be classified into two types: full virtualization and paravirtualization. 
- Full virtualization allows the guest operating system to run unmodified on the virtual machine, as if it were running on a physical machine. The virtualization software (hypervisor) intercepts and emulates the instructions that require privileged access from the guest operating system. 
- Paravirtualization requires the guest operating system to be modified to run on the virtual machine. The guest operating system is aware of the virtualization and communicates directly with the hypervisor, avoiding the need for emulation. Paravirtualization can offer better performance and efficiency than full virtualization. 
- CPU virtualization can be enabled in the BIOS settings of the computer. The steps may vary depending on the manufacturer and model of the computer, but generally involve accessing the Advanced Mode option, finding and selecting CPU configuration, and choosing Enabled for the virtualization feature.  
- CPU virtualization can provide various benefits, such as:
  - Increased utilization and efficiency of the CPU resources. 
  - Reduced costs and energy consumption by consolidating multiple physical machines into one. 
  - Enhanced security and isolation of the virtual machines. 
  - Improved scalability and flexibility of the computing environment. 
  - Easier backup and recovery of the virtual machines. 
  - Access to a larger library of apps and operating systems.