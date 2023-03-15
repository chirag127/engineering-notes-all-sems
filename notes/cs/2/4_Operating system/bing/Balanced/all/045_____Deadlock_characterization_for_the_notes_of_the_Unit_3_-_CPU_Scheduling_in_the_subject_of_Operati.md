Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content on the topic of deadlock characterization for the notes of the unit 3 - CPU scheduling in the subject of operating system.

# Deadlock Characterization

- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- A deadlock can be characterized by four necessary conditions that must hold simultaneously in a system:
  - **Mutual exclusion**: At least one resource must be held in a non-sharable mode; that is, only one process can use the resource at a time.
  - **Hold and wait**: A process must be holding at least one resource and waiting to acquire additional resources that are currently being held by other processes.
  - **No preemption**: A resource can be released only voluntarily by the process holding it, after that process has completed its task.
  - **Circular wait**: A set of processes must exist such that each process in the set is waiting for a resource that is held by another process in the set.
- These four conditions are necessary and sufficient for a deadlock to occur. If one of these conditions is false, then the system is not in a deadlock state.