### Grunt

- Grunt is Pig's interactive shell that enables users to enter Pig Latin statements interactively and provides a shell for users to interact with HDFS  .
- Grunt can be invoked by typing the `pig` command without any script or command to run . For example, `pig -x local` will result in the prompt `grunt>`.
- Grunt supports all the Pig Latin statements and commands, as well as some additional commands that are specific to Grunt .
- Grunt also supports all the Hadoop fs shell commands, which are accessed using the keyword `fs` . For example, `fs -ls /user/pig` will list the files in the HDFS directory `/user/pig`.
- Grunt maintains a history of the commands entered by the user, which can be accessed using the up and down arrow keys. The history file is stored in the user's home directory as `.pig_history`.
- Grunt allows users to set Pig and Hadoop properties using the `set` command . For example, `set mapreduce.task.profile true` will enable profiling for MapReduce tasks.
- Grunt can also execute Pig scripts using the `exec` or `run` commands . For example, `exec script.pig` will execute the script `script.pig` and return to the Grunt prompt, while `run script.pig` will execute the script and exit Grunt.