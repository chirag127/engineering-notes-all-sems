 Here is the content in markdown format written in a formal tone with points and including relevant details, diagrams, etc. to learn about Installing Spark:

#### Installing Spark

1. Download Spark - Download the latest version of Spark from the official Apache Spark website. Choose a package type - pre-built for Hadoop 2.6/2.7, or source code to build yourself. For learning, download the pre-built for Hadoop 2.6.

2. Set up Environment Variables - Set up environment variables SPARK_HOME to point to the root directory of your Spark installation and add $SPARK_HOME/bin to your PATH so that you can run spark-submit, spark-shell, and other Spark commands from any directory.

3. Install Java - Spark requires Java 8+ to run. Download and install OpenJDK or Oracle JDK 8 according to your system. Set JAVA_HOME environment variable to point to the location of Java in your system.

[Diagram showing the steps and the flow of actions from downloading Spark to setting up environment variables to installing Java.]

Advantages:
- Easy to install pre-built packages.
- Large ecosystem of applications and libraries.
- Runs on Hadoop YARN, standalone, Kubernetes, or Mesos.

Disadvantages:
- Fairly heavy system requirements.
-Steep learning curve.

Applications:
- Real-time processing.
- Machine learning and graph processing.
- SQL and streaming queries.