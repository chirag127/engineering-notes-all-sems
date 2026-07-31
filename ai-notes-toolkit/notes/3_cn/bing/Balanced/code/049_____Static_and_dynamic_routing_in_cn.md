### Static and dynamic routing in cn

Static routing and dynamic routing are two methods used to determine how to send a packet toward its destination. Static routes are configured in advance of any network communication. Dynamic routing, on the other hand, requires routers to exchange information with other routers to learn about paths through the network.

Static routing is manual, meaning that a network administrator has to add entries into the routing table for each destination network. Static routing provides high security, as the administrator can control the traffic flow and avoid unwanted routes. Static routing is also simple and easy to implement in small networks. However, static routing is not scalable, as it becomes difficult to maintain and update the routing table in large networks. Static routing also does not adapt to network changes, such as link failures or congestion .

Dynamic routing is automated, meaning that routers use complex routing algorithms to discover the best routes for each destination network. Dynamic routing provides less security, as the routers may exchange information with untrusted routers or expose their routing information to attackers. Dynamic routing is also more complex and requires more resources, such as CPU, memory and bandwidth, to run the routing protocols. However, dynamic routing is scalable, as it can handle large networks with many routers and destinations. Dynamic routing also adapts to network changes, as it can update the routing table dynamically and find alternative routes in case of link failures or congestion .

Some examples of dynamic routing protocols are OSPF, EIGRP, RIP, IS-IS and BGP. These protocols use different metrics, such as hop count, bandwidth, delay, cost and reliability, to calculate the best routes. They also use different methods, such as distance vector, link state and path vector, to exchange routing information with other routers.

To add a static route, use the following command in the global configuration mode:

```bash
ip route destination_network mask {next_hop_address | exit_interface}
```

As you can see, the command is pretty simple. You need to specify the destination network address, its mask and the address of the next hop or the exit interface toward the destination.