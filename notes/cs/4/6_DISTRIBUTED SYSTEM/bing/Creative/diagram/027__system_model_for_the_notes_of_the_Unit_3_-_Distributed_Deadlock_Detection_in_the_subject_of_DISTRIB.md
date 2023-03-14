The following is a detailed ASCII diagram for the system model for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM.

The system model assumes that the distributed system consists of a set of processors that are connected by a communication network. The communication delay is finite but unpredictable. The system has only reusable resources, and processes are allowed only exclusive access to resources. There is only one copy of each resource. The system model is based on the wait-for graph (WFG), which is a directed graph that represents the resource requests and holds among processes. A node in the WFG is a process, and an edge from process P to process Q means that P is waiting for a resource held by Q. A cycle in the WFG indicates a deadlock.

The ASCII diagram is as follows:

```
+-----------------+     +-----------------+     +-----------------+
| Processor 1     |     | Processor 2     |     | Processor 3     |
|                 |     |                 |     |                 |
| +-------------+ |     | +-------------+ |     | +-------------+ |
| | Process P1  | |     | | Process P2  | |     | | Process P3  | |
| +-------------+ |     | +-------------+ |     | +-------------+ |
| | Resource R1 | |     | | Resource R2 | |     | | Resource R3 | |
| +-------------+ |     | +-------------+ |     | +-------------+ |
+-----------------+     +-----------------+     +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       +---------------------->+                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       +---------------------->+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       +----------------------------------------------->+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       +<----------------------------------------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       +<----------------------+                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       +----------------------------------------------->+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |

```

The diagram shows a WFG with three processes (P1, P2, P3) and three resources (R1, R2, R3) distributed among three processors. The edges indicate the requests and holds of resources. For example, P1 holds R1 and requests R2, P2 holds R2 and requests R3, and P3 holds R3 and requests R1. The WFG has a cycle (P1 -> P2 -> P3 -> P1), which means that the system is in a deadlock state.