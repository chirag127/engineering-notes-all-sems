### Pipes

- Pipes are a form of inter-process communication (IPC) that allow data to be transferred between two or more processes in a sequential manner.
- Pipes are often used to implement filters, which are programs that process an input stream and produce an output stream.
- Pipes can be either named or unnamed. Named pipes have a file name and can be accessed by any process that knows the name. Unnamed pipes are created by the pipe() system call and are only accessible by the processes that created them or their descendants.
- Pipes can be either blocking or non-blocking. Blocking pipes wait until there is data available to read or write, while non-blocking pipes return immediately with an error code if there is no data available.
- Pipes can be either unidirectional or bidirectional. Unidirectional pipes only allow data to flow in one direction, while bidirectional pipes allow data to flow in both directions.
- Pipes can be either synchronous or asynchronous. Synchronous pipes guarantee that the data written by one process will be read by another process in the same order, while asynchronous pipes do not have such a guarantee.

#### Pipes in VxWorks

- VxWorks is a real-time operating system (RTOS) that supports pipes as a form of IPC.
- VxWorks provides the following system calls for creating and using pipes:

  - pipeDevCreate(): creates a named pipe device with a specified name and size.
  - pipeDevDelete(): deletes a named pipe device and frees its resources.
  - pipe(): creates an unnamed pipe and returns two file descriptors, one for reading and one for writing.
  - read(): reads data from a pipe device or file descriptor.
  - write(): writes data to a pipe device or file descriptor.
  - close(): closes a pipe device or file descriptor.

- VxWorks pipes are blocking by default, but can be made non-blocking by using the O_NONBLOCK flag in the open() or pipe() system calls.
- VxWorks pipes are unidirectional by default, but can be made bidirectional by using the O_RDWR flag in the open() or pipe() system calls.
- VxWorks pipes are synchronous by default, but can be made asynchronous by using the O_ASYNC flag in the open() or pipe() system calls.

#### Pipes in FreeRTOS

- FreeRTOS is another RTOS that supports pipes as a form of IPC.
- FreeRTOS does not provide a native implementation of pipes, but relies on the FreeRTOS+POSIX library, which is a port of the POSIX standard to FreeRTOS.
- FreeRTOS+POSIX provides the following functions for creating and using pipes:

  - pipe(): creates an unnamed pipe and returns two file descriptors, one for reading and one for writing.
  - read(): reads data from a pipe file descriptor.
  - write(): writes data to a pipe file descriptor.
  - close(): closes a pipe file descriptor.

- FreeRTOS+POSIX pipes are blocking by default, but can be made non-blocking by using the O_NONBLOCK flag in the pipe() function.
- FreeRTOS+POSIX pipes are unidirectional by default, but can be made bidirectional by using the O_RDWR flag in the pipe() function.
- FreeRTOS+POSIX pipes are synchronous by default, but can be made asynchronous by using the O_ASYNC flag in the pipe() function.