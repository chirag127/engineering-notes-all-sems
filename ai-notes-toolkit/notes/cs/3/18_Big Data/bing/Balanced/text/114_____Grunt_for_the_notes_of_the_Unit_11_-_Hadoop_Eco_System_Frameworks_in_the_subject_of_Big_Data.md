### Grunt

- Grunt is Pig's interactive shell that allows users to enter Pig Latin statements and commands interactively and provides a shell for users to interact with HDFS  .
- Grunt can be invoked by typing the `pig` command without any arguments or by specifying the execution mode (`-x local` or `-x mapreduce`)  .
- Grunt supports all Pig Latin statements and commands, as well as some additional commands for shell and utility functions .
- Grunt also supports all Hadoop file system (`hadoop fs`) commands by using the keyword `fs`  .
- Grunt maintains a history of commands entered by the user in a file named `.pig_history` in the user's home directory .
- Grunt allows users to set Pig and Hadoop properties using the `set` command, either in the script or in the command line  .
- Grunt can also execute Pig scripts from files using the `exec` or `run` commands, or from the command line using the `-f` option  .