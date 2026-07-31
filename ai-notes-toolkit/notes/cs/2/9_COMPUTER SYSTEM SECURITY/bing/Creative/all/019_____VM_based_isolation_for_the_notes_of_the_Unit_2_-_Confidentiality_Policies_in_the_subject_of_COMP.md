# VM based isolation

- VM based isolation is a technique that uses hardware virtualization features to create and isolate a secure region of memory from the normal operating system .
- VM based isolation can be used to implement confidentiality policies that protect sensitive data or code from unauthorized access or modification by malicious or compromised processes.
- VM based isolation can also be used to enforce integrity policies that prevent unauthorized or unintended changes to the system configuration or behavior by malicious or compromised processes.
- VM based isolation relies on the following components :
  - A hypervisor or virtual machine monitor (VMM) that runs directly on the hardware and controls the allocation and access of physical resources to virtual machines (VMs).
  - A host operating system that runs on top of the hypervisor and provides the basic services and interfaces for the VMs.
  - One or more guest operating systems that run inside the VMs and provide the user applications and services.
  - A secure kernel that runs inside a special VM and provides the security services and policies for the VM based isolation.
- VM based isolation can provide the following benefits :
  - It can isolate different security domains or levels within the same physical system, such as trusted and untrusted, classified and unclassified, or production and development.
  - It can prevent or limit the propagation of malware or attacks from one VM to another or from the host to the guest or vice versa.
  - It can protect the integrity and confidentiality of the system boot process and code execution by verifying the signatures and hashes of the firmware, bootloader, kernel, and drivers.
  - It can reduce the attack surface and complexity of the host operating system by delegating some security functions to the secure kernel or the hypervisor.
  - It can enable dynamic and flexible security policies and configurations that can be adapted to the changing needs and threats of the system and the users.