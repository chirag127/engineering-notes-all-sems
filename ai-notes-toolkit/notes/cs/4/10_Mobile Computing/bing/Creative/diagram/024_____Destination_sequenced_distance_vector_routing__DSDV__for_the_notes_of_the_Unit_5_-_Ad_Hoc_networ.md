Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some information on the topic of Destination sequenced distance vector routing (DSDV) for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing.

### Destination sequenced distance vector routing (DSDV)

- DSDV is a table-driven routing scheme for ad hoc mobile networks based on the Bellman–Ford algorithm.
- It was developed by C. Perkins and P. Bhagwat in 1994.
- The main contribution of the algorithm was to solve the routing loop problem.
- DSDV adds a new attribute, sequence number, to each route table entry of the conventional RIP.
- Using the sequence number, the mobile nodes can distinguish stale route information from the new and thus prevent the formation of routing loops.
- DSDV provides only one route for a source/destination pair.
- DSDV requires each node to periodically broadcast routing updates.
- DSDV uses bidirectional links.
- DSDV has two types of routing updates: full dump and incremental.
- Full dump updates contain all the routing information of a node and are sent infrequently.
- Incremental updates contain only the changed routing information and are sent more frequently.
- DSDV reduces the number of control messages by using triggered updates, which are sent only when there is a significant change in the topology.
- DSDV also uses a settling time, which is the time before a node advertises a route update, to reduce the network overhead.
- DSDV is suitable for small and moderately sized networks with low mobility.
- DSDV suffers from the problems of high overhead, slow convergence, and wastage of bandwidth.