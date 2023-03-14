The following is a possible ASCII diagram for the application of agreement problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM. The diagram is based on the Byzantine Agreement Problem, which is a type of agreement problem where some processors may behave arbitrarily and maliciously. The diagram shows how seven processors (P1 to P7) can reach an agreement on a binary value (0 or 1) proposed by a source processor (P1) in four rounds of message passing, despite the presence of two faulty processors (P2 and P5) that may send inconsistent or forged messages. The diagram also shows the messages sent and received by each processor, the values they decide on, and the witnesses they have for each value. The diagram assumes that the processors use authenticated messages, which means that they can verify the identity and content of the sender. The diagram is adapted from the lecture slides of the Indian Institute of Information Technology .

The diagram uses the following symbols and notations:

- P1 to P7: the processors in the system
- F: the faulty processors (P2 and P5)
- S: the source processor (P1)
- *: the value proposed by the source processor (1)
- Pn: the name of a processor that sent or received a message
- Wn: the set of witnesses for a message received by processor n
- Dn: the value decided by processor n
- ->: the direction of message passing
- |: the separation of rounds
- /: the separation of processors

The diagram is as follows:

```
P1 (S)  P2 (F)  P3      P4      P5 (F)  P6      P7
|       |       |       |       |       |       |
* ->    * ->    * ->    * ->    * ->    * ->    * ->    Round 1: The source processor broadcasts the value *
|       |       |       |       |       |       |
*       0       *       *       0       *       *       D1 = * (decided)   D2 = 0 (decided)
|       |       |       |       |       |       |
P1 ->   P1 ->   P1 ->   P1 ->   P1 ->   P1 ->   P1 ->    Round 2: The processors that received * from the source broadcast the name of the sender
|       |       |       |       |       |       |
P1      P1      P1      P1      P1      P1      P1       W1 = {P1}         W2 = {P1}
|       |       |       |       |       |       |
P2 ->   P2 ->   P2 ->   P2 ->   P2 ->   P2 ->   P2 ->    Round 3: The faulty processor P2 broadcasts its own name
|       |       |       |       |       |       |
P2      P2      P2      P2      P2      P2      P2       W1 = {P1, P2}     W2 = {P1, P2}
|       |       |       |       |       |       |
P3 ->   P3 ->   P3 ->   P3 ->   P3 ->   P3 ->   P3 ->    Round 3: The processor P3 broadcasts its own name
|       |       |       |       |       |       |
P3      P3      P3      P3      P3      P3      P3       W1 = {P1, P2, P3} W2 = {P1, P2, P3}
|       |       |       |       |       |       |
P4 ->   P4 ->   P4 ->   P4 ->   P4 ->   P4 ->   P4 ->    Round 3: The processor P4 broadcasts its own name
|       |       |       |       |       |       |
P4      P4      P4      P4      P4      P4      P4       W1 = {P1, P2, P3, P4} W2 = {P1, P2, P3, P4}
|       |       |       |       |       |       |
P5 ->   P5 ->   P5 ->   P5 ->   P5 ->   P5 ->   P5