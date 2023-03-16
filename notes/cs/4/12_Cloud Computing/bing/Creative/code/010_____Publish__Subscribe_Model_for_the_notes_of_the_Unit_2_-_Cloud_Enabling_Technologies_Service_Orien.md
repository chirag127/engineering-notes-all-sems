### Publish, Subscribe Model

- Publish, subscribe model, or pub/sub model, is a software architecture model by which applications create and share data  .
- Pub/sub model is an asynchronous service-to-service communication method used in serverless and microservices architectures .
- Pub/sub model enables event-driven architectures and asynchronous parallel processing, while improving performance, reliability and scalability .
- Pub/sub model separates the client (publisher) that sends the message from the client (subscriber) that receives the message. The publisher and the subscriber do not need to establish direct contact.
- Pub/sub model involves:
  - A publisher who sends a message.
  - A topic that categorizes the message.
  - A subscriber who expresses interest in a topic and receives the message.
  - A broker or a messaging system that manages the topics and delivers the messages from publishers to subscribers .
- Pub/sub model has the following benefits:
  - Decoupling: Publishers and subscribers are independent and do not need to know each other's identity, location, or implementation details  .
  - Scalability: Publishers and subscribers can be added or removed dynamically without affecting the system  .
  - Flexibility: Publishers and subscribers can communicate across different platforms, languages, and protocols  .
  - Reliability: Publishers and subscribers can handle failures gracefully and resume communication when the system recovers  .
  - Performance: Publishers and subscribers can process messages in parallel and asynchronously, reducing latency and increasing throughput  .