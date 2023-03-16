### Dynamic voting protocols

- Dynamic voting protocols are a class of protocols for consistency and recovery control of replicated data in distributed systems  .
- The purpose of replicating data is to improve the availability and fault tolerance of a logical file or object in the presence of site failures and network partitions  .
- Dynamic voting protocols assign weights or votes to each replica of a file or object, and require a quorum or majority of votes to access or update the file or object  .
- The weights or votes of replicas can be dynamically changed or reassigned based on the current state of the system, such as the number of active sites, the network connectivity, or the access patterns  .
- Dynamic voting protocols aim to achieve the following goals  :
  - Availability: The file or object should be accessible or updatable by any site that is not isolated from the rest of the system.
  - Consistency: The file or object should have a consistent state across all replicas, and any update should be propagated to all replicas eventually.
  - Efficiency: The file or object should be accessed or updated with minimal communication and synchronization overhead.
- Dynamic voting protocols can be classified into two categories  :
  - Static-weight dynamic voting protocols: The weights or votes of replicas are fixed at the beginning of the system operation, and do not change during normal operation. However, the weights or votes can be reassigned when a site or link failure occurs, or when a site or link recovers.
  - Dynamic-weight dynamic voting protocols: The weights or votes of replicas can change dynamically during normal operation, based on some criteria such as the frequency of access, the distance between sites, or the load of sites.
- Dynamic voting protocols can use different quorum schemes to determine the minimum number of votes required to access or update a file or object   :
  - Majority quorum scheme: The quorum is more than half of the total votes in the system.
  - Read-one write-all quorum scheme: The quorum for read operations is one vote, and the quorum for write operations is all votes in the system.
  - Read-one write-all-available quorum scheme: The quorum for read operations is one vote, and the quorum for write operations is all votes in the available sites.
  - Tree quorum scheme: The quorum is a subset of votes that forms a connected subtree in a logical tree structure of the system.
  - Grid quorum scheme: The quorum is a subset of votes that forms a connected row or column in a logical grid structure of the system.