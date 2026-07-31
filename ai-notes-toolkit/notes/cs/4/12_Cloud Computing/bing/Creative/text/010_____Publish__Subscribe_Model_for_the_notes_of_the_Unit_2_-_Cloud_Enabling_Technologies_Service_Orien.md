### Publish, Subscribe Model

- Publish, subscribe model, or pub/sub model, is a software architecture model by which applications create and share data.
- Pub/sub model is a form of asynchronous service-to-service communication used in serverless and microservices architectures.
- In pub/sub model, any message published to a topic is immediately received by all of the subscribers to the topic.
- Pub/sub model enables event-driven architectures and asynchronous parallel processing, while improving performance, reliability and scalability.
- Pub/sub model separates the publisher that sends the message from the subscriber that receives the message. The publisher and the subscriber do not need to establish direct contact.
- Pub/sub model introduces an asynchronous messaging subsystem that includes the following components:
  - An input messaging channel used by the publisher to send messages using a known message format.
  - A message queue that stores the messages sent by the publisher until they are consumed by the subscribers.
  - A topic that acts as a logical grouping of messages based on a common theme or interest.
  - One or more output messaging channels used by the subscribers to receive messages from the topic.
  - A subscription that defines the criteria for selecting messages from the topic and delivering them to the output channel.
- Pub/sub model has the following benefits:
  - Decoupling: Publishers and subscribers are independent and do not need to know each other's identity, location, or implementation details.
  - Scalability: Publishers and subscribers can scale independently and handle variable workloads by adding or removing instances as needed.
  - Resiliency: Publishers and subscribers can tolerate failures and recover from them without losing messages or affecting each other's availability.
  - Flexibility: Publishers and subscribers can dynamically subscribe or unsubscribe to topics and change their message processing logic without affecting the system.
  - Extensibility: Publishers and subscribers can easily integrate with other services and systems by using standard protocols and formats.