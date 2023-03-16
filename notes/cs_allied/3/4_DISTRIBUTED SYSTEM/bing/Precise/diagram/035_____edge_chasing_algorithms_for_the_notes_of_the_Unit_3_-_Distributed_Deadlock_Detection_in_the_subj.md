# Unit 3 - Distributed Deadlock Detection

## Edge Chasing Algorithms

- Edge chasing algorithm is the implementation of Chandy-Misra-Haas’s algorithm for AND request model and it is useful in detecting deadlock in a distributed Systems.
- This algorithm makes use of a unique message on every occasion, impasse detection is initiated by process Pi and it’s triplet being sent by means of site of process Pi to site of process Pk.
- In edge chasing algorithm, a special message called probe is used in deadlock detection.
- A probe is a triplet (i, j, k) which denotes that process Pi has initiated the deadlock detection and the message is being sent by the home site of process Pj to the home site of process Pk.
- Distributed deadlock detection algorithms can be divided into four classes: path-pushing, edge-chasing, diffusion computation, and global state detection.