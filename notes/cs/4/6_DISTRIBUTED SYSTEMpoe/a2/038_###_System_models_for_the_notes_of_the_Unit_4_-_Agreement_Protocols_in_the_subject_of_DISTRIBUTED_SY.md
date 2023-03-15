 Here is the content in markdown format:

### System models for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- System models classify distributed systems based on assumptions made about the communication medium and the degree of cooperation among components. The models help in analyzing the complexity of different problems and the kinds of algorithms that can be designed.
- The major system models are:
-- Shared memory model: Components can access shared memory. The system appears as a tightly-coupled system. Problems like mutual exclusion can be solved.
-- Message passing model: Components communicate by exchanging messages. The system appears as a loosely-coupled system. Problems like agreement and consensus become harder to solve.
-- Crash-recovery model: Components may crash and later recover. The system must be fault-tolerant. Problems like consensus become even harder in the presence of crashes.
- Mnemonics: Think of 'S' for shared memory, 'M' for message passing and 'C' for crash-recovery to remember the system models.
- Advantages: The system models help analyze system complexity and guide algorithms. They assist in identifying what can/cannot be solved.
- Disadvantages: The models are idealizations. Real systems may not strictly follow any one model and can exhibit aspects of multiple models, making analysis harder.
- Examples: Database systems follow the shared memory model. Communication networks follow the message passing model. Fault-tolerant systems follow the crash-recovery model.
- Applications: The models drive the design of distributed algorithms and protocols. They help determine what kinds of problems can have solutions and the difficulties in solving them. This impacts system scalability and robustness.