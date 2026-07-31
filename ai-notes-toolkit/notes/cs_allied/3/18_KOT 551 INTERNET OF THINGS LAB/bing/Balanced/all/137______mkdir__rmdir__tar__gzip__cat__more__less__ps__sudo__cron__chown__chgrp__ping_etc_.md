# Linux Commands

## mkdir
- mkdir stands for make directory.
- It is used to create new directories in the file system.
- Syntax: `mkdir [options] directory_name`
- Options:
  - `-p`: create parent directories if they do not exist.
  - `-v`: print a message for each created directory.
  - `-m`: set the mode (permissions) of the created directory.

## rmdir
- rmdir stands for remove directory.
- It is used to delete empty directories from the file system.
- Syntax: `rmdir [options] directory_name`
- Options:
  - `-p`: remove directory and its parents if they are empty.
  - `-v`: print a message for each removed directory.

## tar
- tar stands for tape archive.
- It is used to create or extract compressed archive files.
- Syntax: `tar [options] [archive_file] [file_list]`
- Options:
  - `-c`: create a new archive file.
  - `-x`: extract files from an archive file.
  - `-f`: specify the name of the archive file.
  - `-v`: print the names of the files being processed.
  - `-z`: use gzip compression or decompression.
  - `-j`: use bzip2 compression or decompression.

## gzip
- gzip stands for GNU zip.
- It is used to compress or decompress files using the Lempel-Ziv coding (LZ77) algorithm.
- Syntax: `gzip [options] file_name`
- Options:
  - `-c`: write the output to standard output and do not modify the original file.
  - `-d`: decompress the file instead of compressing it.
  - `-k`: keep the original file and create a new file with the .gz extension.
  - `-l`: list the compressed file name, size, ratio, and uncompressed size.
  - `-r`: recursively compress or decompress all files in a directory.

## cat
- cat stands for concatenate.
- It is used to read, write, or append data to files or standard input/output.
- Syntax: `cat [options] file_name`
- Options:
  - `-n`: number the output lines starting from 1.
  - `-b`: number the non-blank output lines starting from 1.
  - `-s`: suppress repeated empty output lines.
  - `-E`: display a $ at the end of each line.
  - `-T`: display TAB characters as ^I.

## more
- more is a command that displays the contents of a file or standard input one screen at a time.
- It allows the user to scroll forward and backward using the keyboard.
- Syntax: `more [options] file_name`
- Options:
  - `-d`: display a help message at the bottom of the screen.
  - `-l`: ignore form feed characters (^L) in the file.
  - `-s`: squeeze multiple blank lines into one.
  - `-u`: suppress underlining and bolding of text.
  - `+n`: start from the nth line of the file.

## less
- less is a command that displays the contents of a file or standard input one screen at a time.
- It allows the user to scroll forward and backward using the keyboard or mouse.
- It also supports searching and editing of the file or input.
- Syntax: `less [options] file_name`
- Options:
  - `-N`: display line numbers at the beginning of each line.
  - `-i`: ignore case in searches.
  - `-S`: chop long lines instead of wrapping them.
  - `-X`: do not clear the screen after exiting less.
  - `+F`: follow the end of the file as it grows.

## ps
- ps stands for process status.
- It is used to display information about the running processes on the system.
- Syntax: `ps [options]`
- Options:
  - `-a`: show all processes except session leaders and processes not associated with a terminal.
  - `-u`: show user-oriented format, including user name, CPU usage, memory usage, etc.
  - `-x`: show all processes, including those without a controlling terminal.
  - `-e`: show all processes, equivalent to -ax.
  - `-f`: show full format, including parent process ID, start time, command line, etc.

## sudo
- sudo stands for superuser do.
- It is used to execute commands as another user, usually the root or superuser.
- Syntax: `sudo [options] command`
- Options:
  - `-u`: specify the user name or ID to run the command as.
  - `-l`: list the commands that