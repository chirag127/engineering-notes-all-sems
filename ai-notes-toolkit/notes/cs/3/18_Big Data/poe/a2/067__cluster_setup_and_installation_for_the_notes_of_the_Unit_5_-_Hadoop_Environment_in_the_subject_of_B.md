 Here is the markdown content for the given topic:

### Cluster Setup and Installation

1. Select Machines - Select machines to be used as master and slaves/workers. The master machine should have good amount of RAM and CPU. Worker machines can have less configurations.
2. Install Java - Install Java on all machines as Hadoop is written in Java. Use Java 1.8 or higher version. Set JAVA_HOME environment variable.
3. Install Hadoop - Download Hadoop tar file and extract it. Add Hadoop bin directory to system PATH.
4. Configure Hadoop - Edit core-site.xml, hdfs-site.xml, mapred-site.xml, yarn-site.xml files to configure Hadoop. Set Hadoop variables like namenode, datanode, jobtracker, tasktracker locations, ports, etc.
5. Format Namenode - Run `hdfs namenode -format` command to format the namenode. This should be done only for the first time or if the namenode is corrupted.
6. Start Hadoop Daemons - Start HDFS daemons - namenode and datanodes. Also start YARN daemons - resourcemanager and nodemanagers.
7. Test Hadoop Installation - Create input data, write a MapReduce program, deploy jar and run it. Check if the output is correct. This will test if the Hadoop cluster is setup properly.

The content is written in Markdown format with points and without any emojis or external links as per the instructions. The tone is formal and not showing any feelings. Please let me know if you would like me to modify or add any other content.