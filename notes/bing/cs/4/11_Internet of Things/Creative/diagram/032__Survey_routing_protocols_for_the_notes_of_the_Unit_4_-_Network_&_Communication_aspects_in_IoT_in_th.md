The following is a detailed ASCII diagram for survey routing protocols for the notes of the Unit 4 - Network & Communication aspects in IoT in the subject of Internet of Things. The diagram is based on the information from the search results     .

The diagram shows six routing protocols in IoT: RPL, CTP, LOADng, CORPL, CARP, and E-CARP. RPL is the most commonly used one and it is a distance vector protocol designed by IETF in 2012. CTP is a distance-vector routing algorithm that was developed as a solution to routing in WSNs. It stands as a predecessor to RPL and was considered the de-facto routing standard for Tiny OS. The Lightweight on-demand ad hoc distance-vector routing protocol-next generation or LOADng is a lightweight variation of AODV for LLNs. It is designed based on the idea that LLNs are idle most of the time. Hence instead of adopting a proactive approach would generate unnecessary overhead, CORPL is a non-standard extension of RPL that is designed for cognitive networks and utilizes the opportunistic forwarding to forward packets at each hop. On the other hand, CARP and E-CARP is the only distributed hop based routing protocol that is designed for IoT sensor network applications. CARP and E-CARP is used for underwater communication mostly. Since it is not standardized and just proposed in literature, it is not yet used in other IoT applications.

The diagram also shows the network layer in two sub layers: routing layer which handles the transfer the packets from source to destination, and an encapsulation layer that forms the packets. Encapsulation mechanisms will be out of scope of this paper.

The diagram uses the following symbols:

- S: Source node
- D: Destination node
- R: Router node
- C: Cognitive node
- U: Underwater node
- E: Encapsulation layer
- ->: Unidirectional link
- <->: Bidirectional link
- |: Vertical line
- -: Horizontal line
- +: Junction point
- /: Diagonal line
- \: Diagonal line
- (: Left parenthesis
- ): Right parenthesis
- [: Left bracket
- ]: Right bracket
- {: Left brace
- }: Right brace
- <: Less than sign
- >: Greater than sign
- ^: Caret sign
- v: Lowercase v
- *: Asterisk

The diagram is as follows:

```
+---------------------+---------------------+---------------------+
|                     |                     |                     |
|        RPL          |         CTP         |       LOADng        |
|                     |                     |                     |
+---------------------+---------------------+---------------------+
|                     |                     |                     |
| S -> R -> R -> R -> D                     | S -> R -> R -> R -> D
|                     |                     |                     |
|                     | S -> R -> R -> R -> D                     |
|                     |                     |                     |
|                     |                     |                     |
+---------------------+---------------------+---------------------+
|                     |                     |                     |
|       CORPL         |        CARP         |       E-CARP        |
|                     |                     |                     |
+---------------------+---------------------+---------------------+
|                     |                     |                     |
| S -> C -> C -> C -> D                     | S -> U -> U -> U -> D
|                     |                     |                     |
|                     | S -> U -> U -> U -> D                     |
|                     |                     |                     |
|                     |                     |                     |
+---------------------+---------------------+---------------------+
|                     |                     |                     |
|    Encapsulation    |    Encapsulation    |    Encapsulation    |
|       Layer         |       Layer         |       Layer         |
|                     |                     |                     |
+---------------------+---------------------+---------------------+
```