#### Running MRv1 in YARN

In this section, we will discuss how to run MapReduce version 1 (MRv1) in YARN, which is a resource management system used in Hadoop clusters. YARN is designed to support multiple processing frameworks, including MRv1, which was the original MapReduce framework in Hadoop.

To run MRv1 in YARN, follow these steps:

1. Install Hadoop on your cluster: Before you can run MRv1 in YARN, you need to have Hadoop installed on your cluster. Follow the installation instructions provided by your Hadoop distribution.

2. Configure MRv1 for YARN: MRv1 needs to be configured to run in YARN mode. To do this, set the following properties in your `mapred-site.xml` file:

```
<property>
  <name>mapreduce.framework.name</name>
  <value>yarn</value>
</property>
<property>
  <name>yarn.app.mapreduce.am.env</name>
  <value>HADOOP_MAPRED_HOME=$HADOOP_HOME</value>
</property>
```

3. Start the MRv1 job: Once you have configured MRv1 for YARN, you can start a job by running the following command:

```
hadoop jar <path-to-jar> <main-class> <input-path> <output-path>
```

Replace `<path-to-jar>` with the path to your MapReduce job jar file, `<main-class>` with the name of your MapReduce job's main class, `<input-path>` with the path to your input data, and `<output-path>` with the path to your output directory.

4. Monitor the job: You can monitor the progress of your MRv1 job by running the following command:

```
yarn application -list
```

This will show you the status of all YARN applications running on your cluster, including your MRv1 job.

5. View the job output: Once your MRv1 job has completed, you can view the output by running the following command:

```
hadoop fs -cat <output-path>/part-r-00000
```

Replace `<output-path>` with the path to your output directory. This command will display the contents of the output file on the console.

In conclusion, running MRv1 in YARN is a straightforward process that involves configuring MRv1 for YARN mode and starting a job using the `hadoop jar` command. By following the steps outlined above, you can run MRv1 jobs in YARN and take advantage of the benefits of YARN's resource management capabilities.