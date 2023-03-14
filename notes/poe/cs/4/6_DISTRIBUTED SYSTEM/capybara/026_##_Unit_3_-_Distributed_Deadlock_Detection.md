## Unit 3 - Distributed Deadlock Detection

Deadlock is a situation in which two or more processes are blocked indefinitely, waiting for each other to release resources. Deadlocks can occur in distributed systems as well as in centralized systems. Distributed deadlock detection is the process of detecting deadlocks in distributed systems. In this unit, we will learn about distributed deadlock detection and the various techniques used to detect deadlocks in distributed systems.

### Types of Deadlocks

Before we dive into distributed deadlock detection, let's first understand the different types of deadlocks:

1. **Deadlock**: This is a situation in which two or more processes are blocked indefinitely, waiting for each other to release resources.

2. **Starvation**: This is a situation in which a process is blocked indefinitely, waiting for a resource that is never released.

3. **Livelock**: This is a situation in which two or more processes keep changing their states in response to the states of other processes, but none of them make progress.

### Techniques for Distributed Deadlock Detection

There are two main techniques used for distributed deadlock detection:

1. **Centralized Algorithm**: In this technique, a central server maintains a global resource allocation graph and a global wait-for graph. The central server periodically checks for deadlocks in the system using these graphs. If a deadlock is detected, the central server takes appropriate action to resolve it.

2. **Distributed Algorithm**: In this technique, each node in the system maintains a local resource allocation graph and a local wait-for graph. The nodes periodically exchange messages to update their graphs and detect deadlocks. If a deadlock is detected, the nodes take appropriate action to resolve it.

### Advantages of Distributed Deadlock Detection

1. Distributed deadlock detection can be more efficient than centralized deadlock detection, as it avoids the need for a central server to maintain global graphs.

2. Distributed deadlock detection is more fault-tolerant than centralized deadlock detection, as a failure of the central server does not affect the ability of the nodes to detect deadlocks.

### Disadvantages of Distributed Deadlock Detection

1. Distributed deadlock detection can be more complex than centralized deadlock detection, as it requires nodes to exchange messages and coordinate with each other.

2. Distributed deadlock detection can be less accurate than centralized deadlock detection, as each node only has a local view of the system.

### Mnemonic for Distributed Deadlock Detection

One possible mnemonic for distributed deadlock detection is "D3", which stands for "Distributed Deadlock Detection". This can be helpful in remembering the topic and its abbreviation.