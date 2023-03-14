 Here is the content in markdown format for the given topic:

### Centralized Deadlock Detection

For the notes of Unit 3 - Distributed Deadlock Detection in the subject of Distributed Systems:

- In a centralized deadlock detection, a dedicated server monitors the global state of all the processes in the system and detects if a deadlock has occurred.
- The server maintains a wait-for graph which tracks all the resource requests and holds by processes.
- If a cycle is detected in the wait-for graph, it indicates a deadlock. The server then initiates a recovery routine to resolve the deadlock.
- Advantages: Simple to implement. Only one component monitoring for deadlocks leading to low overhead.
- Disadvantages: The centralized server becomes a bottleneck and single point of failure. It has to keep track of a huge amount of global data leading to scalability issues.
- Mnemonics: Think of a prison warden (central server) monitoring all prisoners (processes) and their requests/holdings (wait-for graph) to detect if a riot (deadlock) may occur.
- Learning Trick: Draw diagrams depicting wait-for graphs in different conditions (with/without cycles) to visualize the deadlock detection process. This aids in understanding the concept better.

The above content summarizes the key points regarding centralized deadlock detection. Diagrams and examples can be included for further clarification if required. Please let me know if you would like me to modify or expand the answer.