## Downloading and Installing Hadoop; Understanding Different Hadoop Modes. Startup Scripts, Configuration Files.

1. **Downloading Hadoop**: Hadoop can be downloaded from the Apache Hadoop website. Choose the version that is compatible with your system and download the tarball.

2. **Installing Hadoop**: After downloading, extract the tarball to a directory of your choice. Set the environment variables for Hadoop by adding the Hadoop bin directory to the PATH variable and setting the HADOOP_HOME variable to the Hadoop installation directory.

3. **Hadoop Modes**: Hadoop can be run in three modes: Standalone, Pseudo-Distributed, and Fully-Distributed. Standalone mode is used for development and testing, while Pseudo-Distributed mode is used for testing on a single machine. Fully-Distributed mode is used for production environments.

4. **Startup Scripts**: Hadoop includes several startup scripts for starting and stopping the Hadoop daemons. These scripts are located in the Hadoop bin directory.

5. **Configuration Files**: Hadoop uses several configuration files to set various parameters for the Hadoop daemons. These files are located in the Hadoop conf directory. Some of the important configuration files include core-site.xml, hdfs-site.xml, and mapred-site.xml.
