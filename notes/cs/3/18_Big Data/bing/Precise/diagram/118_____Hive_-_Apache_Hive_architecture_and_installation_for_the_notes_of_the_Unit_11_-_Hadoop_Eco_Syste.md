### Hive - Apache Hive architecture and installation

#### Apache Hive Architecture
Apache Hive is an open-source data warehousing tool for performing distributed processing and data analysis. It was developed by Facebook to reduce the work of writing the Java MapReduce program. Apache Hive uses a Hive Query language, which is a declarative language similar to SQL.

The major components of Apache Hive are the Hive clients, Hive services, Processing framework and Resource Management, and the Distributed Storage. Hive Metastore(HMS) provides a central repository of metadata that can easily be analyzed to make informed, data-driven decisions, and therefore it is a critical component of many data lake architectures.

#### Apache Hive Installation
To install Apache Hive, you need to start by downloading the most recent stable release of Hive from one of the Apache download mirrors. Next, you need to unpack the tarball. You can install a stable release of Hive by downloading a tarball, or you can download the source code and build Hive from that.

Apache Hive is based on Hadoop and requires a fully functional Hadoop framework. If your system does not have a working Hadoop installation, you need to install Hadoop first and only then proceed to install and configure Hive.

Running HiveServer2 and Beeline requires Java 1.7 or newer. Note that Hive versions 1.2 onward require Java 1.7 or newer, while Hive versions 0.14 to 1.1 work with Java 1.6 as well.