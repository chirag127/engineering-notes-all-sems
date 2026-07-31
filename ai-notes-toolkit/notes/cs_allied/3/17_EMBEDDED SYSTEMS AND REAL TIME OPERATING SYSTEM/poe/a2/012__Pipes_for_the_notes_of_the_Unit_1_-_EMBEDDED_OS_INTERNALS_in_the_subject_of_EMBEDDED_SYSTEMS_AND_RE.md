 Here are the points on Pipes for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM:

### Pipes

- Pipes are a mechanism for inter-process communication (IPC) in Linux.
- A pipe is a connection between two processes through which data can be streamed in both directions.
- Pipes are created using `pipe()` system call. It returns two file descriptors, a read end and a write end of the pipe.
- The write end of a pipe can be used to write data to the pipe, and the read end can be used to read data from the pipe.
- Data written to the write end of a pipe is buffered until it is read from the read end.
- Pipes are unidirectional, data can only be transferred in one direction. If bidirectional communication is required, two pipes are required.
- Pipes are an efficient means of IPC as the kernel buffers the data, and no intermediate buffer is required in user space.
- The size of data that can be passed through a pipe is limited by the pipe buffer size. If the pipe is filled before the reader can drain it, the writer will get blocked.
- Pipes are suitable for transferring small amounts of data between related processes.

The above points are written in a formal tone without any emojis or external links as requested. The content is written in Markdown format with headings and points. Let me know if you would like me to elaborate on any of the points or modify the content in any way.