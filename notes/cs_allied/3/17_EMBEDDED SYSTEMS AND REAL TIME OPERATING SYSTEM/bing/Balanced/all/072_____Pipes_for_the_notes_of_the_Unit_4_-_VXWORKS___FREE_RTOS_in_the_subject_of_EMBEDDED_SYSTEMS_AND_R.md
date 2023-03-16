# Pipes for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Pipes are a form of inter-process communication (IPC) that allow data to be transferred between two processes in a unidirectional or bidirectional way.
- Pipes are often implemented as circular buffers or queues that can store a fixed amount of data until it is read by the receiver or overwritten by the sender.
- Pipes can be used to implement various communication patterns, such as producer-consumer, client-server, or filter-chain.
- Pipes can be either named or unnamed, depending on whether they have a unique identifier in the file system or not.
- Pipes can be either blocking or non-blocking, depending on whether they wait for data to be available or not.

## Pipes in VxWorks

- VxWorks is a real-time operating system (RTOS) that is widely used in embedded systems and critical applications.
- VxWorks supports pipes as a form of IPC, along with other mechanisms such as message queues, semaphores, signals, shared memory, and sockets.
- VxWorks pipes are implemented as message queues with a fixed message size of one byte, which means they can only transfer byte streams.
- VxWorks pipes can be created with the pipeDevCreate() function, which takes the name, maximum number of bytes, and options as parameters.
- VxWorks pipes can be opened with the open() function, which returns a file descriptor that can be used to read or write data with the read() or write() functions.
- VxWorks pipes can be closed with the close() function, which releases the file descriptor and the resources associated with the pipe.
- VxWorks pipes can be deleted with the pipeDevDelete() function, which removes the pipe from the file system and frees the memory allocated for it.
- VxWorks pipes can be configured with the ioctl() function, which can set or get various attributes of the pipe, such as the blocking mode, the number of bytes available, or the number of readers or writers.
- VxWorks pipes can be used to communicate between tasks within the same or different processes, or between processes and device drivers.

## Pipes in FreeRTOS

- FreeRTOS is another RTOS that is designed for small and simple embedded systems.
- FreeRTOS does not support pipes as a native form of IPC, but it provides a similar feature called stream buffers.
- Stream buffers are circular buffers that can store variable-length messages or byte streams, and can be used to transfer data between tasks or between tasks and interrupts.
- Stream buffers can be created with the xStreamBufferCreate() function, which takes the buffer size and the trigger level as parameters.
- Stream buffers can be written to with the xStreamBufferSend() function, which takes the buffer handle, the data pointer, the data length, and the block time as parameters.
- Stream buffers can be read from with the xStreamBufferReceive() function, which takes the buffer handle, the data pointer, the data length, and the block time as parameters.
- Stream buffers can be deleted with the vStreamBufferDelete() function, which takes the buffer handle as a parameter.
- Stream buffers can be queried with the xStreamBufferBytesAvailable() function, which returns the number of bytes available in the buffer, or the xStreamBufferSpacesAvailable() function, which returns the number of free spaces in the buffer.
- Stream buffers can be used to communicate between tasks within the same or different processes, or between tasks and interrupts.