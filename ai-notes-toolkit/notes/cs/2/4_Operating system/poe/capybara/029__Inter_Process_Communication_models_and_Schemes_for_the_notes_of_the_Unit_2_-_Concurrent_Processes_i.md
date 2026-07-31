### Inter Process Communication models and Schemes

Inter Process Communication (IPC) refers to the exchange of data or information between two or more processes running on a computer system. It is an essential aspect of concurrent processes in the subject of Operating Systems. Here are some of the common IPC models and schemes:

1. Message Passing: In this model, processes communicate with each other by sending and receiving messages. It can be implemented in either a synchronous or asynchronous manner. Synchronous message passing requires the sender to wait for the recipient to receive the message, while asynchronous message passing allows the sender to continue its execution without waiting for the recipient.

2. Shared Memory: In this scheme, processes communicate by accessing a shared memory region. Any process can read or write to the shared memory space. It requires proper synchronization mechanisms to avoid race conditions and inconsistencies.

3. Pipes: Pipes are a type of communication channel between two related processes. It can be implemented as a unidirectional or bidirectional channel. In a unidirectional pipe, data flows in one direction, while in a bidirectional pipe, data can flow in both directions.

4. Remote Procedure Calls (RPCs): RPCs allow a process to call a procedure or function that is located in a different process or machine. The calling process sends a request message to the remote process, which executes the procedure and sends a response message back to the calling process.

5. Sockets: Sockets are a type of communication endpoint that allows processes to communicate over a network. It can be implemented using TCP or UDP protocol. TCP provides reliable and ordered data transmission, while UDP provides unreliable and unordered data transmission.

In conclusion, understanding the different IPC models and schemes is crucial for developing efficient and robust concurrent processes in Operating Systems.