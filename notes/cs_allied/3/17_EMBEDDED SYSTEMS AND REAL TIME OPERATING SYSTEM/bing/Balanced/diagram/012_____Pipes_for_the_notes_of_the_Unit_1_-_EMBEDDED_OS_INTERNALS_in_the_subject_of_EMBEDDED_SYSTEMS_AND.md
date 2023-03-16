### Pipes

- Pipes are a form of inter-process communication (IPC) that allow data to be transferred between two or more processes in a sequential manner.
- Pipes are often used in embedded systems to pass simple messages between tasks, such as sensor readings, commands, or status updates .
- Pipes have two ends: a read end and a write end. Data written to the write end can be read from the read end by another process .
- Pipes can be either named or unnamed. Named pipes have a file name and can be accessed by any process that knows the name. Unnamed pipes are created by the system call `pipe` and are only accessible by the processes that created them or their descendants .
- Pipes can be either blocking or non-blocking. Blocking pipes wait until there is data available to read or write, while non-blocking pipes return immediately with an error code if there is no data available .
- Pipes have a limited buffer size, which means that they can run out of space if the writer is faster than the reader. This can cause data loss or deadlock in embedded software.
- Pipes can be used with other IPC methods, such as message queues, mailboxes, or sockets, to provide more flexibility and functionality .
- Pipes are configured at build time in some embedded operating systems, such as Nucleus SE. There may be a maximum number of pipes allowed for an application.
- Pipes are one of the components of embedded systems, along with hardware, application-specific software, and a real-time operating system (RTOS).