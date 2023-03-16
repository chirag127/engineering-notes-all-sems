# Pipes for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Pipes are a form of inter-process communication (IPC) that allow data to be transferred between two processes in a unidirectional or bidirectional way.
- Pipes are often implemented as circular buffers or queues that can store a fixed amount of data in memory.
- Pipes can be used to implement producer-consumer patterns, where one process writes data to the pipe and another process reads data from the pipe.
- Pipes can also be used to implement filters, where one process reads data from a pipe, performs some transformation on it, and writes the result to another pipe.
- Pipes can be either named or unnamed. Named pipes have a unique identifier that can be used by any process to access the pipe. Unnamed pipes are created by a parent process and inherited by its child processes.
- Pipes can be either blocking or non-blocking. Blocking pipes wait until there is data available to read or write, while non-blocking pipes return immediately with an error code if there is no data available or no space to write.
- Pipes can have different modes of operation, such as byte-stream mode, message mode, or record mode. Byte-stream mode treats the data as a continuous stream of bytes, while message mode and record mode preserve the boundaries of the data units written to the pipe.

## Pipes in VxWorks

- VxWorks is a real-time operating system (RTOS) that is widely used in embedded systems and critical infrastructure sectors.
- VxWorks supports pipes as a form of IPC, along with other mechanisms such as message queues, semaphores, shared memory, and sockets.
- VxWorks pipes are implemented as message queues with a fixed message size of one byte. This means that pipes in VxWorks can only operate in byte-stream mode.
- VxWorks pipes can be created by using the pipeDevCreate() function, which takes the name of the pipe, the maximum number of bytes that can be stored in the pipe, and the options for the pipe as arguments.
- VxWorks pipes can be accessed by using the open(), close(), read(), and write() functions, which are similar to the standard POSIX functions for file operations.
- VxWorks pipes can be configured to be blocking or non-blocking by using the O_NONBLOCK option in the open() function. By default, pipes are blocking in VxWorks.
- VxWorks pipes can also be configured to be bidirectional by using the O_RDWR option in the open() function. By default, pipes are unidirectional in VxWorks.
- VxWorks pipes can be deleted by using the pipeDevDelete() function, which takes the name of the pipe and a boolean flag to indicate whether to force the deletion or not as arguments.

## Pipes in FreeRTOS

- FreeRTOS is another RTOS that is widely used in embedded systems and IoT devices.
- FreeRTOS does not support pipes as a native form of IPC, but it provides a similar mechanism called stream buffers.
- Stream buffers are circular buffers that can store a variable amount of data in memory. They can be used to implement pipes, UARTs, TCP/IP stacks, and other communication protocols.
- Stream buffers can be created by using the xStreamBufferCreate() function, which takes the size of the buffer and the trigger level as arguments. The trigger level is the minimum amount of data that must be in the buffer before a task that is blocked on the buffer is unblocked.
- Stream buffers can be accessed by using the xStreamBufferSend() and xStreamBufferReceive() functions, which take the handle of the buffer, a pointer to the data, the size of the data, and a timeout value as arguments.
- Stream buffers can be configured to be blocking or non-blocking by using the portMAX_DELAY or 0 as the timeout value in the xStreamBufferSend() and xStreamBufferReceive() functions. By default, stream buffers are blocking in FreeRTOS.
- Stream buffers can also be configured to operate in byte-stream mode or message mode by using the xStreamBufferCreateStatic() or xStreamBufferCreateStaticMessage() functions, respectively. In message mode, the stream buffer preserves the boundaries of the data units written to the buffer.
- Stream buffers can be deleted by using the vStreamBufferDelete() function, which takes the handle of the buffer as an argument.