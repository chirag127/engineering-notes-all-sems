# Publish, Subscribe Model

- Publish, subscribe model, or pub/sub model, is a software architecture model by which applications create and share data.
- Pub/sub model is a form of asynchronous service-to-service communication used in serverless and microservices architectures.
- Pub/sub model enables event-driven architectures and asynchronous parallel processing, while improving performance, reliability and scalability.
- Pub/sub model separates the client (publisher) that sends the message from the client (subscriber) that receives the message. The publisher and the subscriber do not need to establish direct contact.
- Pub/sub model involves:
  - A publisher who sends a message to a topic.
  - A topic which is a logical channel that groups messages by subject or type.
  - A subscriber who receives the message from the topic.
  - A message broker or a messaging service that manages the topics and delivers the messages to the subscribers.
- Pub/sub model has the following benefits:
  - Decoupling: Publishers and subscribers are independent and do not need to know each other's identity, location, or implementation details.
  - Scalability: Pub/sub model can handle high volumes of messages and subscribers without affecting the performance of the publishers.
  - Reliability: Pub/sub model ensures that messages are delivered to the subscribers even if the publishers or the message broker fail or become unavailable.
  - Flexibility: Pub/sub model allows subscribers to dynamically subscribe or unsubscribe to topics based on their interest or availability.
  - Extensibility: Pub/sub model enables new publishers and subscribers to join or leave the system without affecting the existing ones.