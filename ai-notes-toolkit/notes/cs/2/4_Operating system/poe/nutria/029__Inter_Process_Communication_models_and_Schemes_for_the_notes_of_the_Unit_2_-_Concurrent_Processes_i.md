
### Inter Process Communication models and Schemes
* Message Passing: This model involves two or more processes exchanging messages with one another. Processes can send messages to each other, which are stored in a buffer until they are received by the other process.
* Shared Memory: This model involves two or more processes sharing a common memory space. Each process can read and write to the shared memory, allowing them to communicate with one another.
* Remote Procedure Call (RPC): This model involves two or more processes calling a procedure on a remote machine. The procedure is executed on the remote machine and the results are sent back to the calling process.
* Synchronization: This model involves two or more processes synchronizing their execution with each other. Processes can be synchronized using semaphores, locks, and other synchronization primitives.
* Signals: This model involves two or more processes sending signals to each other. Signals are used to notify processes of certain events, such as an interrupt or a system call.