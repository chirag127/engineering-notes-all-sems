 Here is the content in Markdown format for the topic ### MRv2 for the notes of the Unit 6 - Hadoop Eco System and YARN in the subject of Big Data:

### MRv2

- MRv2 is the second version of MapReduce. It was introduced in Hadoop 2.x to overcome the limitations of MRv1.
- MRv2 runs on YARN instead of using its own resource management framework as in MRv1. This makes MRv2 more efficient, scalable and powerful than MRv1.
- In MRv2, the JobTracker and TaskTracker of MRv1 have been replaced by ResourceManager and NodeManager respectively. The ResourceManager manages resources across the cluster and schedules applications. The NodeManager launches and monitors containers.
- MRv2 has a pluggable architecture that can run algorithms other than MapReduce on YARN. This enables other processing frameworks like Spark, Flink, etc. to run on YARN along with MapReduce.
- Some advantages of MRv2 over MRv1 are:
	- Better utilization of cluster resources due to YARN.
	- Better scalability to handle bigger clusters and workloads.
	- Support for non-MapReduce applications like graph processing and stream processing frameworks.
	- Improved cluster utilization via centralised resource management.
	- Improved cluster security with support for Kerberos authentication and service-level authorization.
- Some disadvantages of MRv2 are:
	- Additional complexity due to interactions between multiple frameworks on YARN.
	- Compatibility issues in running older MRv1 jobs due to differences with MRv2.

[Include diagrams, codes, tables, examples, applications, etc. if helpful for learning and comprehension]