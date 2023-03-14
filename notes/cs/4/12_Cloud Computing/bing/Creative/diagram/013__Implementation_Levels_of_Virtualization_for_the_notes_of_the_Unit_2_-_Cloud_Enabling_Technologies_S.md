The following is a detailed ASCII diagram for Implementation Levels of Virtualization for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing.

The diagram is based on the information from the web search results   and shows the five levels of virtualization implementation: Instruction Set Architecture Level (ISA), Hardware Abstraction Level (HAL), Operating System Level, Library Support Level, and User-Application Level.

The diagram uses the following symbols:

- `|` and `-` for horizontal and vertical lines
- `+` for line intersections
- `>` for arrows
- `*` for bullet points
- `[]` for boxes
- `()` for circles
- `{}` for braces

The diagram is as follows:

```
+---------------------------------------------------------------------------+
|                                                                           |
|  User-Application Level                                                   |
|                                                                           |
|  * Virtualization at the application level                                |
|  * Allows multiple instances of the same application to run concurrently  |
|  * Examples: Java Virtual Machine, .NET Framework                         |
|                                                                           |
+---------------------------------------------------------------------------+
        |
        |
        V
+---------------------------------------------------------------------------+
|                                                                           |
|  Library Support Level                                                    |
|                                                                           |
|  * Virtualization at the library level                                    |
|  * Allows applications to use different libraries without recompilation   |
|  * Examples: Wine, Cygwin                                                 |
|                                                                           |
+---------------------------------------------------------------------------+
        |
        |
        V
+---------------------------------------------------------------------------+
|                                                                           |
|  Operating System Level                                                   |
|                                                                           |
|  * Virtualization at the operating system level                           |
|  * Allows multiple instances of the same or different OS to run on the    |
|    same hardware                                                          |
|  * Examples: Docker, LXC, Solaris Zones                                   |
|                                                                           |
+---------------------------------------------------------------------------+
        |
        |
        V
+---------------------------------------------------------------------------+
|                                                                           |
|  Hardware Abstraction Level (HAL)                                         |
|                                                                           |
|  * Virtualization at the hardware level                                   |
|  * Allows multiple instances of different OS to run on the same hardware  |
|  * Uses a bare hypervisor to manage the hardware resources                |
|  * Examples: VMware ESX, Xen, Hyper-V                                     |
|                                                                           |
+---------------------------------------------------------------------------+
        |
        |
        V
+---------------------------------------------------------------------------+
|                                                                           |
|  Instruction Set Architecture Level (ISA)                                 |
|                                                                           |
|  * Virtualization at the instruction set level                            |
|  * Allows legacy code written for different hardware architectures to run |
|    on the same hardware                                                   |
|  * Uses an ISA emulator to interpret the source code                      |
|  * Examples: QEMU, Bochs, Virtual PC                                      |
|                                                                           |
+---------------------------------------------------------------------------+
        |
        |
        V
+---------------------------------------------------------------------------+
|                                                                           |
|  Hardware Machine                                                         |
|                                                                           |
|  * The physical server that hosts the virtual machines                    |
|  * Provides the CPU, memory, disk, and I/O devices                        |
|                                                                           |
+---------------------------------------------------------------------------+
```