# mkdir, rmdir, tar, g

- mkdir is a command that creates a new directory in the file system.
- rmdir is a command that removes an empty directory from the file system.
- tar is a command that creates or extracts compressed archive files.
- g is a command that invokes the GNU Compiler Collection (GCC) to compile source code files.

## Examples

- To create a new directory named "project" in the current working directory, use the command:

`mkdir project`

- To remove an empty directory named "project" from the current working directory, use the command:

`rmdir project`

- To create a compressed archive file named "project.tar.gz" that contains all the files and subdirectories in the "project" directory, use the command:

`tar czvf project.tar.gz project`

- To extract the contents of the compressed archive file named "project.tar.gz" in the current working directory, use the command:

`tar xzvf project.tar.gz`

- To compile a source code file named "main.c" using the GCC compiler and produce an executable file named "main", use the command:

`g main.c -o main`