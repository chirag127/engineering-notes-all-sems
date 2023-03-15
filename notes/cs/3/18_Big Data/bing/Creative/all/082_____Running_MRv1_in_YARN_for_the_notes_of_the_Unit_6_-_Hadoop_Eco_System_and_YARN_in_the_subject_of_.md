# Running MRv1 in YARN

- MRv1 is the original version of MapReduce that consists of interfaces and classes from the Java package org.apache.hadoop.mapred.
- YARN is the newer version of MapReduce that consists of interfaces and classes from the Java package org.apache.hadoop.mapreduce.
- YARN is also known as MRv2 or Yet Another Resource Negotiator .
- YARN separates the resource management and processing components of MapReduce, allowing multiple types of applications to run on the same cluster.
- MRv1 applications can run on YARN with minor changes in the configuration and command syntax .
- To run MRv1 applications on YARN, the following steps are required :
  - Set the mapreduce.framework.name property to yarn in the mapred-site.xml file.
  - Use the yarn command in the Hadoop-YARN bin folder rather than the hadoop command to submit applications.
  - Use the -libjars option to specify the location of the MRv1 jar files, such as hadoop-mapreduce-client-jobclient-2.x.x-tests.jar.
  - Use the ResourceManager web interface to monitor the applications running on the YARN cluster.
- The following is an example of running the sleep job from MRv1 on YARN:
  - yarn jar /usr/lib/hadoop-mapreduce/hadoop-mapreduce-client-jobclient-2.x.x-tests.jar sleep -m 3 -r 3 -mt 100 -rt 100
  - This command runs a sleep job with 3 mappers and 3 reducers, each sleeping for 100 seconds.
  - The output of the command shows the application ID, such as application_1403121905533_0002, which can be used to track the progress of the job on the ResourceManager web interface.