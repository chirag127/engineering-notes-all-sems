## Unit 1 - EMBEDDED OS INTERNALS

- An embedded operating system is a computer operating system designed for use in embedded computer systems .
- Embedded computer systems are devices that are installed as built-in components of a wider system, in which they serve a special, functional purpose.
- Examples of embedded computer systems are smart TVs, digital cameras, smart watches, routers, medical devices, etc.
- An embedded operating system is engineered and optimized to improve the efficiency of controlling the hardware resources, drive graphics processing, and decrease response time for the tasks performed by the device.
- An embedded operating system is also designed to be small, resource-efficient, dependable, and reduce many features that aren't required by specialized applications.
- An embedded operating system is essentially the brain of an embedded computer system, which defines the functionality of a product.
- An embedded operating system is a combination of software and hardware. It produces an easily understandable result by humans in many formats such as images, text, and voice.
- Embedded operating systems are developed with programming code, which helps convert hardware languages into software languages like C and C++.
- An embedded operating system achieves these functions via a kernel that includes, at a minimum: process management, memory management, and I/O system management components.
- Process management is the function of creating, scheduling, and terminating processes or threads that execute the application code.
- Memory management is the function of allocating, deallocating, and protecting the memory space used by the processes, the kernel, and the device drivers.
- I/O system management is the function of interfacing with the hardware devices, such as sensors, actuators, displays, keyboards, etc., and providing services for data transfer, device control, and error handling.
- An embedded operating system may also include other components, such as file system, network stack, security, graphics, etc., depending on the requirements and features of the embedded device.
- An embedded operating system aims to perform with certainty specific task(s) regularly that help the device operate.
- How the OS fits into an embedded system depends on the architecture and design of the system, which can be classified into three types: monolithic, microkernel, and hybrid.
- A monolithic architecture is one where the OS and the application code are tightly coupled and run in the same address space. This architecture is simple, fast, and efficient, but also prone to errors, security risks, and difficult to maintain and update.
- A microkernel architecture is one where the OS is divided into a minimal kernel that provides the basic services, and a set of modules that run in separate address spaces and provide the additional services. This architecture is modular, flexible, and secure, but also complex, slow, and resource-intensive.
- A hybrid architecture is one where the OS combines the features of both monolithic and microkernel architectures, and allows the developer to choose the best trade-off between performance and reliability.