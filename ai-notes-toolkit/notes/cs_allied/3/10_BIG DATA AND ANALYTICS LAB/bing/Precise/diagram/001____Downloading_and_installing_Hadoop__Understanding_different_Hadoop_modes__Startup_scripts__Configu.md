## Downloading and Installing Hadoop; Understanding Different Hadoop Modes. Startup Scripts, Configuration Files.

1. **Downloading Hadoop**: Hadoop can be downloaded from the Apache Hadoop website. Choose the version that is compatible with your system and download the tarball.

2. **Installing Hadoop**: After downloading the tarball, extract it to a directory of your choice. Set the environment variables `HADOOP_HOME` to the directory where Hadoop is installed and `PATH` to include the `bin` directory of Hadoop.

3. **Hadoop Modes**: Hadoop can run in three modes: Standalone, Pseudo-Distributed, and Fully-Distributed. Standalone mode is used for development and testing, while Pseudo-Distributed mode is used for testing on a single machine. Fully-Distributed mode is used for production and runs on a cluster of machines.

4. **Startup Scripts**: Hadoop comes with several startup scripts that can be used to start and stop the Hadoop daemons. These scripts are located in the `sbin` directory of the Hadoop installation.

5. **Configuration Files**: Hadoop has several configuration files that can be used to configure the behavior of the system. These files are located in the `etc/hadoop` directory of the Hadoop installation. Some of the important configuration files are `core-site.xml`, `hdfs-site.xml`, and `mapred-site.xml`.
