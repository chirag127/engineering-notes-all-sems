### Running MRv1 in YARN

1. YARN (Yet Another Resource Negotiator) is the resource management layer of Apache Hadoop.
2. YARN allows multiple data processing engines to handle data stored in a single platform.
3. MRv1 (MapReduce version 1) is the original version of the MapReduce programming model for processing large data sets.
4. MRv1 can be run in YARN by using the MapReduce Application Master, which is responsible for negotiating resources with the ResourceManager and working with the NodeManager to execute and monitor tasks.
5. To run MRv1 in YARN, the following steps can be followed:
    1. Configure the MapReduce Application Master by setting the appropriate properties in the mapred-site.xml file.
    2. Submit the MRv1 job to the ResourceManager using the `hadoop jar` command.
    3. The ResourceManager will allocate resources for the job and launch the Application Master.
    4. The Application Master will negotiate resources with the ResourceManager and work with the NodeManager to execute and monitor tasks.
    5. The job will run to completion and the results will be stored in the specified output location.
6. Running MRv1 in YARN allows for better resource utilization and improved scalability compared to running MRv1 in standalone mode.