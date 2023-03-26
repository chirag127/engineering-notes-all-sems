 Here is the content in markdown format without any emojis or external links and in formal tone:

### Design issues in Distributed Shared Memory

1. Coherency Maintaining coherency between the multiple copies of shared data on different nodes is a major issue. Some of the approaches to maintain coherency are:
- Update-based:Updates at one node are promptly propagated to other nodes.
- Invalidation-based:Other copies are invalidated when a node updates the data. Invalidate requests are sent to other nodes which then fetch updated data.
2. Granularity The granularity of sharing refers to the amount of data that is shared. Choosing appropriate granularity is a trade-off between the overhead of coherency maintenance and the usefulness of sharing. Fine-grained sharing has high overhead but high usefulness and vice versa for coarse-grained sharing.
3. Consistency models Consistency models define the degree of consistency of the shared memory. The models lie on a spectrum from weak to strong consistency. Weaker models have less overhead but stronger models are more intuitive to program with.
4. Scalability As the number of nodes in the system increases, the coherency overhead also increases significantly affecting the scalability of the system. Mechanisms to reduce this overhead such as hierachical coherence and multiple coherence domains are used to improve scalability.

The points cover the major design issues in distributed shared memory. Let me know if you would like me to elaborate on any of the points or modify the content in any way.