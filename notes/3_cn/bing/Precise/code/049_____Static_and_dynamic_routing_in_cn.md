### Static and dynamic routing in cn

Static routing is a type of routing that is manually configured by a network administrator. The administrator creates a routing table that specifies the path for each destination network. This type of routing is suitable for small networks, where the network topology is simple and does not change frequently.

On the other hand, dynamic routing is a type of routing that is automatically configured by routing protocols. The routing protocols exchange information about the network topology and calculate the best path for each destination network. This type of routing is suitable for large networks, where the network topology is complex and changes frequently.

Here is an example of how to configure static routing on a Cisco router:

```
Router(config)# ip route [destination network] [subnet mask] [next-hop address or exit interface]
```

And here is an example of how to configure dynamic routing using the OSPF routing protocol on a Cisco router:

```
Router(config)# router ospf [process ID]
Router(config-router)# network [network address] [wildcard mask] area [area ID]
```