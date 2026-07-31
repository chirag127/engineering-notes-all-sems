### Hadoop configuration

- Hadoop configuration is the process of setting the parameters and properties of the Hadoop system and its components, such as HDFS, YARN, and MapReduce.
- Hadoop configuration is driven by two types of important configuration files  :
  - Read-only default configuration files, which provide the default values for the configuration parameters. These files are located in the `share/hadoop/common` directory of the Hadoop installation and have names like `core-default.xml`, `hdfs-default.xml`, `yarn-default.xml`, and `mapred-default.xml`.
  - Site-specific configuration files, which override the default values and specify the custom settings for the Hadoop cluster. These files are located in the `etc/hadoop` directory of the Hadoop installation and have names like `core-site.xml`, `hdfs-site.xml`, `yarn-site.xml`, and `mapred-site.xml`.
- The site-specific configuration files are the ones that need to be edited by the Hadoop administrator to configure the Hadoop cluster according to the requirements and specifications of the environment and the applications.
- The site-specific configuration files contain XML elements that define the name, value, description, and source of each configuration parameter. For example, the following XML element sets the value of the `fs.defaultFS` parameter to `hdfs://localhost:9000` in the `core-site.xml` file:

```xml
<configuration>
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://localhost:9000</value>
    <description>The name of the default file system.</description>
    <source>core-default.xml</source>
  </property>
</configuration>
```

- Some of the common configuration parameters that need to be set in the site-specific configuration files are  :
  - `fs.defaultFS`: The name of the default file system. This parameter is set in the `core-site.xml` file and specifies the URI of the HDFS name node.
  - `dfs.namenode.name.dir`: A comma-separated list of directories where the name node stores the metadata of the HDFS file system. This parameter is set in the `hdfs-site.xml` file and specifies the local directories on the name node machine.
  - `dfs.datanode.data.dir`: A comma-separated list of directories where the data node stores the data blocks of the HDFS file system. This parameter is set in the `hdfs-site.xml` file and specifies the local directories on the data node machines.
  - `yarn.resourcemanager.hostname`: The hostname of the resource manager. This parameter is set in the `yarn-site.xml` file and specifies the machine where the resource manager daemon runs.
  - `yarn.nodemanager.local-dirs`: A comma-separated list of directories where the node manager stores the local data of the YARN applications. This parameter is set in the `yarn-site.xml` file and specifies the local directories on the node manager machines.
  - `yarn.nodemanager.log-dirs`: A comma-separated list of directories where the node manager stores the logs of the YARN applications. This parameter is set in the `yarn-site.xml` file and specifies the local directories on the node manager machines.
  - `mapreduce.framework.name`: The name of the MapReduce framework. This parameter is set in the `mapred-site.xml` file and specifies the implementation of the MapReduce framework. The default value is `yarn`, which means that the MapReduce jobs run on the YARN framework.
  - `mapreduce.jobhistory.address`: The address of the job history server. This parameter is set in the `mapred-site.xml` file and specifies the host and port of the machine where the job history server daemon runs.
  - `mapreduce.jobhistory.webapp.address`: The address of the job history web application. This parameter is set in the `mapred-site.xml` file and specifies the host and port of the machine where the job history web application runs.

- To configure the Hadoop cluster, the Hadoop administrator needs to edit the site-specific configuration files on the master node and copy them to the slave nodes. Alternatively, the Hadoop administrator can use a distributed configuration management tool, such as Ansible, Puppet, or Chef, to automate the configuration process and ensure consistency across the cluster nodes.
- To apply the configuration changes, the Hadoop administrator needs to restart the Hadoop daemons on the