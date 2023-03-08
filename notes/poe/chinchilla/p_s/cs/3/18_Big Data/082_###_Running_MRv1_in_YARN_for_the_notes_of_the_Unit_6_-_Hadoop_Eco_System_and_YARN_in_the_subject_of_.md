### Running MRv1 in YARN

In Hadoop 2, MapReduce version 1 (MRv1) can be run in YARN using a compatibility module. This allows users to run their existing MRv1 jobs on YARN without having to rewrite them for MapReduce version 2 (MRv2).

#### Advantages of running MRv1 in YARN

- Allows users to run their existing MRv1 jobs on YARN without having to rewrite them for MRv2.
- Provides a seamless migration path from MRv1 to MRv2.
- Allows users to take advantage of the resource management and scheduling capabilities of YARN.

#### Disadvantages of running MRv1 in YARN

- MRv1 jobs running in YARN are not as performant as MRv2 jobs.
- MRv1 jobs running in YARN do not have access to all of the features of YARN, such as containers and labels.

#### Example of running MRv1 in YARN

To run an MRv1 job in YARN, you need to use the `hadoop jar` command with the `yarn` option, like this:

```
$ hadoop jar myjob.jar org.apache.hadoop.mapred.JobClient -Dmapred.job.tracker=<yarn-resourcemanager-hostname>:<yarn-resourcemanager-port> -Dmapreduce.framework.name=yarn -submit -archives <archive1>#<link1>,<archive2>#<link2> <input> <output>
```

This command submits an MRv1 job to YARN, with the job tracker specified as the YARN resource manager.

#### Applications of running MRv1 in YARN

- Allows users to run their existing MRv1 jobs on YARN without having to rewrite them for MRv2.
- Provides a seamless migration path from MRv1 to MRv2.
- Can be useful for organizations that have a large investment in MRv1 jobs and want to continue using them.

Overall, running MRv1 in YARN can be a useful tool for organizations that want to continue using their existing MRv1 jobs while taking advantage of the resource management and scheduling capabilities of YARN.