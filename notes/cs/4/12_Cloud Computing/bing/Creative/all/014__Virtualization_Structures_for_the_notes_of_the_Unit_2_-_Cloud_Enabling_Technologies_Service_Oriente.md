### Virtualization Structures for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing

- Virtualization is a technology that can manipulate hardware and create virtual machines that can run multiple operating systems and applications .
- Virtualization is the foundation element of cloud computing, which is the delivery of shared resources as a service-on-demand via the internet.
- Virtualization structures are the ways of organizing the virtual machines and the physical resources in a cloud environment.
- There are two main types of virtualization structures: **hosted virtualization** and **bare-metal virtualization** .

#### Hosted virtualization
- In hosted virtualization, the virtual machines run on top of a host operating system, which manages the access to the physical resources such as CPU, memory, disk, and network .
- The host operating system can be any general-purpose operating system, such as Windows, Linux, or Mac OS .
- The virtual machines are isolated from each other and can run different operating systems and applications .
- The advantages of hosted virtualization are:
  - It is easy to install and use, as it does not require any modification to the hardware or the host operating system .
  - It supports a wide range of guest operating systems and applications, as it does not depend on the host operating system .
  - It provides a high level of security and fault tolerance, as the virtual machines are isolated from each other and from the host operating system .
- The disadvantages of hosted virtualization are:
  - It has a high overhead, as the host operating system consumes some of the physical resources and adds an extra layer of software between the virtual machines and the hardware .
  - It has a low performance, as the host operating system introduces some latency and interference in the access to the physical resources .
  - It has a limited scalability, as the number of virtual machines that can run on a single host is limited by the capacity of the host operating system and the hardware .

#### Bare-metal virtualization
- In bare-metal virtualization, the virtual machines run directly on the hardware, without any host operating system .
- The hardware is managed by a special software called **hypervisor** or **virtual machine monitor (VMM)**, which creates and controls the virtual machines and allocates the physical resources to them .
- The hypervisor can be either **type 1** or **type 2** .
  - A type 1 hypervisor runs directly on the hardware and has full control over it .
  - A type 2 hypervisor runs on top of another operating system, which acts as a host for the hypervisor and provides some of the hardware access .
- The virtual machines are isolated from each other and can run different operating systems and applications .
- The advantages of bare-metal virtualization are:
  - It has a low overhead, as there is no host operating system to consume the physical resources or to add an extra layer of software between the virtual machines and the hardware .
  - It has a high performance, as the hypervisor provides a direct and efficient access to the physical resources .
  - It has a high scalability, as the number of virtual machines that can run on a single host is limited only by the capacity of the hardware .
- The disadvantages of bare-metal virtualization are:
  - It is difficult to install and use, as it requires some modification to the hardware or the firmware to support the hypervisor .
  - It supports a limited range of guest operating systems and applications, as it depends on the compatibility of the hypervisor and the hardware .
  - It provides a low level of security and fault tolerance, as the virtual machines are not isolated from the hypervisor and the hardware .

#### Example of hosted virtual