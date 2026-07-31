### Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Deadlock avoidance is a technique that tries to prevent a deadlock from occurring by ensuring that the system is always in a safe state, where there is at least one possible sequence of resource allocation that does not lead to a deadlock .
- However, deadlock avoidance is impractical in distributed systems due to several problems, such as :
  - The lack of global information about the current state of the system and the future requests of the processes.
  - The high communication and synchronization overhead involved in maintaining and updating the global state.
  - The possibility of inconsistent and outdated information due to network delays and failures.
  - The difficulty of predicting the future behavior of the processes and the resources.
- Therefore, deadlock detection is preferred over deadlock avoidance in distributed systems, as it allows more concurrency and flexibility in resource allocation .
- Deadlock detection involves examining the status of the process-resource interactions for the presence of a cyclic wait, which indicates a deadlock .
- Deadlock detection algorithms in distributed systems can be classified into four categories :
  - Path-pushing algorithms, which propagate the information about the dependency paths along the wait-for graph.
  - Edge-chasing algorithms, which send probe messages along the dependency cycles in the wait-for graph.
  - Diffusion computation algorithms, which initiate a distributed computation at each node to detect a deadlock.
  - Global state detection algorithms, which collect the global state of the system and check for a deadlock using a centralized or distributed algorithm.