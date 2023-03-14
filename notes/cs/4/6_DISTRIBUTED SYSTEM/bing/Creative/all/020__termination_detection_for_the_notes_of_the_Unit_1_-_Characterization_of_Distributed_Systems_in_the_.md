### Termination detection for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

Termination detection is a fundamental problem in distributed systems, where the goal is to determine if a distributed computation has terminated. A distributed computation is globally terminated if every process is locally terminated and there are no messages in transit between any processes. A process is locally terminated if it has finished its computation and will not restart any action unless it receives a message. A message is in transit if it has been sent by a process but not yet received by another process.

There are different algorithms for termination detection, depending on the assumptions and requirements of the system. One of the algorithms is Huang's algorithm, which was proposed by Shing-Tsaan Huang in 1989. Huang's algorithm is based on the following assumptions:

- There is a logical bidirectional communication channel between every pair of processes.
- Communication channels are reliable but non-FIFO.
- Message delay is arbitrary but finite.
- One of the cooperating processes, called the controlling agent, monitors the computation and initiates the termination detection.
- The initial weight of the controlling agent is 1 and the initial weight of all other processes is 0.
- The computation starts when the controlling agent sends a computation message to one of the processes.
- A computation message can be sent only by the controlling agent or an active process.
- A control message is sent to the controlling agent by an active process when it becomes idle.
- The algorithm assigns a weight W (such that 0 < W < 1) to every active process and every in transit message.

The main idea of Huang's algorithm is to split and transfer the weight of the controlling agent to the processes and messages involved in the computation, and to collect the weight back to the controlling agent when the processes become idle and the messages are delivered. The computation is terminated when the controlling agent regains its initial weight of 1.

The algorithm consists of the following rules:

- Rule to send B (DW): Suppose process P with weight W is sending B (DW) to process Q.
  - Split the weight of the process P into W1 and W2, such that W = W1 + W2 and W1 > 0, W2 > 0.
  - Set the weight of the process P as W1 (i.e., W = W1).
  - Send B (W2) to process Q, where DW = W2.
- Rule to receive B (DW) by process Q:
  - Add the weight DW to the weight of process Q, i.e., for process Q, W = W + DW.
  - If process Q was idle, it will become active on receiving B (DW).
- Rule to send C (DW): Any active process having weight W can become idle by sending C (W) to the controlling agent.
  - Send a control message C (W) to the controlling agent, where DW = W.
  - Set the weight of the process as 0, i.e., W = 0. (After this, the process will become idle.)
- Rule to receive C (DW) by the controlling agent:
  - Add the weight received through the control message to the weight of the controlling agent, i.e., W = W + DW.
  - After adding, if the weight of the controlling agent becomes 1, then it can be concluded that the computation has terminated.

An example of Huang's algorithm is shown in the following figure, where the controlling agent is P0 and the other processes are P1, P2, and P3. The weight of each process and message is shown in parentheses.

![Huang's algorithm example](https://i.imgur.com/8y3qXy7.png)

The advantages of Huang's algorithm are:

- The algorithm detects every true termination in finite time.
- The algorithm does not require addition of new communication channels between processes.
- The algorithm does not delay the underlying computation.

The limitations of Huang's algorithm are:

- The algorithm is unable to detect computation termination if a message is lost in transit.
- The algorithm does not work when a process fails while in an active state.

A possible mnemonic to remember Huang's algorithm is:

- B for Basic message, split and send weight
- C for Control message, collect and check weight
- W for Weight, assigned and transferred by processes and messages
- 1 for One, the initial and final weight of the controlling agent

A possible learning trick to understand Huang's algorithm is to imagine the weight as a token or a coin that represents the ownership of the computation.