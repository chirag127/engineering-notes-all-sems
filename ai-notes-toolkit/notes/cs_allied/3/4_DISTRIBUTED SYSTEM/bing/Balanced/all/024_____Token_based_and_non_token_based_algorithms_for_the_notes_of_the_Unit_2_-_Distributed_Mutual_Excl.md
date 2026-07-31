# Token based and non token based algorithms for distributed mutual exclusion

Distributed mutual exclusion (DME) is the problem of ensuring that only one process at a time can access a shared resource in a distributed system. There are two main approaches to solve this problem: token based and non token based algorithms.

## Token based algorithms

In token based algorithms, a unique token is shared among all the processes in the system. The token represents the permission to enter the critical section. A process can enter the critical section only if it has the token. The token is passed from one process to another according to some protocol.

Some examples of token based algorithms are:

- **Suzuki-Kasami algorithm**: This algorithm uses a token that contains a vector of sequence numbers, indicating the latest request of each process. The token is sent to the process with the highest sequence number in the vector. The process that has the token can enter the critical section multiple times without releasing the token, until it receives a higher request from another process.
- **Raymond's algorithm**: This algorithm organizes the processes in a logical tree structure. The token is initially held by the root of the tree. A process that wants to enter the critical section sends a request message to its parent in the tree. The parent forwards the request to the token holder, if it is not the token holder itself. The token holder sends the token to the requester along the path of the request messages. The process that has the token can enter the critical section and becomes the new root of the tree.

## Non token based algorithms

In non token based algorithms, a process communicates with a set of other processes to determine who should enter the critical section next. The communication is done using messages such as REQUEST, REPLY, and RELEASE. The processes use timestamps or logical clocks to order the requests and to resolve conflicts.

Some examples of non token based algorithms are:

- **Lamport's algorithm**: This algorithm uses logical clocks to assign timestamps to the requests. A process that wants to enter the critical section broadcasts a REQUEST message with its timestamp to all other processes. It waits for a REPLY message from each process, indicating that they have received the request and they are not in the critical section or have a higher priority request. The process with the smallest timestamp has the highest priority. After entering and exiting the critical section, the process broadcasts a RELEASE message to all other processes.
- **Ricart-Agrawala algorithm**: This algorithm is an improvement of Lamport's algorithm that reduces the number of messages. A process that wants to enter the critical section broadcasts a REQUEST message with its timestamp to all other processes. It waits for a REPLY message from each process that has a lower priority request or is not interested in the critical section. A process that has a higher priority request defers its REPLY until it exits the critical section or gives up its request. After entering and exiting the critical section, the process sends a REPLY message to all the deferred requests.