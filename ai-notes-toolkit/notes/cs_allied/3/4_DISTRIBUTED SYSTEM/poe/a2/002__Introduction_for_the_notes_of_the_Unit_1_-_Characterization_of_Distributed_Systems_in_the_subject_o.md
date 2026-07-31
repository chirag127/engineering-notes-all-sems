 Here are the notes in formal markdown format without any emojis or external links:

### Introduction for the notes of the Unit 1 - Characterization of Distributed Systems

1. A distributed system is a system whose components are located on different networked computers, which communicate and coordinate their actions by passing messages to one another.

2. The components interact with one another in order to achieve a common goal.

3. The key properties of distributed systems are:

- Concurrency: Components of a distributed system execute concurrently.
- Lack of a global clock: There is no way to synchronize the clocks of all the components precisely.
- Independent failure: Components can fail independently, and the system as a whole must continue to function.
- Unreliable communication: The network connections between components are not reliable and might drop or reorder messages.
4. Advantages of distributed systems:

- Increased resource sharing: Making multiple resources available increases availability and efficiency.
- Increased reliability: The distributed system as a whole continues to function even if some components have failed.
- Scalability: It is possible to increase resources by adding more machines or nodes, allowing the system to handle larger loads.
- Locality of components: Having components close to the resources or users that they serve can reduce latency.

5. Challenges in designing distributed systems:

- Difficulty of building robust software due to asynchrony and concurrency
- Dealing with partial failures since detecting and recovering from failures is difficult
- Managing unreliable communication channels and ensuring consistency across nodes
- Performance issues like latency, throughput, and scalability
- Security issues since there are multiple less-trusted nodes