Virtualization of CPU is the process of abstracting the physical processor's resources into one or more logical representations that can be applied to different workloads. This allows a single computer to run multiple operating systems and applications on separate virtual machines (VMs) that share the same physical hardware. Virtualization of CPU enables more efficient utilization of computer hardware, easier management of IT resources, and minimal downtime of applications.

The following diagram illustrates the basic architecture of a virtualized CPU:

```
+-------------------+  +-------------------+  +-------------------+
|                   |  |                   |  |                   |
|  Guest OS 1      |  |  Guest OS 2      |  |  Guest OS 3      |
|                   |  |                   |  |                   |
|  Application 1   |  |  Application 2   |  |  Application 3   |
|                   |  |                   |  |                   |
+-------------------+  +-------------------+  +-------------------+
|                   |  |                   |  |                   |
|  Virtual CPU 1   |  |  Virtual CPU 2   |  |  Virtual CPU 3   |
|                   |  |                   |  |                   |
+-------------------+  +-------------------+  +-------------------+
|                   |  |                   |  |                   |
|  Virtualization  |  |  Virtualization  |  |  Virtualization  |
|  Software        |  |  Software        |  |  Software        |
|                   |  |                   |  |                   |
+-------------------+  +-------------------+  +-------------------+
|                   |  |                   |  |                   |
|  Physical CPU    |  |  Physical CPU    |  |  Physical CPU    |
|                   |  |                   |  |                   |
+-------------------+  +-------------------+  +-------------------+
```

Each guest OS runs on a virtual CPU that is mapped to a physical CPU by the virtualization software. The virtualization software is responsible for managing the allocation and scheduling of the physical CPU resources to the virtual CPUs, as well as handling any privileged instructions or interrupts from the guest OSes. The virtualization software can be either a hypervisor that runs directly on the hardware, or a host OS that runs on the hardware and provides virtualization services to the guest OSes. The virtualization software can also provide other features such as memory management, network access, storage access, and security for the virtual machines.   
