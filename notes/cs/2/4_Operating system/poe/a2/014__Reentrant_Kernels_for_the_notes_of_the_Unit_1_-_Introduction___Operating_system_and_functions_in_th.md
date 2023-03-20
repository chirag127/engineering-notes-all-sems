 Here is the content in markdown format without any emojis or external links:

### Reentrant Kernels for the notes of the Unit 1 - Introduction : Operating system and functions

1. A reentrant kernel is a kernel where multiple processes can make system calls to the kernel simultaneously without causing errors. This allows for greater throughput and responsiveness in the system.
2. Reentrancy is achieved by making kernel data structures and routines protected from simultaneous access. This is done using techniques like semaphores, monitors, and message passing.
3. The reentrant kernel handles context switches much more efficiently since it does not have to complete a system call for one process before beginning another. This results in a more interactive feel for the user.
4. Examples of reentrant kernels are found in modern operating systems like Linux, UNIX, and Windows NT. Earlier operating systems often used non-reentrant kernels which would only handle one system call at a time.
5. The reentrant kernel is more difficult to program but results in an overall more robust and efficient operating system. The extra complexity is worth the benefits in performance and multitasking capabilities.

The above content summarizes the key points regarding reentrant kernels in a formal tone with points and without any emojis or external links as per the given instructions. Let me know if you would like me to modify or expand the answer.