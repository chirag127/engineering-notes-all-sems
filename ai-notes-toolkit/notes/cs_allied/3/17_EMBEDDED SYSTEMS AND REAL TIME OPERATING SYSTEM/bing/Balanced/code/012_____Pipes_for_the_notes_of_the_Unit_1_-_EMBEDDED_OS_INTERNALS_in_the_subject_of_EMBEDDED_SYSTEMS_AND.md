### Pipes

- Pipes are a form of inter-process communication (IPC) that allow data to be transferred between two or more processes in a sequential manner.
- Pipes are often used in embedded systems, where memory and CPU resources are limited, and tasks need to communicate efficiently and reliably.
- Pipes have two ends: a read end and a write end. Data written to the write end can be read from the read end in a first-in first-out (FIFO) order.
- Pipes can be either named or unnamed. Named pipes have a file name and can be accessed by any process that knows the name. Unnamed pipes are created by the system call `pipe` and can only be accessed by the processes that created them or their descendants .
- Pipes can be either blocking or non-blocking. Blocking pipes wait until there is data available to read or write, while non-blocking pipes return immediately with an error code if there is no data available.
- Pipes can be used to implement simple message passing protocols, such as sending fixed-size messages or using delimiters to separate messages.
- Pipes have some advantages and disadvantages compared to other IPC methods, such as sockets, message queues, or shared memory. Some of the advantages are:
  - Pipes are easy to use and require minimal system calls.
  - Pipes are portable across different operating systems and platforms.
  - Pipes can be used to create pipelines of commands or processes that process data sequentially.
- Some of the disadvantages are:
  - Pipes have limited capacity and can cause data loss or deadlock if not handled properly .
  - Pipes are unidirectional and require two pipes for bidirectional communication.
  - Pipes are not suitable for complex or structured data, such as objects or records.