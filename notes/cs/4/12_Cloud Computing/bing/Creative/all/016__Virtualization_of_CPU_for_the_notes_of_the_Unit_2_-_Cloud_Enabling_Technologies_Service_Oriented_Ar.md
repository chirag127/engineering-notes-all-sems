### Virtualization of CPU for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing

- CPU virtualization is the process of abstracting the physical processor's resources into one or more logical representations that can be applied to different workloads.
- CPU virtualization enables the hardware resources of a single computer—processors, memory, storage and more—to be divided into multiple virtual computers, called virtual machines (VMs).
- Each VM runs its own operating system (OS) and behaves like an independent computer, even though it is running on just a portion of the actual underlying computer hardware.
- CPU virtualization is the foundation of cloud computing, as it allows cloud providers to serve users with their existing physical computer hardware and enables cloud users to purchase only the computing resources they need when they need it.
- CPU virtualization is supported by hardware features in modern processors, such as Intel Virtualization Technology (Intel VT) or AMD Virtualization (AMD-V).
- CPU virtualization can be implemented by software, such as a hypervisor or a virtual machine monitor (VMM), that manages the creation, execution, and termination of VMs.
- CPU virtualization brings several benefits, such as:
  - Resource efficiency: It allows multiple applications to run on a single physical computer, maximizing the utilization of the hardware's computing capacity.
  - Easier management: It enables automated deployment and configuration of VMs and applications, as well as security policies and resource allocation based on software-defined templates and rules.
  - Minimal downtime: It isolates the OS and applications from the hardware, making them more resilient to crashes and failures.
  - Portability and compatibility: It enables the migration and replication of VMs across different physical computers, regardless of the underlying hardware differences.
- CPU virtualization also has some challenges, such as:
  - Performance overhead: It introduces some additional processing and memory consumption by the hypervisor or VMM, which can affect the performance of the VMs and applications.
  - Security risks: It exposes the hypervisor or VMM as a potential target for attacks, as it has access to the hardware and all the VMs running on it.
  - Compatibility issues: It may not support some legacy or specialized applications that require direct access to the hardware or specific hardware features.

#### Mnemonics and learning tricks

- To remember the benefits of CPU virtualization, you can use the acronym **REMP**:
  - **R**esource efficiency
  - **E**asier management
  - **M**inimal downtime
  - **P**ortability and compatibility
- To remember the challenges of CPU virtualization, you can use the acronym **PSC**:
  - **P**erformance overhead
  - **S**ecurity risks
  - **C**ompatibility issues
- To remember the steps to enable CPU virtualization in the BIOS, you can use the acronym **FACSE**:
  - **F**7 or Advanced Mode
  - **A**dvanced tab
  - **C**PU configuration
  - **S**VM Mode or Intel VT or AMD-V
  - **E**xit and save changes