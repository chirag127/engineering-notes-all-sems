#### Grunt in Pig

- Grunt is a shell command in Apache Pig.
- It is mainly used to write Pig Latin scripts.
- Pig scripts can be executed with Grunt shell, which is a native shell provided by Apache Pig to execute Pig queries .
- Grunt shell can also be used to invoke any shell commands using `sh` and `fs` .
- However, using `sh` command from the Grunt shell, we cannot execute the commands that are a part of the shell environment (ex − `cd`) .