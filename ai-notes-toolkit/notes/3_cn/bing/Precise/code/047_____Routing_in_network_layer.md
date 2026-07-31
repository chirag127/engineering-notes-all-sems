### Routing in network layer

Routing is the process of selecting a path for traffic in a network or between or across multiple networks. The network layer is responsible for routing packets from the source to the destination. Here is an example of a routing algorithm in Python:

```python
def dijkstra(graph, start, end):
    shortest_paths = {start: (None, 0)}
    current_node = start
    visited = set()
    
    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    path = path[::-1]
    return path
```
This is an implementation of Dijkstra's algorithm, which is used to find the shortest path between nodes in a graph. It can be used for routing in a network by representing the network as a graph, where nodes are devices and edges are connections between them. The weights on the edges represent the cost of transmitting data along that connection, such as the distance or the amount of traffic. The algorithm finds the path with the lowest total cost from the source to the destination.