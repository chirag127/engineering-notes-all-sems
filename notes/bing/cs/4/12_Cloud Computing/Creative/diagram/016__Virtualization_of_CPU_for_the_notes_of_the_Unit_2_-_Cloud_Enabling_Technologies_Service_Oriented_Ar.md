Virtualization of CPU is the process of abstracting the physical processor's resources into one or more logical representations that can be applied to different workloads. This technique allows a single CPU to act like multiple CPUs, each running a different operating system or application. Virtualization of CPU can improve the performance, efficiency, and security of the system.

The following diagram illustrates the basic architecture of a virtualized CPU:

```
+------------------------+
|      Hypervisor        |
| (Virtual Machine Monitor) |
+------------------------+
|   Virtual CPU 1   |   Virtual CPU 2   |   Virtual CPU 3   |
+----------------+----------------+----------------+
| Guest OS 1 | Guest OS 2 | Guest OS 3 |
+---------+---------+---------+
| App 1 | App 2 | App 3 |
+-----+-----+-----+
+--------------------------------+
|        Physical CPU            |
+--------------------------------+
```

The hypervisor or virtual machine monitor (VMM) is the software layer that creates and manages the virtual CPUs. It allocates the physical CPU resources to the virtual CPUs and handles the interactions between them. The virtual CPUs run the guest operating systems and their applications, which are unaware of the virtualization layer. The hypervisor can also provide isolation and security between the virtual CPUs, preventing them from interfering with each other.