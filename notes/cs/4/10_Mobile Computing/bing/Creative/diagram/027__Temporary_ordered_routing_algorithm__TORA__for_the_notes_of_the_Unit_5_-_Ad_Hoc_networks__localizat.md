The following is a detailed ASCII diagram for Temporary ordered routing algorithm (TORA) for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing.

### Temporary ordered routing algorithm (TORA)

TORA is a source-initiated on-demand routing protocol that builds and maintains a directed acyclic graph (DAG) rooted at a destination. Each node has a height metric that determines the direction of data flow. TORA uses three basic functions: route creation, route maintenance, and route erasure. The diagram below illustrates the basic operation of TORA.

```
    A            B            C            D            E
    |            |            |            |            |
    |            |            |            |            |
    |            |            |            |            |
    |            |            |            |            |
    |            |            |            |            |
    |            |            |            |            |
    |            |            |            |            |
    |            |            |            |            |
    |            |            |            |            |
    |            |            |            |            |
    |            |            |            |            |
    |            |            |            |            |
    +------------+------------+------------+------------+
    |            |            |            |            |
    |            |            |            |            |
    |            |            |            |            |
    F            G            H            I            J
    |            |            |            |            |
    |            |            |            |            |
    |            |            |            |            |
    +------------+------------+------------+------------+
    |            |            |            |            |
    |            |            |            |            |
    |            |            |            |            |
    K            L            M            N            O
    |            |            |            |            |
    |            |            |            |            |
    |            |            |            |            |
    +------------+------------+------------+------------+
    |            |            |            |            |
    |            |            |            |            |
    |            |            |            |            |
    P            Q            R            S            T
    |            |            |            |            |
    |            |            |            |            |
    |            |            |            |            |
    +------------+------------+------------+------------+
    |            |            |            |            |
    |            |            |            |            |
    |            |            |            |            |
    U            V            W            X            Y
    |            |            |            |            |
    |            |            |            |            |
    |            |            |            |            |
    +------------+------------+------------+------------+
    |            |            |            |            |
    |            |            |            |            |
    |            |            |            |            |
    Z            AA           AB           AC           AD
```

Suppose node A wants to send data to node AD. Node A broadcasts a query (QRY) packet containing the destination ID (AD) to its neighbors. Node B receives the QRY packet and forwards it to its neighbors. Node C receives the QRY packet and forwards it to its neighbors. Node D receives the QRY packet and forwards it to its neighbors. Node E receives the QRY packet and forwards it to its neighbors. Node J receives the QRY packet and forwards it to its neighbors. Node I receives the QRY packet and forwards it to its neighbors. Node H receives the QRY packet and forwards it to its neighbors. Node G receives the QRY packet and forwards it to its neighbors. Node F receives the QRY packet and forwards it to its neighbors. Node K receives the QRY packet and forwards it to its neighbors. Node L receives the QRY packet and forwards it to its neighbors. Node M receives the QRY packet and forwards it to its neighbors. Node N receives the QRY packet and forwards it to its neighbors. Node O receives the QRY packet and forwards it to its neighbors. Node T receives the QRY packet and forwards it to its neighbors. Node S receives the QRY packet and forwards it to its neighbors. Node R receives the QRY packet and forwards it to its neighbors. Node Q receives the QRY packet and forwards it to its neighbors. Node P receives the QRY packet and forwards it to its neighbors. Node U receives the Q