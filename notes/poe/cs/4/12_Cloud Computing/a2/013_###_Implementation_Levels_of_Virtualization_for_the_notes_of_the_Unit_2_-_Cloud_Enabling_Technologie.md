 Here is the content in markdown format:

### Implementation Levels of Virtualization for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing

There are 3 levels of virtualization:

1. Full Virtualization: Provides a complete virtual copy of the underlying hardware. The guest OS is unaware of the virtualization. Examples: VMware, VirtualBox.
Mnemonic: Provides full hardware view. Guest OS unaware.

Advantages:
- High performance.
- Supports multiple guest OSs.
- high security as guest OS is isolated.

Disadvantages:
- Requires more resources.

2. Para-virtualization: The guest OS is modified to be virtualization aware to achieve high performance. Examples: Xen.
Mnemonic: Guest OS modified. Performance high.

Advantages:
- Better performance than full virtualization.

Disadvantages:
- Guest OS needs to be modified.
- Limited to only supported OSs.

3. Operating System-level Virtualization: The resources of a single OS are virtualized to create isolated environments. Examples: OpenVZ, LXC.
Mnemonic: Single OS, isolated environments.

Advantages:
- Low overhead.
- High density.

Disadvantages:
- Limited to a single OS.
- Less secure as isolation is not strong.

To summarize, choose the virtualization level based on your requirements like performance, security, support for multiple OSs, etc. Full virtualization provides strong isolation but lower performance. Para-virtualization provides better performance but with limitations. OS-level virtualization has low overhead but weaker isolation.