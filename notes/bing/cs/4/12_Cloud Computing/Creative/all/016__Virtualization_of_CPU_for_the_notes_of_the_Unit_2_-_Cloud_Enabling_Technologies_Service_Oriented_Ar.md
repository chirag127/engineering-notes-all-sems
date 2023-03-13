### Virtualization of CPU for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing

- CPU virtualization is one of the cloud-computing technologies that allows a single CPU to act as multiple virtual machines (VMs) working together.
- CPU virtualization enables cloud providers to serve users with their existing physical computer hardware, and enables cloud users to purchase only the computing resources they need when they need it, and to scale those resources cost-effectively as their workloads grow .
- CPU virtualization can be classified into two types: software-based and hardware-assisted.
- Software-based CPU virtualization is where the application code gets executed on the CPU directly, but with the help of a software layer called a hypervisor or a virtual machine monitor (VMM) that intercepts and emulates the privileged instructions of the guest operating systems (OSs) running on the VMs.
- Hardware-assisted CPU virtualization is where the CPU has built-in features that support virtualization, such as Intel VT-x and AMD-V, that allow the guest OSs to run in a separate mode called root mode, while the hypervisor runs in a higher-privileged mode called host mode.
- The advantages of CPU virtualization include:
  - Improved resource utilization and efficiency, as multiple VMs can share the same CPU and run different applications and OSs simultaneously  .
  - Reduced costs and energy consumption, as fewer physical servers are needed to run the same workloads, and less power and cooling are required  .
  - Increased flexibility and scalability, as VMs can be created, migrated, cloned, and deleted on demand, and can adapt to changing workloads and user demands  .
  - Enhanced security and isolation, as VMs are isolated from each other and from the host, and can run different security policies and configurations  .
  - Simplified management and maintenance, as VMs can be managed and updated centrally and remotely, and can be backed up and restored easily  .
- The disadvantages of CPU virtualization include:
  - Performance overhead, as the hypervisor adds an extra layer of abstraction and complexity, and may introduce latency and contention for CPU resources among the VMs  .
  - Compatibility and interoperability issues, as some applications and OSs may not run well or at all on virtualized environments, and may require modifications or adaptations  .
  - Security and reliability risks, as the hypervisor may introduce new vulnerabilities and attack vectors, and may compromise the availability and integrity of the VMs if it fails or gets compromised  .
- A possible mnemonic to remember the types of CPU virtualization is: **SH**ow me the **H**ardware and **S**oftware **V**irtualization.
- A possible learning trick to understand the difference between software-based and hardware-assisted CPU virtualization is: Imagine that the CPU is a car, and the hypervisor is a driver. In software-based CPU virtualization, the driver has to use a manual transmission, and has to shift gears every time the car needs to change speed or direction. In hardware-assisted CPU virtualization, the driver has an automatic transmission, and the car can adjust the gears by itself. The automatic transmission makes the driving smoother and faster, but it also requires a more advanced and expensive car.