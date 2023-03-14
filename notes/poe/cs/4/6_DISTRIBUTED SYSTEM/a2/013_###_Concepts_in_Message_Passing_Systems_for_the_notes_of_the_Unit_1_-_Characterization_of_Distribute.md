 Here is the content in markdown format:

### Concepts in Message Passing Systems for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Messages: Messages are the means of communication between processes in a message passing system. They contain data being exchanged between processes.
- Channels: Channels provide the medium through which messages are exchanged between processes. They are unidirectional and can be either send only or receive only. Bidirectional channels allow processes to both send and receive messages.
- Send/Receive Primitives: These primitives are used by processes to send and receive messages through channels. The sending process uses the send primitive to send messages while the receiving process uses the receive primitive to receive messages.
- Synchronization: Message passing provides a mechanism for synchronization between processes. The send and receive primitives can be blocking or non-blocking. Blocking primitives suspend the execution of a process until the message is sent/received. This enforces synchronization between the participating processes. Non-blocking primitives, on the other hand, allow processes to continue execution even if a message cannot be sent/received immediately.
- References/Pointers: Messages can contain references/pointers to data rather than containing the actual data. This is more efficient if large amounts of data need to be exchanged. The receiving process can then access the data using the references/pointers received in the message.
- Advantages:
    - Decouples processes and provides modularity
    - Supports heterogeneous systems and dynamic process creation/deletion
    - Provides a convenient means of synchronization
- Disadvantages:
    - Extra overhead for message transmission/reception
    - Message ordering issues if FIFO channels are not used
    - Difficult to implement
- Applications: Scientific simulations, telecommunications systems, etc.