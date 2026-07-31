 Here are the notes on Concepts in Message Passing Systems for the topic of Distributed Systems:

### Concepts in Message Passing Systems

1. Processes: Autonomous entities in a distributed system that can send and receive messages.
2. Messages: Packets of information exchanged between processes. They contain the destination address, sender address, and actual data or information.
3. Channels: The medium through which messages are exchanged between processes. They provide reliable and ordered delivery of messages.
4. Primitives: The basic operations of message passing like send, receive, etc. They are used to transmit messages between processes through channels.
5. Communications fabrics: The underlying infrastructure providing communication channels between processes. Examples are Ethernet, TCP/IP, etc.
6. Synchronicity: The manner in which send and receive primitives are executed. It can be asynchronous (send and receive are independent) or synchronous (send waits for receive to complete and vice-versa).
7. Buffering: The temporary storage of messages. Buffers are used when the sender and receiver are not synchronized. The messages are stored in the buffers until the receiving process is ready to receive them.
8. Rendezvous: A message passing concept where the sender and receiver have to be synchronized. The sender is blocked until the receiver is ready to receive the message.

The notes cover the major concepts involved in message passing for communication between processes in a distributed system. The concepts can be used to understand the working of any message passing system.