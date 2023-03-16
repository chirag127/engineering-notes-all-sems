### Centralized Deadlock Detection

Centralized deadlock detection is a technique used in distributed database systems to handle deadlock detection. In this approach, the system maintains one global wait-for graph in a single chosen site, which is named as the deadlock-detection coordinator .

There are two techniques used in the centralized approach of deadlock detection: the Completely Centralized Algorithm and the Ho Ramamurthy Algorithm (One phase and Two-phase) .

#### Completely Centralized Algorithm
In a network of n sites, one site is chosen as a control site. This site is responsible for deadlock detection .

#### Ho Ramamurthy Algorithm
This algorithm uses only two levels: Master control nodes and Cluster control nodes. Cluster control nodes are used for detecting deadlock among their members and reporting dependencies outside their cluster to the Master control node .

#### Central Coordinator
A centralized deadlock detection approach uses a central coordinator to manage a resource graph of processes and the resources they are using. Each time a process gets a lock or releases a lock on a resource, it sends a message to this coordinator (waiting-for or releasing) .