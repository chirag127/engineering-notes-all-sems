 Here is the solution to Byzantine Agreement problem written in markdown format:

### Solution to Byzantine Agreement problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

The Byzantine Agreement problem can be solved using the following methods:

1. Proof of Work - Bitcoin uses this method. Miners solve computationally intensive puzzles to agree upon the ledger. The ledger with highest proof of work is considered the agreed ledger.
Advantages: Does not require trusting a third party.
Disadvantages: Wastage of energy and resources in solving puzzles.

2. Practical Byzantine Fault Tolerance (PBFT) - It uses replication of servers and majority voting to tolerate Byzantine faults.
Steps:

- Clients send requests to primary replica which forwards the request to backup replicas.
- Replicas run the request and send replies to primary.
- Primary waits for f+1 matching replies (f is maximum number of faulty replicas). If received, it sends the response to the client.
- If primary is faulty, one of the correct backup replicas is elected as the new primary.

Advantages: Efficient and can tolerate high number of faults.
Disadvantages: Centralized - depends on primary replica.

3. Viewstamped Replication - Improves on PBFT. Does not depend on primary. Each server assigns timestamps (viewstamps) to requests and agrees on a total order of requests. The request with the highest viewstamp is executed first.
Advantages: Decentralized, can tolerate high number of faults.
Disadvantages: Complex to implement.

Mnemonics:
Proof of Work - puzzles, mining, bitcoin
PBFT - replicate, majority vote, primary, backups
Viewstamped Replication - timestamps, total order, decentralized

Hope this helps! Let me know if you would like me to explain anything in more detail.