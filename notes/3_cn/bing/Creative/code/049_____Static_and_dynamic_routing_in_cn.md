Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write code for static and dynamic routing in computer networks. Here is my attempt:

### Static and dynamic routing in cn

Static routing is a method of configuring the routes in a network manually, by specifying the next hop address for each destination network. Static routing is simple, secure and efficient for small networks, but it does not adapt to network changes and requires a lot of administrative overhead for large networks.

Dynamic routing is a method of configuring the routes in a network automatically, by using routing protocols that exchange information about the network topology and the best paths to reach each destination network. Dynamic routing is scalable, adaptable and resilient for large networks, but it consumes more bandwidth, CPU and memory resources than static routing.

Here is an example of static routing code in Cisco IOS:

```
Router(config)# ip route 192.168.1.0 255.255.255.0 10.0.0.2
Router(config)# ip route 192.168.2.0 255.255.255.0 10.0.0.3
Router(config)# ip route 192.168.3.0 255.255.255.0 10.0.0.4
```

This code configures the router to forward packets destined for the networks 192.168.1.0/24, 192.168.2.0/24 and 192.168.3.0/24 to the next hop addresses 10.0.0.2, 10.0.0.3 and 10.0.0.4 respectively.

Here is an example of dynamic routing code in Cisco IOS:

```
Router(config)# router ospf 1
Router(config-router)# network 10.0.0.0 0.0.0.255 area 0
Router(config-router)# network 192.168.0.0 0.0.255.255 area 0
```

This code enables the Open Shortest Path First (OSPF) routing protocol on the router, and advertises the networks 10.0.0.0/24 and 192.168.0.0/16 to the other routers in the same area 0. The router will then learn the best routes to reach other networks from the OSPF updates.