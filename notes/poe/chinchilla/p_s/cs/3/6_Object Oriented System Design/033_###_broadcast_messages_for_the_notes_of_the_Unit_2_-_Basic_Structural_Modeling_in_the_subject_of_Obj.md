### Broadcast Messages for the Notes of the Unit 2 - Basic Structural Modeling in the Subject of Object Oriented System Design

In the Unit 2 of Object Oriented System Design, we will be discussing the concept of Basic Structural Modeling. One of the key aspects of this topic is Broadcast Messages. In this section, we will dive deeper into Broadcast Messages, their advantages, disadvantages, examples, and applications.

#### What are Broadcast Messages?

In Object Oriented System Design, Broadcast Messages are messages that are sent by an object to all the objects that have subscribed to it. These messages are not targeted at any specific object, but rather are broadcasted to all the objects that are interested in receiving them. 

#### Advantages of Broadcast Messages

- Broadcast Messages are an efficient way to notify multiple objects of an event or change in state.
- They help in achieving loose coupling between objects as they do not depend on a specific object to receive the message.
- They facilitate the implementation of event-driven systems where multiple objects need to react to a single event.

#### Disadvantages of Broadcast Messages

- Broadcast Messages can result in a lot of unnecessary processing if not used judiciously.
- They can lead to performance issues if a large number of objects are subscribed to them.
- They can make the system more complex if not used properly.

#### Examples of Broadcast Messages

Consider a scenario where a stock price changes. In this case, multiple objects such as the stock market ticker, watchlist, and portfolio need to be updated. Broadcast Messages can be used to efficiently notify all these objects of the price change.

#### Applications of Broadcast Messages

- Event-driven systems such as GUI applications, network systems, and multimedia systems.
- Systems that require real-time notifications such as stock market systems, weather forecasting systems, and traffic management systems.

In conclusion, Broadcast Messages are an important concept in Object Oriented System Design, especially in the context of Basic Structural Modeling. They provide an efficient way to notify multiple objects of an event or change in state and facilitate loose coupling between objects. However, they need to be used judiciously to avoid unnecessary processing and system complexity.