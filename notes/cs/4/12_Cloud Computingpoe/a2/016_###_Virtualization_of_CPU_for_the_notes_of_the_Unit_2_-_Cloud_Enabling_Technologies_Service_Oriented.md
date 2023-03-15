 Here is the content in markdown format for the topic ### Virtualization of CPU for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing:

### Virtualization of CPU

- CPU virtualization is a technology which allows multiple operating systems to run on a single physical CPU.
- Each operating system thinks that it has exclusive access to the underlying hardware.
- In reality, the CPU is shared between the operating systems and the hypervisor is responsible for allocating CPU resources to different VMs and scheduling their execution.
- Some key techniques used for CPU virtualization are:
    - Processor mode virtualization: Sensitive instructions are trapped and emulated by the hypervisor.
    - Binary translation: Instructions are translated to hypervisor instructions on the fly.
    - Paravirtualization: The guest OS is modified to be hypervisor-aware and uses special hypercalls to request privileged operations.
- Advantages: Consolidation, Isolation, Flexibility. Multiple VMs can share the resources of a single physical CPU, applications are isolated from each other, resources can be dynamically scaled based on demand.
- Disadvantages: Performance overhead due to instruction emulation or translation. The performance can be improved using hardware-assisted virtualization which provides virtualization-specific CPU instructions to facilitate more efficient hypervisor implementations.
- Examples: VMware, KVM, VirtualBox, etc.
- Applications: Server consolidation, application isolation, OS-level sandboxing, elastic resource scaling, etc.

Mnemonics/Tricks:
- VCPU - Virtual CPU; P2V - Physical to Virtual (machine conversion); Hype calls - Hypervisor procedure calls.

Does this help? Let me know if you would like me to elaborate on any of the points or add more details.