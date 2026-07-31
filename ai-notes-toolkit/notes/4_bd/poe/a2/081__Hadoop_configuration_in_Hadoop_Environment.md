 Here is the content in markdown format with points, without emojis or external links and in a formal tone:

#### Hadoop configuration in Hadoop Environment

1. Hadoop configuration refers to the settings and parameters that are used to specify the behavior and deployment of Hadoop clusters. The basic Hadoop configuration involves:

- Specifying the storage paths for Hadoop distributed file system (HDFS)
- Configuring MapReduce parameters such as number of reducers
- Specifying network addresses of the nodes
- Configuring security parameters

2. The Hadoop configuration is defined in XML files called configuration files. The main configuration files are:

- core-site.xml: Specifies the HDFS namespace and the default storage system for Hadoop.
- hdfs-site.xml: Specifies HDFS parameters such as replication factor.
- yarn-site.xml: Specifies parameters for resource management and scheduling.
- mapred-site.xml: Specifies MapReduce framework parameters.

3. The configuration files reside on the local disk of all the nodes in the Hadoop cluster. The configuration parameters can be changed by editing the XML configuration files and then distributing the updated files to all the nodes in the cluster. The changes take effect once the Hadoop daemons (HDFS, YARN, MapReduce) are restarted to reload the configuration.

4. Hadoop also provides a command line tool called `hdfs dfsadmin -refreshNodes' to refresh the configuration from the files for specific daemons without restarting them. This is useful for making small incremental changes to the configuration.

The above points cover the key aspects of Hadoop configuration in the Hadoop environment. Let me know if you would like me to elaborate on any of the points or add more details to the explanation.