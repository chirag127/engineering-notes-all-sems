### Internet and Resource Reservation Protocols

- Resource Reservation Protocol (RSVP) is a network-control protocol that enables Internet applications to obtain different qualities of service (QoS) for their data flows    .
- RSVP operates over IPv4 or IPv6 and provides receiver-initiated setup of resource reservations for multicast or unicast data flows.
- RSVP is used in real-time systems for efficient quality band transmission to a particular receiver. It is generally used by the receiver side for the fast delivery of the transmission packets from the sender to the receiver.
- RSVP supports the following features     :
  - Application-adaptive QoS: RSVP enables applications to specify their QoS requirements and adapt to the network conditions.
  - Dynamic resource allocation: RSVP allows the network to allocate and deallocate resources according to the changing traffic demands and network conditions.
  - Policy control: RSVP enables the network to enforce policies for resource allocation and admission control based on the identity and priority of the users and applications.
  - Scalability: RSVP uses soft state and aggregation techniques to reduce the overhead and complexity of maintaining resource reservations in large and dynamic networks.
  - Heterogeneity: RSVP supports different types of QoS models, such as the integrated services model and the differentiated services model, and can interoperate with various routing protocols and network technologies.
- RSVP uses the following messages to establish and maintain resource reservations     :
  - PATH: Sent by the sender to inform the intermediate nodes and the receiver about the characteristics and requirements of the data flow.
  - RESV: Sent by the receiver to request a specific QoS from the intermediate nodes and the sender for the data flow.
  - PATH TEAR: Sent by the sender to tear down the PATH state in the intermediate nodes and the receiver when the data flow is terminated or modified.
  - RESV TEAR: Sent by the receiver to tear down the RESV state in the intermediate nodes and the sender when the data flow is terminated or modified.
  - PATH ERROR: Sent by an intermediate node or the receiver to report an error in processing a PATH message or receiving a data flow.
  - RESV ERROR: Sent by an intermediate node or the sender to report an error in processing a RESV message or providing a QoS for a data flow.
  - RESV CONF: Sent by an intermediate node or the sender to confirm the successful processing of a RESV message and the provision of a QoS for a data flow.