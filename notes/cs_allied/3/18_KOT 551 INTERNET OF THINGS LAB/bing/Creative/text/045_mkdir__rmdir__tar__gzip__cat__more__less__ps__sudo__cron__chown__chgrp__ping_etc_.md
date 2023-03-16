# Linux Commands

## mkdir
- mkdir stands for make directory.
- It is used to create a new directory or folder in the current working directory or in a specified path.
- Syntax: `mkdir [options] directory_name`
- Example: `mkdir test` will create a folder named test in the current directory.
- Options: 
  - `-p` or `--parents` will create parent directories as needed.
  - `-v` or `--verbose` will print a message for each created directory.
  - `-m` or `--mode` will set the file mode (permissions) of the created directory.

## rmdir
- rmdir stands for remove directory.
- It is used to delete an empty directory or folder.
- Syntax: `rmdir [options] directory_name`
- Example: `rmdir test` will delete the folder named test if it is empty.
- Options: 
  - `-p` or `--parents` will remove directory and its ancestors.
  - `-v` or `--verbose` will print a message for each removed directory.
  - `--ignore-fail-on-non-empty` will ignore errors when trying to remove non-empty directories.

## tar
- tar stands for tape archive.
- It is used to create or extract compressed archive files that contain multiple files or directories.
- Syntax: `tar [options] [archive_file] [file_or_directory ...]`
- Example: `tar -czvf test.tar.gz test` will create a compressed archive file named test.tar.gz that contains the folder test and its contents.
- Options: 
  - `-c` or `--create` will create a new archive file.
  - `-x` or `--extract` or `--get` will extract files from an archive file.
  - `-z` or `--gzip` or `--gunzip` or `--ungzip` will use gzip compression or decompression.
  - `-v` or `--verbose` will print the names of the files being processed.
  - `-f` or `--file` will specify the name of the archive file.
  - `-t` or `--list` will list the contents of an archive file.

## gzip
- gzip stands for GNU zip.
- It is used to compress or decompress files using the Lempel-Ziv coding (LZ77) algorithm.
- Syntax: `gzip [options] [file ...]`
- Example: `gzip test.txt` will compress the file test.txt and rename it to test.txt.gz.
- Options: 
  - `-d` or `--decompress` or `--uncompress` will decompress the file.
  - `-k` or `--keep` will keep the original file and not delete it.
  - `-l` or `--list` will list the compressed file name, size, ratio, uncompressed size, and modification date.
  - `-r` or `--recursive` will recursively compress or decompress all files in a directory and its subdirectories.
  - `-t` or `--test` will test the integrity of the compressed file.

## cat
- cat stands for concatenate.
- It is used to display the contents of a file or multiple files, or to concatenate files and redirect the output to another file or device.
- Syntax: `cat [options] [file ...]`
- Example: `cat test.txt` will display the contents of test.txt on the standard output (screen).
- Options: 
  - `-b` or `--number-nonblank` will number the non-blank output lines.
  - `-n` or `--number` will number all the output lines.
  - `-s` or `--squeeze-blank` will suppress repeated empty output lines.
  - `-E` or `--show-ends` will display a $ at the end of each line.
  - `-T` or `--show-tabs` will display TAB characters as ^I.

## more
- more is a command that displays the contents of a file or multiple files one screen at a time.
- Syntax: `more [options] [file ...]`
- Example: `more test.txt` will display the contents of test.txt one screen at a time and wait for the user to press a key to continue or quit.
- Options: 
  - `-d` or `--silent` or `--quiet` will print a message instead of ringing the bell when an invalid key is pressed.
  - `-l` or `--logical` will count logical rather than screen lines.
  - `-p` or `--clean` or `--print-over` will not scroll the screen, but clear it and then display the text.