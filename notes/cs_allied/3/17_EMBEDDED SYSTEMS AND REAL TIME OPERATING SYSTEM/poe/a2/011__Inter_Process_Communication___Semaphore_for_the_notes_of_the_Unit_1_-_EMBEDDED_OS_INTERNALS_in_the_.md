 Here are the notes on Inter Process Communication – Semaphore for the topic EMBEDDED OS INTERNALS:

### Inter Process Communication – Semaphore

- Semaphore is a variable which is used to control access to a common resource by multiple processes in a concurrent system like embedded operating system.
- It basically limits the number of processes that can access the shared resource at a time.
- Two operations on semaphore:
	- P(): Decrements the semaphore value. If the value is less than 0 after decrement, the process is blocked.
	- V(): Increments the semaphore value and wakes up a blocked process (if any).
- Binary semaphore: Can have only two values – 0 and 1. Used to lock a resource.
- Counting semaphore: Can have any non-negative integer value. Used to control the number of resources of a particular type.
- Semaphores help avoid race conditions and ensure mutual exclusion and synchronization between processes.
- They are useful for solving critical section problems and for protecting shared data structures from being corrupted.

The notes are written in points and in a formal tone without any emojis or external links as per the given instructions. The content is written inside header tags and in Markdown format. Please let me know if you would like me to modify or expand the notes in any way.