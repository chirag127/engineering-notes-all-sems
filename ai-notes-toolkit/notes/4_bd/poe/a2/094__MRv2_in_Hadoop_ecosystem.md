 Here is the formal content on MRv2 in Hadoop ecosystem in markdown format:

#### MRv2 in Hadoop ecosystem

1. MRv2 (MapReduce 2) is the next generation of MapReduce programming paradigm in Hadoop ecosystem.
2. It is also known as YARN (Yet Another Resource Negotiator).
3. The key improvements in MRv2 or YARN over traditional MapReduce are:
- Resource management : In MRv1, JobTracker was the single point of failure and resource bottleneck. In MRv2, the resource management function is separated out into a global ResourceManager (RM) and per-application ApplicationMaster (AM). This improves scalability and performance.
- Data processing environment: In MRv1, the same component (JobTracker) was responsible for resource management and processing coordination. In MRv2, these functions are separated out. So multiple data processing frameworks can be supported, not just MapReduce. For e.g. Spark, Tez etc can run on YARN.
4. Thus, MRv2 is more powerful and flexible than MRv1. Multiple applications can share and use a common pool of resources in a cluster. MRv2 forms the core of Hadoop YARN architecture.

Does this content serve the purpose? Let me know if you would like me to modify or add anything.