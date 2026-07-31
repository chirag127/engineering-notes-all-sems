### Static and dynamic routing in computer networks

- Static routing and dynamic routing are two methods used to determine how to send a packet toward its destination.
- Static routes are configured in advance of any network communication by the network administrator. Dynamic routes are learned by routers through exchanging information with other routers.
- Static routing is suitable for small networks with one or two routes, while dynamic routing is more efficient for large and complex networks with multiple routes.
- Static routing provides more security and control over the network traffic, while dynamic routing adapts to network changes and failures automatically.
- Static routing uses less bandwidth and CPU resources, while dynamic routing uses more bandwidth and CPU resources to exchange routing information.
- Static routing is manual and static, while dynamic routing is automated and dynamic.

#### Advantages and disadvantages of static routing

- Advantages:
  - It is simple and easy to configure.
  - It provides more security and control over the network traffic.
  - It uses less bandwidth and CPU resources than dynamic routing.
  - It is faster and more reliable than dynamic routing.
- Disadvantages:
  - It is not scalable and flexible for large and complex networks.
  - It does not adapt to network changes and failures automatically.
  - It requires manual reconfiguration of routes when the network topology changes.
  - It is prone to human errors and misconfigurations.

#### Advantages and disadvantages of dynamic routing

- Advantages:
  - It is scalable and flexible for large and complex networks.
  - It adapts to network changes and failures automatically.
  - It does not require manual reconfiguration of routes when the network topology changes.
  - It can balance the network load and optimize the network performance.
- Disadvantages:
  - It is complex and difficult to configure and troubleshoot.
  - It provides less security and control over the network traffic.
  - It uses more bandwidth and CPU resources than static routing.
  - It is slower and less reliable than static routing.

#### Examples of static and dynamic routing

- Static routing example:

  - Suppose there are three routers R1, R2, and R3 connected as shown below:

```
    R1 ----- R2 ----- R3
    |        |        |
    |        |        |
    A        B        C
```

  - To configure static routes on R1, the network administrator needs to enter the following commands:

```
    R1(config)# ip route 192.168.2.0 255.255.255.0 10.0.0.2
    R1(config)# ip route 192.168.3.0 255.255.255.0 10.0.0.2
```

  - These commands tell R1 to send packets destined for network 192.168.2.0/24 and 192.168.3.0/24 to the next-hop router R2 with IP address 10.0.0.2.
  - Similarly, the network administrator needs to configure static routes on R2 and R3 for the other networks.

- Dynamic routing example:

  - Suppose there are three routers R1, R2, and R3 connected as shown above, and they use the Routing Information Protocol (RIP) as the dynamic routing protocol.
  - To configure dynamic routes on R1, the network administrator needs to enter the following commands:

```
    R1(config)# router rip
    R1(config-router)# network 10.0.0.0
    R1(config-router)# network 192.168.1.0
```

  - These commands tell R1 to enable RIP on the interfaces that belong to network 10.0.0.0/24 and 192.168.1.0/24, and to advertise these networks to other routers.
  - Similarly, the network administrator needs to configure dynamic routes on R2 and R3 for the other networks.
  - After the configuration, the routers will exchange routing information periodically and update their routing tables accordingly.