
### System models for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

Agreement protocols are used in distributed systems to ensure that all processes are in agreement on the order of events in the system. Agreement protocols are used to ensure that all processes agree on the same value or sequence of values. The following are the system models for agreement protocols:

1. **Two-Phase Commit Protocol**: This protocol is used to ensure that all processes agree on a single value. It involves two phases: the prepare phase and the commit phase. In the prepare phase, each process sends a request to the coordinator process. The coordinator then sends a response to each process indicating whether the request was accepted or rejected. In the commit phase, the coordinator sends a commit message to all processes, indicating that the agreement has been reached.

2. **Three-Phase Commit Protocol**: This protocol is similar to the two-phase commit protocol, but with an additional phase. In the additional phase, the coordinator sends a commit message to each process, indicating that the agreement has been reached.

3. **Byzantine Agreement Protocol**: This protocol is used to ensure that all processes agree on a single value in the presence of faulty processes. It involves multiple rounds of communication between the processes. The processes must come to agreement on the same value in order for the agreement to be successful.

4. **Consensus Protocol**: This protocol is used to ensure that all processes agree on the same sequence of values. It involves multiple rounds of communication between the processes. The processes must come to agreement on the same sequence of values in order for the agreement to be successful.

Mnemonics and Learning Tricks:

1. **Two-Phase Commit Protocol**: Think of the two phases as "prepare" and "commit".

2. **Three-Phase Commit Protocol**: Think of the three phases as "prepare", "commit", and "complete".

3. **Byzantine Agreement Protocol**: Think of the rounds of communication as "rounds of agreement".

4. **Consensus Protocol**: Think of the rounds of communication as "rounds of consensus".