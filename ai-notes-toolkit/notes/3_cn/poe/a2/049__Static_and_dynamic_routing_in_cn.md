 Here is the content in markdown format with formal tone and without any emojis or external links:

### Static and dynamic routing in cn

1. Static routing: In static routing, the routes are determined prior to the start of the communication between sender and receiver. The path is determined based on the network topology and the sender needs to specify the complete path with the network addresses of all intermediate routers in the path. It is simple to implement but not scalable since the routes are fixed.
2. Dynamic routing: In dynamic routing, the routes are determined dynamically based on the current network conditions. The sender only specifies the destination address and the routers determine the best path based on routing algorithms and routing tables which are updated dynamically. It is scalable but complex to implement.
3. Advantages of dynamic routing:
- Better resource utilization as the traffic can be routed dynamically around network issues or congested routes.
- Scalable as the routers determine the routes dynamically based on the current network state. The network topology can change but the routing takes place efficiently without any manual intervention.
- Redundancy can be included to provide backup routes in case of path failures. The routers can reroute the traffic to the backup paths.
4. Disadvantages of dynamic routing:
- Complex to implement and maintain due to the use of sophisticated routing algorithms and protocols.
- The routing tables in each router need to be updated dynamically leading to extra overhead on the routers.
- The convergence time needed to propagate routing changes across the network can be high leading to latency.

The content summarizes the key points around static and dynamic routing in a formal tone with points and without any emojis or external links as per the given instructions. Please let me know if you would like me to modify or expand the content in any way.