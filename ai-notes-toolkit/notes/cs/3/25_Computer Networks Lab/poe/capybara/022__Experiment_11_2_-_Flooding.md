### Experiment 11.2 - Flooding

In this experiment, we will learn about the Flooding technique in computer networking. Flooding is a simple and robust technique used for broadcasting messages in a network. The basic idea behind flooding is to forward a message to all the neighboring nodes in the network.

Here are the main points to keep in mind while learning about Flooding:

- Flooding is a broadcast technique that sends a message to all the nodes in a network.
- The message is forwarded to all of its neighboring nodes, and those nodes, in turn, forward the message to their neighbors.
- This process continues until all the nodes in the network have received the message.
- Flooding is a simple and robust technique, but it can lead to a lot of network traffic if the message is not controlled or limited.
- Flooding can be used for various applications such as routing, multicasting, and broadcasting.
- There are two types of flooding techniques: uncontrolled flooding and controlled flooding.
- In uncontrolled flooding, a message is forwarded to all the nodes in the network without any control, which can lead to network congestion and duplication of messages.
- In controlled flooding, the message is forwarded to all the nodes in the network, but with some control, such as setting a time-to-live (TTL) value, which limits the number of hops a message can take before being discarded.
- The TTL value ensures that the message does not circulate indefinitely in the network and avoids the creation of loops.
- Flooding can also be used in combination with other routing algorithms, such as Dijkstra's algorithm, to find the shortest path between two nodes in a network.

In conclusion, Flooding is a simple and robust technique used for broadcasting messages in a network. It can be used for various applications such as routing, multicasting, and broadcasting. However, it can lead to network congestion if not controlled properly. Controlled flooding, with the use of a TTL value, ensures that the message does not circulate indefinitely in the network and avoids the creation of loops.