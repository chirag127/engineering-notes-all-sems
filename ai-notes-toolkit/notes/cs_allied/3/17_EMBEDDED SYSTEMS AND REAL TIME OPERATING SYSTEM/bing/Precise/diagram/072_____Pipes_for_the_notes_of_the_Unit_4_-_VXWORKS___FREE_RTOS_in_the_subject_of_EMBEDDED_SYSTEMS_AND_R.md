# Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

## Pipes

- Pipes are a mechanism for interprocess communication (IPC) in real-time operating systems such as VxWorks and FreeRTOS.
- Pipes allow two or more processes to exchange data in a unidirectional manner, with one process writing to the pipe and the other process reading from it.
- Pipes are implemented as a kernel object and are created using the `pipe` system call.
- The `pipe` system call returns two file descriptors, one for reading and one for writing.
- Data written to the write end of the pipe is buffered by the kernel until it is read by a process from the read end of the pipe.
- Pipes are useful for implementing filters, where the output of one process is used as the input to another process.
- Pipes can also be used to implement simple client-server architectures, where the server process listens on a named pipe and client processes connect to the server by opening the named pipe for writing.
- Pipes have some limitations, such as a fixed buffer size and the inability to seek within the data stream.
- Named pipes, also known as FIFOs, are a variation of pipes that can be accessed by multiple processes using a name in the file system.