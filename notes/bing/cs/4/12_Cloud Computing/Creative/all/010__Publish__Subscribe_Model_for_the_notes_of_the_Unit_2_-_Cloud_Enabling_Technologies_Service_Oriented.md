### Publish, Subscribe Model for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing

- Publish, subscribe model, or pub/sub model, is a software architecture model by which applications create and share data.
- Pub/sub model is a form of asynchronous service-to-service communication used in serverless and microservices architectures.
- In pub/sub model, any message published to a topic is immediately received by all of the subscribers to the topic.
- Pub/sub model enables event-driven architectures and asynchronous parallel processing, while improving performance, reliability and scalability.
- Pub/sub model separates the publisher that sends the message from the subscriber that receives the message. The publisher and the subscriber do not need to establish direct contact.
- Pub/sub model introduces an asynchronous messaging subsystem that includes the following components:
  - An input messaging channel used by the publisher. The publisher packages events into messages, using a known message format, and sends these messages via the input channel.
  - A messaging engine that receives messages from the input channel, applies a set of rules to route the messages, and publishes the messages to one or more output channels. The messaging engine in this pattern is also called the broker.
  - One or more output messaging channels. Each output channel has a unique name that can be used by subscribers to identify it.
  - One or more subscribers that receive messages from an output channel. The subscriber in this pattern is also called the consumer.

- A simple ASCII diagram of the pub/sub model is shown below:

```
    Publisher 1  Publisher 2  Publisher 3
        |           |           |
        |           |           |
        v           v           v
    +---------------------------------+
    |          Input Channel         |
    +---------------------------------+
                  |
                  |
                  v
    +---------------------------------+
    |          Broker/Engine         |
    +---------------------------------+
                  |
                  |
                  v
    +---------------------------------+
    |        Output Channel 1        |
    +---------------------------------+
        |                   |
        |                   |
        v                   v
    Subscriber 1       Subscriber 2
```

- Some advantages of the pub/sub model are:
  - Decoupling: Publishers and subscribers are independent and do not need to know each other's identity, location, or implementation details.
  - Scalability: Publishers and subscribers can be added or removed dynamically without affecting the system functionality or performance.
  - Reliability: Publishers and subscribers can handle failures gracefully and resume communication when possible. Messages can be persisted and retried until they are delivered successfully.
  - Flexibility: Publishers and subscribers can use different message formats, protocols, and transport mechanisms as long as they adhere to the common interface defined by the broker.
  - Extensibility: Publishers and subscribers can be enhanced or replaced without impacting the rest of the system. New topics and channels can be created easily to support new business requirements or scenarios.

- Some disadvantages of the pub/sub model are:
  - Complexity: Publishers and subscribers need to coordinate with the broker and handle message serialization, deserialization, routing, filtering, and error handling. The broker also needs to manage the topics, channels, subscriptions, and message delivery policies.
  - Consistency: Publishers and subscribers may not have a consistent view of the system state due to the asynchronous and distributed nature of the communication. Messages may be delivered out of order, duplicated, or lost.
  - Security: Publishers and subscribers need to authenticate and authorize themselves with the broker and encrypt and decrypt the messages. The broker also needs to enforce access control and encryption policies for the topics, channels, and messages.

- Some examples of pub/sub model in cloud computing are :
  - Amazon Simple Notification Service (SNS): A fully managed pub/sub messaging service that enables you to decouple microservices, distributed systems, and serverless applications.
  - Google Cloud Pub/Sub: A scalable, reliable, and secure pub/sub messaging service that allows you to send and receive messages between independent applications.
  - Azure Service Bus: A fully managed enterprise integration message broker that supports pub/sub scenarios using topics and subscriptions.

- A possible mnemonic to remember the pub/sub model is:

```
Pub/sub is a model of communication
Where publishers send messages without hesitation
To topics that are managed by a broker
Who routes them to subscribers who are eager
To consume the messages asynchronously
And process them according to their logic
```