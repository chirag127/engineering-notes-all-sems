 Here is the formal content in Markdown format without any emojis or external links on the given topic:

### Solution to Byzantine Agreement problem

1. Byzantine fault tolerance: The Byzantine fault tolerance algorithm allows a system of nodes to reach consensus even with some nodes failing or acting maliciously to propagate incorrect information.
2. Practical Byzantine fault tolerance (PBFT): PBFT is a widely used algorithm to achieve Byzantine fault tolerance. It works on a system of multiple replicated servers or nodes. The key points of the algorithm are:
- All nodes establish TCP connections with one another to send messages.
- A primary node is selected to order client requests and assign sequence numbers.
- For each client request, a three-phase commit protocol is used:
    - Pre-prepare: Primary sends a pre-prepare message with the sequence number and request details.
    - Prepare: Nodes send prepare messages if they agree on the pre-prepare details.
    - Commit: Primary sends commit message if sufficient prepares are received, and nodes commit the request if they receive commit message matching their prepare.
- Requests are committed if 2/3 or more nodes successfully execute the three-phase commit. This can tolerate 1/3 faulty or malicious nodes.
- Views are changed if a node doesn't receive expected messages, and a new primary is selected to keep the system progressing.

The key goals achieved are:
- Agreement: All correct nodes agree on the sequence of requests.
- Validity: If a request is committed, it was previously proposed by a client.
- Integrity: No request is committed unless a majority of correct nodes have accepted it.
- Termination: All correct nodes eventually commit or reject any request.

The PBFT algorithm ensures Byzantine fault tolerance and allows for state machine replication of services across multiple nodes. It is more complex but highly reliable and secure compared to simpler consensus algorithms.