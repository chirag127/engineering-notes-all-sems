 Here is the content in markdown format for the topic ### Types of Virtualization for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing:

### Types of Virtualization

The major types of virtualization are:

1. Full Virtualization: Creates a complete virtual machine which acts as a real machine. The guest OS is unaware of the underlying hardware. Examples: VMware, VirtualBox.
Advantages: High performance and resource efficiency.
Disadvantages: Requires more resources and additional software.

2. Para Virtualization: The guest OS is modified to be aware of the virtual environment. This allows direct access to hardware resulting in better performance. Example: Xen.
Advantages: Better performance than full virtualization.
Disadvantages: The guest OS needs to be modified.

3. OS-Level Virtualization: Multiple isolated user space instances are running on a single kernel. The resources are shared but software is isolated. Examples: Docker, LXC.
Advantages: Fast, efficient and lightweight.
Disadvantages: Limited isolation and less flexibility.

4. Application Virtualization: An application is virtualized and separated from the underlying OS. It is packaged into a container that can run on any system. Example: ThinApp.
Advantages: Portable and isolated applications.
Disadvantages: Limited to applications and requires additional software.

Mnemonics:
Full -> Guest unaware, additional software
Para -> Guest aware, modified OS
OS -> Share kernel, isolated software
App -> Application isolated, portable

Learning Tricks:
Think of virtualization as layers. Full virtualization is the top layer which creates a full virtual machine. Para virtualization lies below it where the guest OS is modified. Even lower is OS-level virtualization where the resources are shared. Application virtualization is the lowest layer where only the application is virtualized.