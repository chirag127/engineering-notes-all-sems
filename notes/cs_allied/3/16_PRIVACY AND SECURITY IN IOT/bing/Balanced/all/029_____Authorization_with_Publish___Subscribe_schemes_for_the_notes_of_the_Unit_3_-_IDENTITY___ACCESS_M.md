# Authorization with Publish / Subscribe schemes for IoT

- Publish / Subscribe (Pub/Sub) is a communication paradigm that allows publishers to send messages to subscribers without knowing their identities or locations, and vice versa.
- Pub/Sub is suitable for large-scale and dynamic IoT systems, where devices need to exchange data efficiently and flexibly.
- However, Pub/Sub also poses some security and privacy challenges, such as data confidentiality, service privacy, and access control.
- Data confidentiality means that only authorized subscribers can access the messages published by publishers, and vice versa.
- Service privacy means that the identities and interests of publishers and subscribers are protected from unauthorized parties, such as brokers or adversaries.
- Access control means that publishers and subscribers can specify and enforce policies that define who can publish or subscribe to which topics.
- Authorization is the process of granting or denying access rights to publishers and subscribers based on their identities, attributes, or roles.
- Authorization schemes for Pub/Sub can be classified into two categories: centralized and decentralized.
- Centralized authorization schemes rely on a trusted authority or broker to manage and enforce the access policies for Pub/Sub. For example, AWS IoT Core provides a policy-based authorization mechanism for Pub/Sub over MQTT, HTTP, or WebSocket.
- Decentralized authorization schemes do not depend on a single authority or broker, but rather distribute the policy management and enforcement among the Pub/Sub participants. For example, blockchain-based Pub/Sub models use smart contracts to store and execute the access policies for Pub/Sub.