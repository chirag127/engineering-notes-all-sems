### Grunt

Grunt is an interactive shell for Pig, a high-level language for data analysis on Hadoop. Grunt allows users to enter Pig Latin statements interactively and execute them on Hadoop clusters. Grunt also provides a shell for interacting with the Hadoop Distributed File System (HDFS).

Some of the features of Grunt are:

- It supports all the Pig Latin commands and operators, such as LOAD, STORE, FILTER, JOIN, GROUP, FOREACH, etc.
- It supports all the Hadoop fs shell commands, such as ls, cat, mkdir, rm, etc. They are accessed using the keyword fs followed by a dash and the command name, such as fs -ls, fs -cat, etc.
- It supports some utility commands, such as set, exec, run, explain, illustrate, etc. They are used to set properties, execute scripts, run queries, show execution plans, generate examples, etc.
- It supports tab completion, history, and help. Users can press the tab key to complete a command or a file name, use the up and down arrow keys to navigate the history, and type help to get a list of commands and their usage.

To use Grunt, users need to invoke Pig with no script or command to run, and specify the execution mode, either local or mapreduce. For example, to start Grunt in local mode, users can type:

```bash
pig -x local
```

This will result in the prompt:

```bash
grunt>
```

Then, users can enter Pig Latin statements or HDFS commands at the grunt prompt. For example, to load a file from the local file system and store it in HDFS, users can type:

```bash
grunt> A = LOAD 'passwd' USING PigStorage(':');
grunt> STORE A INTO 'hdfs://localhost:9000/user/pig/passwd' USING PigStorage();
```

To exit Grunt, users can type quit or Ctrl-D.