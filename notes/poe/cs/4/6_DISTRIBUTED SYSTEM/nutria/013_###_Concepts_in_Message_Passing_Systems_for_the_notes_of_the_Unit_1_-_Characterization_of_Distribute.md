

# Concepts in Message Passing Systems for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

Message passing is a communication mechanism used in distributed systems to allow processes to communicate and synchronize with each other. It is a key component of distributed systems, as it allows processes to exchange information and coordinate their actions. 

Message passing systems can be divided into two categories: synchronous and asynchronous. Synchronous message passing systems require processes to wait for a response from the receiver before continuing, while asynchronous systems allow processes to continue without waiting for a response.

In synchronous message passing systems, messages are sent and received in a predefined order. The sender and receiver must agree on a protocol for sending and receiving messages, and the sender must wait for a response before continuing. This ensures that the sender and receiver are in sync, and that all messages are received in the correct order.

In asynchronous message passing systems, messages are sent and received in an unpredictable order. Processes can continue without waiting for a response, and messages may be received out of order. Asynchronous message passing systems are more efficient than synchronous systems, as they allow processes to continue without waiting for a response.

Message passing systems can also be classified based on the type of message being sent. Some common types of messages include control messages, data messages, and status messages. Control messages are used to control the behavior of processes, while data messages are used to exchange information. Status messages are used to report the current status of a process.

Mnemonics:

* **S**ynchronous **M**essage **P**assing **S**ystems
* **A**synchronous **M**essage **P**assing **S**ystems
* **C**ontrol **M**essages
* **D**ata **M**essages
* **S**tatus **M**essages