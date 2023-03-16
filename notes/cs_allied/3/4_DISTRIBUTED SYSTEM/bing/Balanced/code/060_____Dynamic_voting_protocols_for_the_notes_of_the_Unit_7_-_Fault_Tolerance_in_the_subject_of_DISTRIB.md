### Dynamic voting protocols

- Dynamic voting protocols are techniques for consistency and recovery control of replicated files in distributed systems  .
- The purpose of a replicated file is to improve the availability of a logical file in the presence of site failures and network partitions  .
- A dynamic voting protocol assigns a number of votes to each copy of a replicated file, and allows a group of copies to access the file only if they have a majority of votes   .
- The number of votes assigned to each copy can change dynamically depending on the system state, such as the number of copies, the network topology, the failure pattern, etc    .
- Dynamic voting protocols can improve the performance and reliability of distributed systems by reducing the communication overhead, increasing the concurrency, and tolerating more failures    .
- Dynamic voting protocols can be classified into two categories: topological and non-topological.
  - Topological dynamic voting protocols assign votes based on the network structure and the location of copies, such as the distance, the connectivity, the partitionability, etc.
  - Non-topological dynamic voting protocols assign votes based on other criteria, such as the access frequency, the update rate, the copy age, etc.
- Examples of dynamic voting protocols are:
  - The dynamic weighted voting scheme proposed by Davcev  , which assigns votes to copies according to their distance from the center of the network and the number of copies in their partition.
  - The dynamic vote reassignment protocols proposed by Gifford, which reassign votes to the surviving copies when a node or a link fails, and restore the original votes when the failure is repaired.
  - The quorum-based voting protocols proposed by Gifford, which require a transaction to obtain a quorum of votes from a subset of copies before performing a restricted operation, such as reading or writing the file.
  - The efficient dynamic voting algorithms proposed by Agrawal and Abbadi, which assign votes to copies based on their topological properties, such as the non-partitionability, the connectivity, and the diameter of the group containing the copy.