## Unit 4 - Agreement Protocols

- Agreement protocols are used to achieve a common goal in distributed systems, even in the presence of failures  .
- Agreement protocols require processes to exchange their values with other processes and relay the values received from others several times to isolate the effect of faulty processes .
- Agreement protocols can be classified into two types: consensus protocols and leader election protocols  .
- Consensus protocols are used to ensure that all processes agree on a single value, such as whether to commit or abort a transaction, or what is the latest update to a replicated data item   .
- Leader election protocols are used to ensure that all processes agree on a single process, such as who is the coordinator, the primary, or the owner of a resource   .
- Agreement protocols must satisfy the following properties   :
  - Validity: The agreed value or process must be one of the initial values or processes of the non-faulty processes.
  - Agreement: All non-faulty processes must agree on the same value or process.
  - Termination: All non-faulty processes must eventually decide on a value or process.
- Agreement protocols may also need to satisfy other properties, such as fault-tolerance, uniformity, anonymity, or fairness, depending on the application and the system model   .
- Agreement protocols are challenging to design and implement, especially in asynchronous systems, where there is no bound on message delays or process speeds, and where failures may be undetectable   .
- Agreement protocols are often based on techniques such as message passing, timeouts, quorums, randomization, or failure detectors   .
- Agreement protocols are widely used in distributed systems, such as distributed databases, distributed file systems, distributed consensus platforms, distributed coordination services, or distributed resource management systems   .