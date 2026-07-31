# Atomic Commit in Distributed Database System

- A distributed database system consists of multiple sites that store data and execute transactions.
- A distributed transaction is a transaction that accesses data from more than one site.
- Atomicity is a property that ensures that a distributed transaction either commits (succeeds) or aborts (fails) as a whole, regardless of failures or communication delays in the system.
- Atomic commit is a protocol that coordinates the decision of whether to commit or abort a distributed transaction among all the sites involved.
- Atomic commit is essential for maintaining the consistency and integrity of the distributed database.
- There are two main types of atomic commit protocols: blocking and non-blocking.
- Blocking protocols require some sites to wait for the response of other sites before making a decision. They guarantee atomicity, but may cause delays or deadlocks in the presence of failures.
- Non-blocking protocols allow sites to make independent decisions based on local information. They do not guarantee atomicity, but may improve performance and availability in the presence of failures.
- Examples of blocking protocols are two-phase commit (2PC) and three-phase commit (3PC).
- Examples of non-blocking protocols are one-phase commit (1PC), presumed abort (PA), presumed commit (PC), and failure-aware commit (FLAC).