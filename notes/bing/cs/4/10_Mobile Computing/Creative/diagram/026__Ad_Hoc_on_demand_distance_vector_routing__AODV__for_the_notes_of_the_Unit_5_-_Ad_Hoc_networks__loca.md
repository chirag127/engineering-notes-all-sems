The following is a detailed ASCII diagram for Ad Hoc on demand distance vector routing (AODV) for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing.

AODV is a reactive routing protocol that establishes routes on demand between nodes in an ad hoc network. It uses control messages such as route requests (RREQs), route replies (RREPs), route errors (RERRs), and hello messages to discover and maintain routes. AODV uses sequence numbers to ensure loop-free and fresh routes. AODV also supports multicast routing using multicast route requests (MRREQs), multicast route replies (MRREPs), and multicast route error (MRERRs) messages.

The diagram below shows an example of AODV routing in an ad hoc network with six nodes (A, B, C, D, E, and F). The arrows indicate the direction of data packets and control messages. The numbers indicate the sequence numbers of the nodes.

```
    A(1)  B(2)  C(3)  D(4)  E(5)  F(6)
    |     |     |     |     |     |
    |     |     |     |     |     |
    |     |     |     |     |     |
    |     |     |     |     |     |
    |     |     |     |     |     |
    |     |     |     |     |     |
    |     |     |     |     |     |
    |     |     |     |     |     |
    |     |     |     |     |     |
    |     |     |     |     |     |
    +-----+-----+-----+-----+-----+
    |     |     |     |     |     |
    |     |     |     |     |     |
    |     |     |     |     |     |
    |     |     |     |     |     |
    |     |     |     |     |     |

    A wants to send data to F, but does not have a route to F.

    A broadcasts a RREQ with its own address, sequence number, and a broadcast ID.

    RREQ(A, 1, 1) --> B, C, D, E

    B, C, D, and E receive the RREQ and update their routing tables with the reverse route to A.

    B, C, D, and E forward the RREQ to their neighbors, except A.

    RREQ(A, 1, 1) --> F (from B and E)

    F receives the RREQ and updates its routing table with the reverse route to A.

    F unicasts a RREP with its own address, sequence number, and the hop count to A.

    RREP(F, 6, 1) --> E

    E receives the RREP and updates its routing table with the forward route to F.

    E forwards the RREP to A.

    RREP(F, 6, 2) --> B

    B receives the RREP and updates its routing table with the forward route to F.

    B forwards the RREP to A.

    RREP(F, 6, 3) --> A

    A receives the RREP and updates its routing table with the forward route to F.

    A sends data to F using the route A-B-F.

    DATA(A, F) --> B --> F

    F sends an acknowledgment to A using the route F-B-A.

    ACK(F, A) --> B --> A

    The routing tables of the nodes are as follows:

    A: | Destination | Next Hop | Hop Count | Sequence Number |
       | F           | B        | 3         | 6               |

    B: | Destination | Next Hop | Hop Count | Sequence Number |
       | A           | A        | 1         | 1               |
       | F           | F        | 1         | 6               |

    C: | Destination | Next Hop | Hop Count | Sequence Number |
       | A           | A        | 1         | 1               |

    D: | Destination | Next Hop | Hop Count | Sequence Number |
       | A           | A        | 1         | 1               |

    E: | Destination | Next Hop | Hop Count | Sequence Number |
       | A           | A        | 1         | 1