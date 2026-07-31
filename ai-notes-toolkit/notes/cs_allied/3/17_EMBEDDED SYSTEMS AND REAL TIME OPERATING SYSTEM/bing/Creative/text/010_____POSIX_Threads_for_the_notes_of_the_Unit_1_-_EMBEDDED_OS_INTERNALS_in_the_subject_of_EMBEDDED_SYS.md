### POSIX Threads

- POSIX Threads, or pthreads, is an **execution model** that allows a program to control multiple different flows of work that overlap in time .
- POSIX Threads is an **API** defined by the **IEEE** standard **POSIX.1c**, Threads extensions (IEEE Std 1003.1c-1995).
- A single process can contain multiple threads, all of which are executing the same program.
- The POSIX thread libraries are a standards based thread **API for C/C++**.
- POSIX threads are most effective on **multi-processor or multi-core systems** where the process flow can be scheduled to run on another processor thus gaining speed through parallel or distributed processing.
- POSIX threads provide the following features:
  - Thread management: creating, joining, detaching, and synchronizing threads.
  - Mutexes: locking mechanisms to prevent multiple threads from accessing the same data simultaneously.
  - Condition variables: signaling mechanisms to allow threads to communicate events or state changes.
  - Thread-specific data: a way for threads to have their own private data that is not shared with other threads.
  - Thread cancellation: a way for threads to terminate other threads.
  - Thread attributes: a way for threads to specify their properties, such as stack size, scheduling policy, and detach state.