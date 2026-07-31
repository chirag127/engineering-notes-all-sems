### Realtime scheduling for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Realtime scheduling is the process of allocating CPU time to tasks that have timing constraints and need to be executed in a predictable and deterministic manner.
- A real-time operating system (RTOS) is a software platform that provides the basic services and mechanisms for realtime scheduling, such as task creation, priority assignment, context switching, inter-task communication, and synchronization.
- VXWORKS and FREE RTOS are two examples of RTOS that are widely used in embedded systems and real-time applications.
- VXWORKS is a commercial RTOS that offers a rich set of features and supports various architectures and standards. It has a preemptive priority-based scheduler that can handle up to 256 priority levels and supports time slicing, round-robin, and deadline scheduling. It also provides kernel services such as memory management, interrupt handling, timers, message queues, semaphores, mutexes, and event flags.
- FREE RTOS is an open source RTOS that is designed to be simple, portable, and scalable. It has a preemptive priority-based scheduler that can handle up to 255 priority levels and supports time slicing and round-robin scheduling. It also provides kernel services such as task management, queues, semaphores, mutexes, software timers, and event groups.
- The main differences between VXWORKS and FREE RTOS are:

  - VXWORKS is a full-fledged RTOS that supports more features and standards than FREE RTOS, such as networking, file system, security, and graphical user interface. FREE RTOS is a minimalistic RTOS that provides only the core real-time scheduling functionality and kernel services, and relies on add-ons for additional features.
  - VXWORKS is a proprietary RTOS that requires a license fee and a development environment to use. FREE RTOS is a free and open source RTOS that can be downloaded and modified by anyone.
  - VXWORKS has a higher memory footprint and performance overhead than FREE RTOS, due to its complexity and functionality. FREE RTOS has a lower memory footprint and performance overhead, due to its simplicity and efficiency.
  - VXWORKS has a more mature and stable code base and documentation than FREE RTOS, due to its longer history and wider adoption. FREE RTOS has a more active and growing community and development than VXWORKS, due to its openness and popularity.

- References:

  -  https://www.freertos.org/about-RTOS.html
  -  https://www.sternumiot.com/blog-posts/crush-course-introduction-to-real-time-operating-system-rtos
  -  https://hackaday.com/2021/02/24/real-time-os-basics-picking-the-right-rtos-when-you-need-one/
  -  https://engineering.lehigh.edu/sites/engineering.lehigh.edu/files/_DEPARTMENTS/cse/research/tech-reports/2019/LU-CSE-19-003.pdf
  -  https://www.freertos.org/implementation/a00008.html