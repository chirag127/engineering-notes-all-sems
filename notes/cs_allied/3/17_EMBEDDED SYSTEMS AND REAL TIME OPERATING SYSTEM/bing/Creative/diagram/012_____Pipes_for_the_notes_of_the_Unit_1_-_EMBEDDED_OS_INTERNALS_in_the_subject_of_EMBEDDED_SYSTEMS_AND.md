### Pipes

- Pipes are a form of inter-process communication (IPC) that allow data to be transferred between two or more processes in a sequential manner.
- Pipes are often used in embedded systems to pass simple messages between tasks, such as sensor readings, commands, or status updates .
- Pipes have two ends: a read end and a write end. Data written to the write end can be read from the read end in a first-in first-out (FIFO) order .
- Pipes can be either named or unnamed. Named pipes have a file name and can be accessed by any process that knows the name. Unnamed pipes are created by the system call `pipe` and are only accessible by the processes that created them or their descendants .
- Pipes can be either blocking or non-blocking. Blocking pipes wait until data is available to be read or written, while non-blocking pipes return immediately with an error code if data is not available .
- Pipes have some advantages and disadvantages compared to other IPC methods. Some advantages are:
  - Pipes are simple and easy to use, requiring only standard file operations such as `read` and `write` .
  - Pipes are portable and widely supported by various operating systems and programming languages .
  - Pipes can be used to create pipelines of commands or processes that process data in stages .
- Some disadvantages are:
  - Pipes are unidirectional, meaning data can only flow in one direction. To achieve bidirectional communication, two pipes are needed .
  - Pipes have limited buffer size and capacity, which can cause data loss or deadlock if the producer and consumer are not synchronized  .
  - Pipes are not suitable for complex or structured data, as they only transfer bytes without any interpretation or formatting .