### Token based and non token based algorithms for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

Distributed mutual exclusion is the process of ensuring that concurrent processes in a distributed system do not access a shared resource simultaneously, which can lead to inconsistencies and errors. There are two main types of algorithms used to achieve this - token based and non-token based algorithms. Let's take a look at each of them in detail:

#### Token based algorithms
Token based algorithms are based on the concept of a token, which is passed around between processes in the system. The process that holds the token is the only one that is allowed to access the shared resource, while other processes have to wait until they receive the token. Once a process has finished using the resource, it releases the token and passes it on to the next process in line.

Some of the key features of token based algorithms are:

- The token is passed around in a predefined order, which ensures that each process gets a chance to access the resource in a fair manner.
- The token passing process can be centralized or distributed, depending on the design of the algorithm.
- Token based algorithms are generally simpler to implement than non-token based algorithms, as they rely on a single token to control access to the resource.

Some of the most commonly used token based algorithms are:

- Ricart-Agrawala algorithm
- Maekawa's algorithm
- Suzuki-Kasami algorithm

#### Non-token based algorithms
Non-token based algorithms do not rely on a token to control access to the shared resource. Instead, they use various techniques such as timestamps, logical clocks, or voting to determine which process is allowed to access the resource at any given time. The main advantage of non-token based algorithms is that they are more flexible and can be adapted to different scenarios and resource types.

Some of the key features of non-token based algorithms are:

- They do not rely on a single token to control access to the resource, which makes them more robust in case of failures or network partitions.
- Non-token based algorithms can be more complex to implement than token based algorithms, as they require additional mechanisms to coordinate access to the resource.
- Non-token based algorithms can be classified into two main categories - voting-based and timestamp-based algorithms.

Some of the most commonly used non-token based algorithms are:

- Lamport's logical clock algorithm
- Berkeley algorithm
- N-Chooses-K algorithm

In conclusion, both token based and non-token based algorithms are used to achieve distributed mutual exclusion in a distributed system. The choice of which algorithm to use depends on various factors such as the type of resource being shared, the level of fault tolerance required, and the complexity of the system. It is important to understand the strengths and weaknesses of each algorithm in order to choose the best one for a given scenario.