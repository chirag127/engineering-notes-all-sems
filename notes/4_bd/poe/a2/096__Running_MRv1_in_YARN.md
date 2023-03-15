 Here is the content in markdown format with formal tone and without emojis:

#### Running MRv1 in YARN

1. Ensure that YARN is installed and configured on your cluster. YARN requires installation of Hadoop 2.4.0 or above.
2. Download the MapReduce 1 distribution and unpack it.
3. Set the necessary environment variables:
- HADOOP_COMMON_HOME pointing to the Hadoop common directory
- HADOOP_MAPRED_HOME pointing to the MapReduce 1 directory
- HADOOP_YARN_HOME pointing to the YARN directory
4. Add the following entries to the $HADOOP_MAPRED_HOME/conf/mapred-env.sh file:
export YARN_HOME=$HADOOP_YARN_HOME
export HADOOP_CONF_DIR=$HADOOP_COMMON_HOME/conf
5. Create a YARN client configuration file - yarn-client.xml - in the $HADOOP_CONF_DIR directory with the following content:
<configuration>
<property>
<name>yarn.resourcemanager.address</name>
<value>host:port</value>
</property>
</configuration>
Replace host:port with the ResourceManager's host and port respectively.
6. To run a MapReduce 1 job on YARN, use the YARN client mode by running:
$HADOOP_MAPRED_HOME/bin/yarn jar <MRv1 jar>

The content is written in points with a formal tone, without emojis and external links as instructed. Let me know if you would like me to modify or add anything.