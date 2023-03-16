### Pipes

- Pipes are a form of inter-process communication (IPC) that allow data to be transferred between two processes in a unidirectional or bidirectional manner.
- Pipes are often used to implement filters, where the output of one process is fed as the input of another process.
- Pipes can be either named or unnamed. Named pipes have a file name and can be accessed by any process that knows the name. Unnamed pipes are created by the pipe() system call and are only accessible by the processes that created them or their descendants.
- VxWorks is a real-time operating system (RTOS) that supports pipes as a form of IPC. VxWorks provides the following functions for working with pipes:

  - pipeDevCreate(): creates a named pipe device with a specified name and size.
  - pipeDevDelete(): deletes a named pipe device and frees its resources.
  - pipe(): creates an unnamed pipe and returns two file descriptors, one for reading and one for writing.
  - read(): reads data from a pipe device or file descriptor.
  - write(): writes data to a pipe device or file descriptor.
  - close(): closes a pipe device or file descriptor.

- FreeRTOS is another RTOS that does not support pipes natively, but provides a similar functionality with stream buffers. Stream buffers are circular buffers that can be used to transfer data between tasks or between tasks and interrupts. FreeRTOS provides the following functions for working with stream buffers:

  - xStreamBufferCreate(): creates a stream buffer with a specified size and trigger level.
  - xStreamBufferCreateStatic(): creates a stream buffer with a specified size and trigger level using statically allocated memory.
  - vStreamBufferDelete(): deletes a stream buffer and frees its resources.
  - xStreamBufferSend(): sends data to a stream buffer and returns the number of bytes sent.
  - xStreamBufferSendFromISR(): sends data to a stream buffer from an interrupt service routine and returns the number of bytes sent.
  - xStreamBufferReceive(): receives data from a stream buffer and returns the number of bytes received.
  - xStreamBufferReceiveFromISR(): receives data from a stream buffer from an interrupt service routine and returns the number of bytes received.
  - xStreamBufferIsEmpty(): returns pdTRUE if the stream buffer is empty, or pdFALSE otherwise.
  - xStreamBufferIsFull(): returns pdTRUE if the stream buffer is full, or pdFALSE otherwise.
  - xStreamBufferReset(): resets the stream buffer to its initial empty state.
  - xStreamBufferSpacesAvailable(): returns the number of free bytes in the stream buffer.
  - xStreamBufferBytesAvailable(): returns the number of bytes in the stream buffer that are available for reading.
  - xStreamBufferSetTriggerLevel(): sets the trigger level for the stream buffer, which is the number of bytes that must be in the buffer before a task that is blocked on the buffer is unblocked.
  - xStreamBufferSendCompletedFromISR(): notifies the stream buffer that a higher priority task may have been unblocked by a call to xStreamBufferSendFromISR(), and requests a context switch if necessary.
  - xStreamBufferReceiveCompletedFromISR(): notifies the stream buffer that a higher priority task may have been unblocked by a call to xStreamBufferReceiveFromISR(), and requests a context switch if necessary.

- FreeRTOS+POSIX is an optional component of FreeRTOS that provides a subset of the POSIX standard for compatibility with existing applications. FreeRTOS+POSIX supports the pipe() function, which creates an unnamed pipe using two stream buffers, one for reading and one for writing. FreeRTOS+POSIX also supports the read(), write(), and close() functions for accessing the pipe file descriptors.