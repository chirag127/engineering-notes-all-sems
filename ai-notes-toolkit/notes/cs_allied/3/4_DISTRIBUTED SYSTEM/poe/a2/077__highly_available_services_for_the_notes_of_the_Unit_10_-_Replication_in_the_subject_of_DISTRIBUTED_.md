 Here is the content in markdown format without any emojis or external links:

### Highly Available Services

1. Load Balancers: Load balancers distribute client requests across a group of servers. This increases availability as requests are handled by multiple servers, so if one goes down, others can still serve requests.
2. Application Layer Gateways: These sit in front of application servers and route requests to available healthy servers. They detect server failures and remove failed servers from routing. This increases availability.
3. Replication: Data and services are replicated across multiple servers. If one server fails, others can continue providing the service. This relies on replication being fast enough to keep copies in sync, and requires mechanisms to update replicas sequentially or handle conflicts.
4. N+1 Redundancy: Critical components such as servers are designed with extra (N+1) capacity so that if one fails, the others can handle the load. The extra capacity acts as a backup. This guards against single points of failure to increase availability.
5. Heartbeat Monitoring: Servers or services continually check (heartbeat) that critical components are still functioning (or "alive"). If a failure is detected, recovery actions can be taken to restore the service. This can involve restarting a server or reconfiguring a load balancer. Heartbeats must be fast enough to minimize downtime.

The points are written in a formal tone with headers and points, without emojis or external links, in markdown format as requested. Please let me know if you would like me to modify or expand the content in any way.