### Publish, Subscribe Model

- Publish, subscribe model, or pub/sub model, is a software architecture model by which applications create and share data.
- Pub/sub model is a form of asynchronous service-to-service communication used in serverless and microservices architectures.
- In pub/sub model, any message published to a topic is immediately received by all of the subscribers to the topic.
- Pub/sub model separates the publisher that sends the message from the subscriber that receives the message. The publisher and the subscriber do not need to establish direct contact.
- Pub/sub model enables event-driven architectures and asynchronous parallel processing, while improving performance, reliability and scalability.
- Pub/sub model introduces an asynchronous messaging subsystem that includes the following components:
  - An input messaging channel used by the publisher. The publisher packages events into messages, using a known message format, and sends these messages via the input channel.
  - A messaging engine that receives the messages from the input channel and routes them to one or more output channels based on the topic of the message.
  - One or more output messaging channels used by the subscribers. The subscribers register their interest in a topic and receive the messages that match that topic from the output channel.
  - Optionally, a message store that persists the messages for later delivery or auditing purposes.
- Pub/sub model has the following benefits:
  - Decoupling: Publishers and subscribers are independent and do not need to know each other's identity, location, or implementation details.
  - Scalability: Publishers and subscribers can scale independently and handle variable workloads. Multiple subscribers can consume the same message in parallel.
  - Reliability: Publishers and subscribers can handle failures gracefully and resume communication when possible. Messages can be stored and retried until they are delivered or expired.
  - Flexibility: Publishers and subscribers can dynamically join or leave the system without affecting each other. New topics can be created or deleted as needed.