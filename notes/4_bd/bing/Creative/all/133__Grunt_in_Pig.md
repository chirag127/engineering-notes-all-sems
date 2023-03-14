#### Grunt in Pig

- Grunt is the name of the interactive shell of Apache Pig, a platform for analyzing large data sets using a high-level language called Pig Latin.
- Grunt can be used to write Pig Latin scripts, load and store data, and execute Pig Latin commands.
- Grunt can also invoke shell commands using the `sh` and `fs` prefixes. For example, `sh ls` will list the files in the current directory, and `fs -ls` will list the files in the Hadoop file system.
- Grunt can be launched in three modes: local, mapreduce, and embedded. Local mode runs Pig on a single machine without Hadoop, mapreduce mode runs Pig on a Hadoop cluster, and embedded mode runs Pig from within a Java program.
- Grunt supports several features to make writing and debugging Pig Latin scripts easier, such as tab completion, history, aliases, macros, and comments.
- Grunt can also run Pig Latin scripts from a file using the `run` or `exec` commands. The `run` command loads the script into the Grunt shell, while the `exec` command executes the script and exits the shell.
- Grunt can be customized using the `.pigrc` file, which contains Grunt commands that are executed when the shell starts. The `.pigrc` file can be used to set properties, define aliases, load functions, and more.

Here is an example of a Grunt session:

```
$ pig -x local
grunt> A = load 'student.txt' using PigStorage(',') as (name:chararray, age:int, gpa:float);
grunt> B = filter A by age > 18;
grunt> C = group B by name;
grunt> D = foreach C generate group, AVG(B.gpa);
grunt> dump D;
(Bob,3.5)
(Alice,3.8)
grunt> quit
```

Some mnemonics and learning tricks for Grunt in Pig are:

- Remember that Grunt is the name of the Pig shell by thinking of a pig grunting.
- Remember the three modes of Grunt by thinking of LME: Local, Mapreduce, and Embedded.
- Remember the difference between `run` and `exec` by thinking of run as staying in the shell and exec as exiting the shell.
- Remember the `.pigrc` file by thinking of pig racing.