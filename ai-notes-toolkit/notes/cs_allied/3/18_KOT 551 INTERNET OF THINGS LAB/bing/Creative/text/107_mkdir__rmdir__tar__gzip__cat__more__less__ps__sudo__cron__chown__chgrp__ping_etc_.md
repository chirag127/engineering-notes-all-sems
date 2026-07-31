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
  - `-p`: remove directory and its ancestors if they are empty.
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
  - `-c`: write the compressed output to standard output.
  - `-d`: decompress the file instead of compressing it.
  - `-k`: keep the original file and create a new compressed file.
  - `-l`: list the compressed file name, size, ratio, and uncompressed size.
  - `-r`: recursively compress or decompress files in directories.

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
- Syntax: `more [options] file_name`
- Options:
  - `-d`: display a help message at the bottom of the screen.
  - `-l`: ignore form feed characters (^L) in the file.
  - `-s`: squeeze multiple blank lines into one.
  - `-u`: suppress underlining and bolding of text.
- Commands:
  - `Space`: display the next screen of text.
  - `Enter`: display the next line of text.
  - `b`: go back one screen of text.
  - `q`: quit more and return to the shell.

## less
- less is a command that displays the contents of a file or standard input one screen at a time, with more features than more.
- Syntax: `less [options] file_name`
- Options:
  - `-N`: display line numbers at the beginning of each line.
  - `-i`: ignore case in searches.
  - `-S`: chop long lines instead of wrapping them.
  - `-X`: do not clear the screen after quitting less.
- Commands:
  - `Space`: display the next screen of text.
  - `Enter`: display the next line of text.
  - `b`: go back one screen of text.
  - `q`: quit less and return to the shell.
  - `/pattern`: search forward for a pattern in the file.
  - `?pattern`: search backward for a pattern in the file.
  - `n`: repeat the previous search in the same direction.
  - `N`: repeat the previous search in the opposite direction.

## ps
- ps stands for process status.
- It is used to display information about the processes running on the system.
- Syntax: `ps [options]`
- Options:
  - `-e`: display information about all processes.
  - `-f`: display full format listing, including command line arguments and parent process ID.
  - `-l`: display long format listing, including priority, nice value, and memory usage.
  - `-u user`: display information about processes owned by a specific user.
  - `-p pid`: display information about a specific process ID.