#### Running MRv1 in YARN

- MRv1 is the original MapReduce framework that runs on Hadoop 1.x. It can also run on YARN, which is the resource management layer introduced in Hadoop 2.x.
- To run MRv1 applications on YARN, you need to use the `yarn` command in the Hadoop-YARN bin folder rather than the `hadoop` command. For example, to run a word count job, you can use the following command:

  `yarn jar /usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar wordcount input output`

- You can also use the `hadoop` command to run MRv1 applications on YARN, but it is not recommended as it may cause compatibility issues.
- To monitor MRv1 applications on YARN, you can use the ResourceManager web interface, which shows the basic cluster metrics, list of applications, and nodes associated with the cluster. You can access the ResourceManager web interface by using the following URL:

  `http://<ResourceManager-Host>:8088`

- The ResourceManager web interface shows the application ID, name, type, user, queue, state, final status, progress, and tracking URL for each application. You can click on the application ID to see more details about the application, such as the application master, containers, logs, and counters.
- You can also use the `yarn` command to monitor MRv1 applications on YARN. For example, you can use the following command to list all the applications:

  `yarn application -list`

- You can use the following command to get the status of a specific application:

  `yarn application -status <application_id>`

- You can use the following command to kill a specific application:

  `yarn application -kill <application_id>`