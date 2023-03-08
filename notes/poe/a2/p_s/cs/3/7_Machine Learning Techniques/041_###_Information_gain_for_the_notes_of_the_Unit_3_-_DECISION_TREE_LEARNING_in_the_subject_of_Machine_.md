 Here is the content in markdown format:

#### Running MRv1 in YARN

1. Set up Hadoop YARN - Ensure you have a working Hadoop YARN cluster setup. YARN comes bundled with Hadoop 2.x by default.
2. Package MRv1 JAR - Package your MRv1 program into a JAR file using the Maven Shade plugin or similar. This will package your code and dependencies into a single JAR which can be submitted to YARN.
3. Configure YARN resources - You will need to specify the number of containers (executors) to request from YARN, as well as the resource requirements for each (memory and CPU). The number of containers and resource requirements will depend on the size of your cluster and the requirements of your application.
4. Submit application to YARN - Use the yarn jar command to submit your packaged MRv1 JAR to YARN, specifying the resource requirements using command line options. YARN will then launch the specified number of containers and start running your application.
5. Monitor application - You can monitor the application running in YARN using the YARN Web UI or the yarn application command line tools. This will show you information such as number of allocated containers, resource usage, application progress and any errors.

Advantages:
- YARN provides a centralized resource management system for large Hadoop clusters.
- YARN allows you to run multiple applications simultaneously sharing the same cluster resources.
- Fault tolerance and high availability features. If any node fails, YARN will reschedule tasks on other nodes.

Disadvantages:
- There is overhead in running on YARN due to the additional resource negotiation required.
- Debugging and tuning YARN applications can be challenging due to the complexity of the system.
- Knowledge of YARN architecture and tuning is required to use it effectively.

[Diagrams and code examples can be added here for illustration.]