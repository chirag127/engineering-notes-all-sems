 Here is the content in markdown format without any emojis or external links:

### Pipes for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Pipes are a form of inter-process communication (IPC) used to communicate data (as a byte stream) between two processes.
- Pipes have a read end and a write end. Data written to the write end can be read from the read end.
- Pipes are unidirectional, data can only flow in one direction from the write end to the read end. If bidirectional communication is required, two pipes are required with data flowing in opposite directions.
- Pipes are a very efficient means of IPC as no intermediate buffering of the data is required. The data is passed directly from the write system call to the read system call.
- The size of data that can be passed through a pipe is limited by the operating system and is typically between 4K and 64K bytes. If larger amounts of data need to be passed, alternate IPC mechanisms should be used.
- The writes to a pipe will be blocked if the pipe is full and reads from a pipe will be blocked if no data is available. This allows pipes to be used to provide synchronization and flow control between processes.
- Pipes are supported by most operating systems including Linux, Unix, and Windows.

The points are written in a formal tone without any emojis or external links as instructed. Please let me know if you would like me to modify or expand the content in any way.