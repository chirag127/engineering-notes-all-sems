### Running MRv1 in YARN

In Hadoop 2.0, MapReduce was integrated with YARN, which replaced the older MapReduce version 1(MRv1). However, it is still possible to run MRv1 in YARN for legacy applications. In this section, we will discuss how to run MRv1 in YARN.

#### Steps to run MRv1 in YARN:

1. Install Hadoop 2.x and MRv1: First, we need to install Hadoop 2.x and MRv1 on the machine.

2. Configure MRv1: The next step is to configure MRv1 by setting the mapred.job.tracker property to localhost:8021 in mapred-site.xml.

3. Configure YARN: In yarn-site.xml, set the yarn.application.classpath property to include the MRv1 classpath.

4. Start MRv1: Start the MRv1 by starting the JobTracker using the command: $HADOOP_HOME/bin/mapred --daemon start jobtracker

5. Submit the job: Submit the MRv1 job using the command: $HADOOP_HOME/bin/hadoop jar Job.jar input output.

6. Monitor the job: Monitor the job using the JobTracker web UI at http://localhost:50030.

#### Advantages of running MRv1 in YARN:

- Compatibility: Running MRv1 in YARN allows legacy applications to continue running without modification.

- Familiarity: Developers who are used to MRv1 can continue to use it without needing to learn YARN-specific APIs.

#### Disadvantages of running MRv1 in YARN:

- Limited scalability: MRv1 has limited scalability compared to YARN, which can handle a larger number of nodes.

- Lack of features: MRv1 lacks some of the features of YARN, such as dynamic allocation of resources.

#### Example:

Suppose we have a legacy MRv1 application that we want to run on Hadoop 2.x. We can do this by following the steps outlined above.

#### Applications:

Running MRv1 in YARN is useful for organizations that have legacy applications that cannot be easily modified to run on YARN. It allows them to continue using their existing applications without having to rewrite them.

In conclusion, running MRv1 in YARN allows legacy applications to continue running without modification, while developers who are used to MRv1 can continue to use it without needing to learn YARN-specific APIs. However, it has limited scalability compared to YARN and lacks some of the features of YARN, such as dynamic allocation of resources.