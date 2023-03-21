### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

In real-time communication systems, the network should be able to provide guaranteed Quality of Service (QoS) to meet the requirements of various applications. Priority-Based Service and Weighted Round-Robin Service disciplines are two important techniques used to provide QoS in switched networks. 

#### Priority-Based Service

Priority-Based Service is a scheduling technique where packets are prioritized based on their importance or urgency. The packets with higher priority are given preferential treatment over lower priority packets. This technique is used to ensure that packets with higher importance or urgency are transmitted without delay. 

##### Types of Priority-Based Service

1. **Strict Priority (SP)**: In this technique, packets with higher priority are always transmitted before lower priority packets. The lower priority packets are transmitted only after all the higher priority packets have been transmitted.

2. **Weighted Fair Queuing (WFQ)**: In this technique, each packet is assigned a weight based on its priority. The packets with higher weights are given more transmission time than packets with lower weights. This technique ensures that packets with higher priority are given more transmission time but does not completely ignore the lower priority packets.

#### Weighted Round-Robin Service

Weighted Round-Robin Service is a scheduling technique where packets are transmitted in a cyclic order. Each packet is assigned a weight based on its priority, and the transmission time of each packet is proportional to its weight. This technique ensures that packets with higher priority are given more transmission time than packets with lower priority. 

##### Types of Weighted Round-Robin Service

1. **Weighted Round-Robin (WRR)**: In this technique, each packet is assigned a weight based on its priority. The packets with higher weights are given more transmission time than packets with lower weights. The transmission time of each packet is proportional to its weight.

2. **Weighted Fair Queuing Round-Robin (WFQRR)**: In this technique, each packet is assigned a weight based on its priority. The packets are transmitted in a cyclic order, and the transmission time of each packet is proportional to its weight. This technique ensures that packets with higher priority are given more transmission time but does not completely ignore the lower priority packets.

In conclusion, Priority-Based Service and Weighted Round-Robin Service disciplines are important techniques used to provide Quality of Service in switched networks. These techniques ensure that packets with higher importance or urgency are given preferential treatment and are transmitted without delay.