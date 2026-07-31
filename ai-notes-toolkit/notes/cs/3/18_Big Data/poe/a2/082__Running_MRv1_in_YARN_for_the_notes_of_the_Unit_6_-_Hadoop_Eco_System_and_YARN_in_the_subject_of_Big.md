 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### Running MRv1 in YARN for the notes of the Unit 6 - Hadoop Eco System and YARN in the subject of Big Data.

1. Set up a YARN cluster with at least one ResourceManager and NodeManager.
2. Download the MRv1 framework and upload it to HDFS.
3. Set the following in mapred-site.xml:

<property>
<name>mapreduce.framework.name</name>
<value>yarn</value>
</property>

4. Set the following in yarn-site.xml:

<property>
<name>yarn.resourcemanager.hostname</name>
<value>[ResourceManager hostname]</value>
</property>

5. Start YARN daemons - ResourceManager and NodeManager.
6. Submit the MRv1 job to the YARN ResourceManager using the command:

yarn jar <MRv1 jar path> <MainClass> <args>

7. Monitor the job execution progress from the ResourceManager UI.

The above points cover the steps to run an MRv1 job on a YARN cluster. The steps include setting up YARN, configuring the framework to run on YARN, starting the YARN daemons, submitting the MRv1 job to the ResourceManager and monitoring the job status.