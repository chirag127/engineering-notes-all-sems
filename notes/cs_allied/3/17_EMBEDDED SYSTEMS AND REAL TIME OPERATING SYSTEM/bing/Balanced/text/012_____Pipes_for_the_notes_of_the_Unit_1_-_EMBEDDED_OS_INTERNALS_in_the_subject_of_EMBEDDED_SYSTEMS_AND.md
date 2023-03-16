### Pipes

- Pipes are a form of inter-process communication (IPC) that allow data to be transferred between two or more processes in a sequential manner.
- Pipes are often used in embedded systems, where memory and CPU resources are limited, and tasks need to communicate efficiently and reliably.
- Pipes have two ends: a read end and a write end. Data written to the write end can be read from the read end in a first-in first-out (FIFO) order.
- Pipes can be either named or unnamed. Named pipes have a file name and can be accessed by any process that knows the name. Unnamed pipes are created by the system call `pipe` and can only be accessed by the parent process and its children .
- Pipes can be either blocking or non-blocking. Blocking pipes wait until there is data available to read or write, while non-blocking pipes return immediately with an error code if there is no data available.
- Pipes can be used to implement simple message passing, filtering, redirection, and synchronization between processes.
- Pipes have some limitations, such as fixed size, unidirectional flow, and lack of error detection.
- Pipes can be combined with other IPC methods, such as message queues, mailboxes, and sockets, to achieve more complex and robust communication .