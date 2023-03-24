### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

In a switched network, different types of services can be offered to the users. The two commonly used service disciplines for switched networks are Priority-Based Service and Weighted Round-Robin Service.

#### Priority-Based Service

Priority-Based Service is a service discipline that gives priority to certain types of traffic over others. In Priority-Based Service, traffic is classified into different priority levels, and each priority level is assigned a specific amount of resources (such as bandwidth) that it can use.

The highest priority traffic is given the highest amount of resources, and lower priority traffic is given less resources. This ensures that high-priority traffic always gets the resources it needs, even if there is congestion on the network.

#### Weighted Round-Robin Service

Weighted Round-Robin Service is a service discipline that shares the network resources among different types of traffic in a proportional manner. In Weighted Round-Robin Service, each type of traffic is assigned a weight, which represents the proportion of resources it should get.

During each round, the network allocates resources to each type of traffic based on its weight. The traffic is served in a round-robin fashion, with each type of traffic getting a turn to use the resources. The amount of resources allocated to each type of traffic depends on its weight.

Weighted Round-Robin Service is useful when there are multiple types of traffic that need to be serviced, but none of them have a higher priority than the others. By assigning weights to each type of traffic, the network can ensure that each type of traffic gets a fair share of the resources.

#### Comparison between Priority-Based Service and Weighted Round-Robin Service

Both Priority-Based Service and Weighted Round-Robin Service are useful service disciplines for switched networks. However, they differ in how they allocate resources to the different types of traffic.

Priority-Based Service is useful when there are certain types of traffic that have a higher priority than others. By giving high-priority traffic more resources, the network can ensure that it always gets the resources it needs.

Weighted Round-Robin Service is useful when there are multiple types of traffic that need to be serviced, but none of them have a higher priority than the others. By assigning weights to each type of traffic, the network can ensure that each type of traffic gets a fair share of the resources.

In summary, the choice of service discipline depends on the specific requirements of the network and the types of traffic that need to be serviced. Priority-Based Service is useful when there are certain types of traffic that require higher priority, while Weighted Round-Robin Service is useful when there are multiple types of traffic that require fair allocation of resources.