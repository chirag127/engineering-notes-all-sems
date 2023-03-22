 Here are the notes in Markdown format on the topic YARN for the Unit 6 - Hadoop Eco System and YARN in the subject of Big Data:

### YARN

- YARN stands for Yet Another Resource Negotiator. It is a cluster management technology for Hadoop.
- It separates the resource management and job scheduling/monitoring function from the data processing function.
- The two main components of YARN are:
	- ResourceManager (RM): Responsible for allocating resources (memory and CPU) to the applications and scheduling applications.
	- NodeManager (NM): Runs on each DataNode and is responsible for launching the applications' containers, monitoring their resource usage (memory, CPU, etc.) and reporting the same to the ResourceManager.
- The key features of YARN are:
	- Scalability: It uses a hierarchical architecture with global and local schedulers that can handle a large number of nodes and applications.
	- Multi-tenancy: It supports running multiple applications simultaneously sharing the same cluster resources.
	- Compatibility: It is backwards compatible with MapReduce and supports other application types like graph processing and streaming processing.
	- High utilization: It has a centralized scheduler that can perform efficient resource allocation to maximize cluster utilization.
- The basic steps in the YARN application execution are:
	1. The client submits the application to the ResourceManager.
	2. The ResourceManager negotiates resources from the NodeManager and allocates resources to the application.
	3. The application starts execution by launching containers using the allocated resources.
	4. The application performs its processing.
	5. The application finishes execution and releases the allocated resources.