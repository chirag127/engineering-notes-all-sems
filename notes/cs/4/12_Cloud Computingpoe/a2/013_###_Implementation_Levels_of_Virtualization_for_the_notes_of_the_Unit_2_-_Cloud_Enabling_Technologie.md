 Here is the content in markdown format for the topic - ### Implementation Levels of Virtualization for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing:

### Implementation Levels of Virtualization

There are mainly 3 levels of virtualization:

1. Full Virtualization: This is the highest level of virtualization. Each virtual machine runs its own operating system. The virtual machines have access to virtualized hardware resources. Example: VMware, VirtualBox.

Advantages:

- Very isolated and secure. Each VM is separate and secure.
- Can run different operating systems on the same physical machine.
- High performance.

Disadvantages:

- Require more resources as each VM has its own OS.

2. Paravirtualization: The guest operating systems are modified to use special hypercall interfaces to access virtualized resources. The guest OS are aware of the virtualized environment. Example: Xen.

Advantages:

- Better performance than full virtualization.
- Lower overhead.

Disadvantages:

- The guest OS needs to be modified which is complex.

3. Operating System-level Virtualization: Multiple isolated user space instances are sharing the same operating system kernel. Uses containers like Docker, LXC, etc.

Advantages:

- Very fast and efficient.
- Low overhead as the OS kernel is shared.
- Easy to manage and deploy.

Disadvantages:

- Less isolation between containers.
- Can't run different operating systems.

Mnemonics:

FAST - Full virtualization, Paravirtualization, Application containers, System containers, OS-level virtualization.

Learning Tricks:

- Remember the levels from highest to lowest for isolation and resource usage.
- The disadvantages of one level becomes the advantages of the lower level.
- Use examples of software to relate to the levels.

Hope this helps! Let me know if you would like me to explain anything in more detail.