 Here is the content in markdown format for the topic ### Types of Virtualization for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing:

### Types of Virtualization

The major types of virtualization are:

1. Full Virtualization: Creates a complete virtual machine that acts like a real computer with its own operating system. The guest OS is unaware of the host system. Examples: VMware, VirtualBox.
Advantages: High isolation, flexibility, compatibility.
Disadvantages: Resource intensive, additional overhead.

2. Paravirtualization: Guest OS is modified to communicate with the host system for improved performance. Examples: Xen.
Advantages: Better performance than full virtualization.
Disadvantages: Guest OS needs modifications.

3. Operating System-level Virtualization: Creates isolated user space instances that share the kernel. Examples: Linux Containers (LXC), Solaris Zones.
Advantages: Fast, efficient, low overhead.
Disadvantages: Limited isolation, sharing kernel has security implications.

4. Application Virtualization: Packages applications to run in isolated environments. Examples: Microsoft App-V, VMware ThinApp.
Advantages: Isolates apps, portable, easy to manage.
Disadvantages: Limited use cases, not suitable for running entire OS or servers.

Mnemonics:
FULL - Full Virtualization
MODS - Paravirtualization (Modified OS)
SHAR - OS-level Virtualization (Share Kernel)
APPS - Application Virtualization

Learning Tricks:
Think of virtualization as stacking layers. Full virtualization is the top layer which is most isolated but slowest. As we move down, performance increases but isolation decreases.

[Detailed diagrams, code examples, tables, etc. can be added if required to learn the concepts better.]