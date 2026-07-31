# Header Diagram

## mkdir
- mkdir is a command that creates a new directory in the current working directory or a specified path.
- The syntax of mkdir is `mkdir [options] directory_name`.
- Some common options are:
  - -p: create parent directories as needed
  - -v: print a message for each created directory
  - -m: set the file mode (permissions) of the created directory

## rmdir
- rmdir is a command that removes an empty directory in the current working directory or a specified path.
- The syntax of rmdir is `rmdir [options] directory_name`.
- Some common options are:
  - -p: remove directory and its ancestors
  - -v: print a message for each removed directory
  - --ignore-fail-on-non-empty: ignore errors when trying to remove non-empty directories

## tar
- tar is a command that creates or extracts compressed archive files that contain multiple files or directories.
- The syntax of tar is `tar [options] [archive_file] [file_or_directory ...]`.
- Some common options are:
  - -c: create a new archive file
  - -x: extract files from an archive file
  - -z: use gzip compression or decompression
  - -v: print the names of files processed
  - -f: specify the name of the archive file

## g
- g is not a valid command in Linux. Perhaps you meant grep, which is a command that searches for a pattern in a file or input stream and prints the matching lines.
- The syntax of grep is `grep [options] pattern [file ...]`.
- Some common options are:
  - -i: ignore case distinctions
  - -v: invert the sense of matching, to select non-matching lines
  - -n: print line numbers with output lines
  - -c: print only a count of matching lines per file