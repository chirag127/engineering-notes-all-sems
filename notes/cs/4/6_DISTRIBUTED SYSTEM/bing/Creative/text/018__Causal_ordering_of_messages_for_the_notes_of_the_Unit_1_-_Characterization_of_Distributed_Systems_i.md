### Causal ordering of messages

- Causal ordering of messages is a partial ordering of messages in a distributed computing environment. It places a restriction on communication between processes by requiring that if the transmission of message mi to process pk necessarily preceded the transmission of message mj to the same process, then the delivery of these messages to that process must be ordered such that mi is delivered before mj .
- Causal ordering of messages is one of the four semantics of multicast communication, namely unordered, totally ordered, causal, and sync-ordered communication. Multicast communication methods vary according to the message’s reliability guarantee and ordering guarantee .
- The causal ordering of messages describes the causal relationship between a message send event and a message receive event. For example, if send (M1) -> send (M2) then every recipient of both the messages M1 and M2 must receive the message M1 before receiving the message M2 .
- In distributed systems, the causal ordering of messages is not automatically guaranteed. Reasons that may lead to violation of causal ordering of messages are:
  - Transmission delay
  - Congestion in the network
  - Failure of a system 
- Protocols that are used to provide causal ordering of messages are:
  - Birman Schipher Stephenson Protocol
  - Schipher Eggli Sandoz Protocol
  - The ISIS System 
- The general idea of these protocols is to deliver a message to a process only if the message immediately preceding it has been delivered to the process. Otherwise, the message is not delivered immediately instead it is stored in a buffer memory until the message preceding it has been delivered .
- The ISIS system is a framework for reliable distributed communication which is achieved through the help of process groups. It is a programming toolkit whose basic features consist of process group management calls and ordered multicast primitives for communicating with the process group members. ISIS provides multicast facilities such as unordered multicast (FBCAST), casually ordered multicast (CBCAST), totally ordered multicast (ABCAST), and sync-ordered multicast (GBCAST) .
- ISIS uses vector timestamps to implement causally ordered multicast between the members of a process group. It is assumed that all the messages are multicast to all the members of the group including the sender. ISIS uses UDP/IP protocol as its basic transport facility and sends acknowledgments and retransmits packets as necessary to achieve reliability. Messages from a given member are sequenced and delivered in order .
- Causal ordering of messages is useful for reasoning about causality in a distributed system, since sending messages is the only way for machines to affect each other. If not (A -> B) then A cannot possibly have caused B .