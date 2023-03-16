# General Architecture of VxWorks

- VxWorks is a real-time operating system (RTOS) that provides deterministic, priority-based preemptive scheduling, low latency, and minimal jitter for embedded systems.
- VxWorks is built on a modular, scalable, and upgradable architecture that supports multiple hardware architectures, such as Intel, Power, ARM, and RISC-V, and multiple processor modes, such as asymmetric multiprocessing (AMP), symmetric multiprocessing (SMP), and mixed modes and multi-OS (via Type 1 hypervisor) on 32- and 64-bit processors .
- VxWorks consists of three main components: the VxWorks kernel, the VxWorks libraries, and the VxWorks applications.
  - The VxWorks kernel is the core of the RTOS that provides the basic services, such as task management, intertask communication, memory management, interrupt handling, timer services, and device drivers.
  - The VxWorks libraries are a set of optional modules that extend the functionality of the kernel, such as networking, file systems, security, graphics, and POSIX compatibility.
  - The VxWorks applications are the user-defined programs that run on top of the kernel and the libraries, and can be written in C, C++, Ada, or Java.
- VxWorks supports a variety of development tools, such as the Wind River Workbench, the Wind River Compiler, the Wind River Debugger, and the Wind River Simics simulator, that enable developers to create, debug, test, and deploy VxWorks applications.
- VxWorks is designed to meet the high standards of safety, security, and reliability for mission-critical computing systems in various domains, such as aerospace and defense, industrial, medical, automotive, and consumer electronics .