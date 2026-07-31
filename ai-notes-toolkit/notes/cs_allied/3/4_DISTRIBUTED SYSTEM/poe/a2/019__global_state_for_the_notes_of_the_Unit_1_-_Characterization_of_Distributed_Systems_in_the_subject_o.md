 Here is the markdown content on the topic "global state for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM":

### Global State

- In a distributed system, there is no single shared memory. Each process has its own local state.
- Global state: A collection of local states of all processes in the system. It is difficult to capture the global state of a distributed system at a particular instant of time due to the independent local states of processes and absence of synchronized clocks.
- The global state is useful for:
    - Debugging and fault diagnosis.
    - Determining if a distributed system is functioning correctly.
    - Coordinating actions of different processes.
- Methods to capture global state:
    - Centralized approach: Select a single process to collect local states of other processes. Difficult to implement in distributed systems.
    - Distributed approach: Each process sends its local state to other processes. Needs synchronization and leads to high message overhead.
    - Log-based approach: Each process logs its state transitions. Global state can be constructed by combining logs. Needs clock synchronization and leads to large log sizes.
- In practice, capturing instantaneous global states is infeasible. Instead, causally related events are used to partially order events and deduce some global properties.

The above content is written in a formal tone with points and without any emojis or external links as per the given instructions. The markdown formatting is used and the content is written inside the specified header. Please let me know if you would like me to modify or expand the content in any way.