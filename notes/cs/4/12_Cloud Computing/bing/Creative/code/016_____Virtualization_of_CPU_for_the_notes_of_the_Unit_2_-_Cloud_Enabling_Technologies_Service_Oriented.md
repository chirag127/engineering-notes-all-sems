### Virtualization of CPU

- CPU virtualization is a technique that creates multiple versions of various system resources, including your CPU, server, storage, etc. 
- CPU virtualization involves a single CPU acting as if it were multiple separate CPUs. The most common reason for doing this is to run multiple different operating systems on one machine. 
- CPU virtualization emphasizes performance and runs directly on the available CPUs whenever possible. 
- CPU virtualization can be achieved by using a software layer called a hypervisor, which creates and manages virtual machines (VMs) that run on the physical CPU. 
- CPU virtualization can be classified into two types: full virtualization and paravirtualization. 
- Full virtualization allows the guest operating system to run unmodified on the virtual CPU, as if it were running on a real CPU. The hypervisor intercepts and emulates the privileged instructions of the guest operating system. 
- Paravirtualization requires the guest operating system to be modified to run on the virtual CPU. The hypervisor exposes a set of hypercalls that the guest operating system can use to communicate with the hypervisor. Paravirtualization can improve performance and reduce overhead. 
- CPU virtualization has many benefits, such as:
  - Isolating and securing different workloads on the same CPU. 
  - Increasing the utilization and efficiency of the CPU. 
  - Reducing the cost and complexity of hardware and maintenance. 
  - Enabling scalability and flexibility of the CPU resources. 
  - Supporting disaster recovery and business continuity. 
- CPU virtualization can be enabled in the BIOS settings of the PC, by finding and selecting the CPU configuration option and choosing the virtualization mode (such as SVM or VT-x).  
- CPU virtualization can also be enabled in the operating system settings, by installing and configuring a hypervisor software (such as VMware, Hyper-V, VirtualBox, etc.) and creating and managing VMs.