# Grunt

- Grunt is Pig's interactive shell that allows users to enter Pig Latin statements and commands interactively .
- Grunt can also be used to interact with HDFS and perform file system operations such as copying, moving, deleting, and listing files .
- Grunt can be invoked by typing the `pig` command with no script or command to run.
- Grunt supports the following types of commands:
  - Pig Latin statements: These are the statements that define the data processing logic using Pig Latin operators and functions. They must end with a semicolon (;).
  - Shell commands: These are the commands that are executed by the underlying shell (such as bash or cmd). They must be prefixed with a backslash (\).
  - Utility commands: These are the commands that control Pig and MapReduce, such as setting properties, killing jobs, describing relations, etc. They must not be prefixed with anything.
- Grunt can be used in local or Hadoop mode. In local mode, Pig runs on a single machine without Hadoop. In Hadoop mode, Pig runs on a cluster using MapReduce .
- Grunt can be configured using Pig and Hadoop properties. These properties can be set in the configuration files, the PIG_OPTS environment variable, the -P command line option, or the `set` utility command .
- Grunt can be exited by typing `quit` or `exit`.