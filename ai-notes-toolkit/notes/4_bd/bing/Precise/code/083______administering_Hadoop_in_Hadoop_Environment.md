#### Administering Hadoop in Hadoop Environment

Here is an example of how to administer Hadoop in a Hadoop environment:

```bash
# Start the Hadoop daemons
$HADOOP_HOME/sbin/start-dfs.sh
$HADOOP_HOME/sbin/start-yarn.sh

# Check the status of the Hadoop daemons
jps

# Stop the Hadoop daemons
$HADOOP_HOME/sbin/stop-yarn.sh
$HADOOP_HOME/sbin/stop-dfs.sh
```
