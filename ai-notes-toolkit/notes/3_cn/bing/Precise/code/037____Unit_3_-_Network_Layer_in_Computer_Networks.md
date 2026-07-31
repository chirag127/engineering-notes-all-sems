## Unit 3 - Network Layer in Computer Networks

The network layer is responsible for routing data packets from the source to the destination. This layer is responsible for logical addressing and routing. The network layer uses routing algorithms to determine the best path for data packets to take from the source to the destination.

Here is an example of a simple routing algorithm in Python:

```python
def route_packet(source, destination, network_graph):
    # Use a shortest path algorithm to find the best path
    best_path = shortest_path(network_graph, source, destination)
    # Forward the packet along the best path
    forward_packet(packet, best_path)
```

This code uses a shortest path algorithm to determine the best path for a packet to take from the source to the destination. The packet is then forwarded along this path. This is just one example of how routing can be implemented at the network layer. There are many other routing algorithms and techniques that can be used.