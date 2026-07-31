### Virtualization of CPU

- CPU virtualization is a technique that creates multiple versions of various system resources, including your CPU, server, storage, etc. 
- CPU virtualization involves a single CPU acting as if it were multiple separate CPUs. The most common reason for doing this is to run multiple different operating systems on one machine. 
- CPU virtualization emphasizes performance and runs directly on the available CPUs whenever possible. 
- CPU virtualization can be achieved by using a software layer called a hypervisor, which creates and manages virtual machines (VMs) that run on the physical CPU. 
- CPU virtualization can be classified into two types: full virtualization and paravirtualization. 
- Full virtualization allows the guest operating system to run unmodified on the virtual CPU, as if it were running on a real CPU. The hypervisor intercepts and emulates the privileged instructions of the guest operating system. 
- Paravirtualization requires the guest operating system to be modified to run on the virtual CPU. The hypervisor exposes a set of hypercalls that the guest operating system can use to communicate with the hypervisor. Paravirtualization can improve performance and reduce overhead. 
- CPU virtualization can provide many benefits, such as:
  - Isolation: Each VM runs independently and securely from other VMs, preventing interference and improving reliability. 
  - Consolidation: Multiple VMs can run on a single CPU, reducing the need for physical hardware and saving costs. 
  - Migration: VMs can be moved from one CPU to another without downtime, enabling load balancing and fault tolerance. 
  - Compatibility: VMs can run different operating systems and applications on the same CPU, increasing flexibility and interoperability.