 Here is the content in markdown format for the topic ### global state for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM:

### Global State

- The global state of a distributed system is the combination of the states of all the processes in the system at a given instant of time.
- It is difficult to capture the global state of a distributed system because:
    - The states of the individual processes may be changing concurrently.
    - The message delays may be unpredictable.
    - It is difficult to simultaneously capture the local states of all the processes.
- However, the knowledge of the global state is useful for:
    - Debugging and error recovery.
    - Proving correctness of algorithms.
    - Analyzing performance of algorithms.
- Some possible ways to capture the global state are:
    - Take snapshots of the local states of all processes at precisely the same instant of time. This is difficult to achieve in practice due to lack of synchronized clocks and unpredictable delays.
    - Log the events and messages in the system and later analyze the logs to construct the global state. However, the size of logs may become very large for long-running systems.

- Mnemonic: The global veggie state is a combo of states of all processes. It's hard to capture due to concurrent changes and delays. But useful for debugging and analysis. Snapshots or logs can capture global state.

- The key points to remember are:
1. Global state is the combination of states of all processes in the system.
2. It is difficult to capture the global state due to concurrency, unpredictability and difficulty in simultaneously capturing local states.
3. Knowledge of global state is useful for debugging, proof of correctness and analysis.
4. Possible ways to capture global state: snapshots or logging events and messages.