#### Running MRv1 in YARN

- MRv1 stands for MapReduce version 1, which is the original computation framework in Hadoop that consists of a JobTracker and TaskTrackers.
- YARN stands for Yet Another Resource Negotiator, which is the new computation framework in Hadoop that consists of a ResourceManager, NodeManagers, and ApplicationMasters.
- YARN is backward-compatible with MRv1, meaning that all jobs that run against MRv1 can also run in a YARN cluster.
- To run MRv1 jobs in YARN, you need to use the `yarn` command in the Hadoop-YARN bin folder rather than the `hadoop` command. For example, to run a word count job, you can use the following command:

```bash
yarn jar /usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar wordcount input output
```

- You can monitor the MRv1 jobs running on YARN using the ResourceManager web interface, which shows the basic cluster metrics, list of applications, and nodes associated with the cluster. The default URL for the ResourceManager web interface is `http://<ResourceManagerHost>:8088/`.
- You can also view the job history and logs of the MRv1 jobs using the JobHistoryServer web interface, which shows the details of each job, such as the start time, end time, status, counters, tasks, and attempts. The default URL for the JobHistoryServer web interface is `http://<JobHistoryServerHost>:19888/`.