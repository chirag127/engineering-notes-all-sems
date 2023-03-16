### Pipes

- Pipes are a form of inter-process communication (IPC) that allow data to be transferred between two or more processes in a sequential manner.
- Pipes are often used in embedded systems to pass simple messages between tasks, such as sensor readings, commands, or status updates .
- Pipes have two ends: a read end and a write end. Data written to the write end can be read from the read end in a first-in first-out (FIFO) order .
- Pipes can be either named or unnamed. Named pipes have a file name and can be accessed by any process that knows the name. Unnamed pipes are anonymous and can only be accessed by the processes that created them or their descendants .
- Pipes can be either blocking or non-blocking. Blocking pipes wait until data is available or the pipe is full before returning from a read or write operation. Non-blocking pipes return immediately with an error code if data is not available or the pipe is full .
- Pipes can be either byte-stream or message-oriented. Byte-stream pipes treat data as a continuous stream of bytes, while message-oriented pipes preserve the boundaries of each message written to the pipe .
- Pipes have a limited capacity and can run out of space if the writer is faster than the reader. This can cause data loss or deadlock in embedded software. To avoid this, pipes should be sized appropriately for the application and the data rate .
- Pipes provide a more flexible means of passing data than mailboxes or queues, which are other forms of IPC in embedded systems. Mailboxes can only store one message at a time, while queues can store multiple messages of a fixed size. Pipes can store multiple messages of variable size and can be configured at build time or run time .