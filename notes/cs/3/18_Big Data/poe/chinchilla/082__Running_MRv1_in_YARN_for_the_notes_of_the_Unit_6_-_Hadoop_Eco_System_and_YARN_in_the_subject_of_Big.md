### Running MRv1 in YARN

In this section, we will discuss how to run MRv1 jobs in YARN. MRv1 refers to the MapReduce version 1, which was the original implementation of MapReduce in Hadoop before YARN. While YARN is now the preferred way to run MapReduce jobs, some legacy applications still use MRv1.

Here are the steps to run MRv1 jobs in YARN:

1. Start the MRv1 JobTracker service: The MRv1 JobTracker service needs to be running for MRv1 jobs to work in YARN. You can start it using the following command:

   ```
   $ hadoop jobtracker
   ```

2. Configure the MRv1 job: MRv1 jobs need to be configured to run on YARN. This can be done by setting the following properties in the job configuration:

   ```
   mapreduce.framework.name=yarn
   yarn.app.mapreduce.am.env=HADOOP_MAPRED_HOME=/path/to/mrv1
   yarn.app.mapreduce.am.command-opts=-Dmapred.job.tracker=<jobtracker-host:jobtracker-port>
   ```

   Replace `/path/to/mrv1` with the path to the MRv1 installation directory, and `<jobtracker-host:jobtracker-port>` with the hostname and port of the MRv1 JobTracker service.

3. Submit the job: Once the job is configured, it can be submitted to YARN using the following command:

   ```
   $ hadoop jar /path/to/mrv1/hadoop-<version>-examples.jar <job-class> <job-arguments>
   ```

   Replace `/path/to/mrv1` with the path to the MRv1 installation directory, `<version>` with the version of Hadoop, `<job-class>` with the class name of the MRv1 job, and `<job-arguments>` with the arguments for the job.

4. Monitor the job: You can monitor the progress of the MRv1 job using the YARN web UI or the command line:

   ```
   $ yarn application -list
   $ yarn application -status <application-id>
   $ yarn logs -applicationId <application-id>
   ```

   Replace `<application-id>` with the ID of the YARN application.

That's it! With these steps, you can run MRv1 jobs in YARN. However, it is recommended to migrate to YARN-based MapReduce for better performance and scalability.