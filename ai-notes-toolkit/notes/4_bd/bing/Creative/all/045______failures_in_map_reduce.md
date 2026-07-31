#### Failures in MapReduce

- MapReduce is a programming model and framework for processing large-scale data sets in parallel and distributed manner.
- MapReduce consists of two phases: map and reduce, which are executed by a master node and multiple worker nodes.
- Failures are inevitable in MapReduce due to the large number of nodes and the unreliable nature of the network and hardware.
- There are three types of failures in MapReduce: task failures, worker failures, and master failures.

##### Task failures
- A task failure occurs when a map or reduce task fails to complete due to an error in the user code, a corrupted input, or a transient fault.
- Task failures are handled by the master node, which detects the failed task and reassigns it to another worker node.
- Task failures are common and do not affect the correctness of the MapReduce output, as long as the map and reduce functions are deterministic and idempotent.
- A deterministic function is one that produces the same output for the same input, regardless of the order or timing of execution.
- An idempotent function is one that can be applied multiple times without changing the result, such as adding zero or multiplying by one.

##### Worker failures
- A worker failure occurs when a worker node crashes or becomes unreachable due to a network partition, a power outage, or a hardware failure.
- Worker failures are also handled by the master node, which periodically pings the worker nodes and marks them as failed if they do not respond within a timeout period.
- The master node then reassigns the tasks of the failed worker to other workers, and also reassigns the input splits that were stored on the failed worker to other workers.
- Worker failures are less common than task failures, but they can affect the performance and availability of the MapReduce job, as they cause more work to be redone and more data to be transferred.

##### Master failures
- A master failure occurs when the master node crashes or becomes unreachable due to a network partition, a power outage, or a hardware failure.
- Master failures are the most serious type of failures in MapReduce, as they can cause the entire job to fail or stall.
- Master failures are handled by using a backup master node, which takes over the role of the master node in case of a failure.
- The backup master node maintains a copy of the state of the master node, such as the status of the tasks, the workers, and the input splits, by periodically receiving checkpoints from the master node.
- The backup master node can also be elected by the worker nodes using a consensus protocol, such as Paxos or Raft, in case the master node fails to send checkpoints.

##### Mnemonics and learning tricks
- A possible mnemonic to remember the types of failures in MapReduce is: **TWM** (Task, Worker, Master).
- A possible learning trick to remember the difference between deterministic and idempotent functions is: **DID** (Deterministic: same Input, same output; Idempotent: same output, Doesn't matter how many times applied).