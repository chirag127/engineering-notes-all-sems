### Overview of POSIX APIs

- POSIX stands for **Portable Operating System Interface** . It is a family of standards specified by **IEEE** for maintaining compatibility among operating systems.
- POSIX defines both the **system** and **user-level** application programming interfaces (APIs), along with command line shells and utility interfaces, for software compatibility (portability) with variants of Unix and other operating systems.
- POSIX is also a **trademark** of the IEEE. POSIX is intended to be used by both application and system developers.
- POSIX APIs are an increasingly popular OSAL (operating system abstraction layer) for IoT and embedded applications, as can be seen in Zephyr, AWS:FreeRTOS, TI-RTOS, and NuttX. Benefits of POSIX support in Zephyr include:
  - Offering a familiar API to non-embedded programmers, especially from Linux.
  - Enabling the use of existing libraries and middleware that use POSIX APIs.
  - Reducing the learning curve and development time for new applications.
- POSIX APIs are divided into several categories, such as:
  - Process control: functions for creating, terminating, and synchronizing processes, such as fork, exec, wait, and exit.
  - Signals: functions for sending and receiving signals between processes, such as kill, sigaction, and sigprocmask.
  - File and directory operations: functions for manipulating files and directories, such as open, close, read, write, and mkdir.
  - Pipes and FIFOs: functions for creating and using pipes and FIFOs for interprocess communication, such as pipe, mkfifo, and dup.
  - Sockets: functions for creating and using sockets for network communication, such as socket, bind, listen, accept, and connect.
  - Threads: functions for creating and managing threads, such as pthread_create, pthread_join, pthread_mutex, and pthread_cond.
  - Timers: functions for measuring and setting time, such as clock, time, alarm, and sleep.
  - Semaphores: functions for creating and using semaphores for synchronization, such as sem_init, sem_wait, and sem_post.
  - Shared memory: functions for creating and using shared memory segments for interprocess communication, such as shm_open, shm_unlink, and mmap.
  - Message queues: functions for creating and using message queues for interprocess communication, such as mq_open, mq_send, and mq_receive.
- POSIX APIs are defined in a number of **header files** that are included in the C POSIX library. Some of the common header files are:
  - stdio.h: input/output operations, such as printf, scanf, and fopen.
  - stdlib.h: memory management, random numbers, and system calls, such as malloc, free, rand, and system.
  - string.h: string manipulation, such as strcpy, strcat, and strcmp.
  - math.h: mathematical functions, such as sin, cos, and sqrt.
  - unistd.h: POSIX system calls, such as fork, exec, and pipe.
  - signal.h: signal handling, such as kill, sigaction, and sigprocmask.
  - fcntl.h: file control, such as open, close, and fcntl.
  - dirent.h: directory operations, such as opendir, readdir, and closedir.
  - sys/stat.h: file status, such as stat, fstat, and chmod.
  - sys/socket.h: socket operations, such as socket, bind, and connect.
  - pthread.h: thread operations, such as pthread_create, pthread_join, and pthread_mutex.
  - time.h: time operations, such as clock, time, and sleep.
  - semaphore.h: semaphore operations, such as sem_init, sem_wait, and sem_post.
  - mqueue.h: message queue operations, such as mq_open, mq_send, and mq_receive.
  - sys/mman.h: memory mapping, such as shm_open, shm_unlink, and mmap.

: https://docs.zephyrproject.org/latest/services/portability