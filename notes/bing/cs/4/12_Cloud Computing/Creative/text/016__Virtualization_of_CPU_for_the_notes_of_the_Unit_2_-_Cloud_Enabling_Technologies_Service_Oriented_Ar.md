### Virtualization of CPU

- CPU virtualization is a technique that creates multiple versions of various system resources, including your CPU, server, storage, etc. 
- CPU virtualization involves a single CPU acting as if it were multiple separate CPUs. The most common reason for doing this is to run multiple different operating systems on one machine. 
- CPU virtualization emphasizes performance and runs directly on the available CPUs whenever possible. 
- CPU virtualization can be achieved by using a software layer called a hypervisor, which creates and manages virtual machines (VMs) that run on the physical CPU. 
- CPU virtualization can be classified into two types: full virtualization and paravirtualization. 
- Full virtualization allows the guest operating system to run unmodified on the virtual CPU, as if it were running on a real CPU. The hypervisor intercepts and emulates the privileged instructions of the guest operating system. 
- Paravirtualization requires the guest operating system to be modified to run on the virtual CPU. The hypervisor exposes a set of hypercalls that the guest operating system can use to communicate with the hypervisor. Paravirtualization can offer better performance and scalability than full virtualization. 
- CPU virtualization can provide many benefits, such as:
  - Isolation: Each virtual machine is isolated from the others, which improves security and reliability. 
  - Consolidation: Multiple virtual machines can run on a single physical CPU, which reduces hardware costs and power consumption. 
  - Migration: Virtual machines can be moved from one physical CPU to another without downtime, which improves availability and load balancing. 
  - Compatibility: Virtual machines can run different operating systems and applications on the same physical CPU, which increases flexibility and interoperability. 
- CPU virtualization can be enabled in the BIOS settings of the physical CPU, by choosing the appropriate option for the virtualization technology supported by the CPU. For example, Intel CPUs support Intel Virtualization Technology (VT-x), and AMD CPUs support AMD Virtualization (AMD-V).