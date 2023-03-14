#### Running MRv1 in YARN

- MRv1 stands for MapReduce version 1, which is the original computation framework in Hadoop that consists of a JobTracker and TaskTrackers.
- YARN stands for Yet Another Resource Negotiator, which is the new computation framework in Hadoop that consists of a ResourceManager, NodeManagers, and ApplicationMasters.
- YARN is backward-compatible with MRv1, which means that all jobs that run against MRv1 can also run in a YARN cluster.
- To run MRv1 jobs in YARN, you need to use the `yarn` command in the Hadoop-YARN bin folder rather than the `hadoop` command. For example, to run a word count job, you can use the following command:

```
yarn jar /usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar wordcount input output
```

- You can also use the `hadoop` command to submit MRv1 jobs in YARN, but the `yarn` command is preferred.
- To monitor MRv1 jobs in YARN, you can use the ResourceManager web interface, which shows the basic cluster metrics, list of applications, and nodes associated with the cluster. The default URL for the ResourceManager web interface is http://<ResourceManagerHost>:8088/.
- You can also use the `yarn` command to view the status of MRv1 jobs in YARN. For example, to list all the applications, you can use the following command:

```
yarn application -list
```

- To view the details of a specific application, you can use the following command:

```
yarn application -status <application_id>
```

- To view the logs of a specific application, you can use the following command:

```
yarn logs -applicationId <application_id>
```

- To kill a specific application, you can use the following command:

```
yarn application -kill <application_id>
```

- To view the history of MRv1 jobs in YARN, you can use the JobHistoryServer web interface, which shows the completed applications and their details. The default URL for the JobHistoryServer web interface is http://<JobHistoryServerHost>:19888/.
- You can also use the `mapred` command to view the history of MRv1 jobs in YARN. For example, to list all the jobs, you can use the following command:

```
mapred job -list
```

- To view the details of a specific job, you can use the following command:

```
mapred job -status <job_id>
```

- To view the counters of a specific job, you can use the following command:

```
mapred job -counter <job_id> <group_name> <counter_name>
```

- To view the logs of a specific job, you can use the following command:

```
mapred job -logs <job_id>
```

- To kill a specific job, you can use the following command:

```
mapred job -kill <job_id>
```

- A mnemonic to remember the difference between MRv1 and YARN is: MRv1 has a JobTracker, YARN has a ResourceManager. MRv1 has TaskTrackers, YARN has NodeManagers. MRv1 has jobs, YARN has applications.