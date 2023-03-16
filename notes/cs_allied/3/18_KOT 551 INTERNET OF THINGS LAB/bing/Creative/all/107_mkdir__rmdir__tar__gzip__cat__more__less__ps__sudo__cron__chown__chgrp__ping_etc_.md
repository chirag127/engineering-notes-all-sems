# Linux Commands

## mkdir
- mkdir stands for make directory.
- It is used to create new directories in the file system.
- Syntax: `mkdir [options] directory_name`
- Options:
  - `-p`: create parent directories if they do not exist.
  - `-v`: print a message for each created directory.
  - `-m`: set the mode (permissions) of the created directory.
- Examples:
  - `mkdir mydir`: create a directory named mydir in the current working directory.
  - `mkdir -p /home/user/mydir`: create a directory named mydir and its parent directories if they do not exist.
  - `mkdir -v -m 755 mydir`: create a directory named mydir with read, write and execute permissions for the owner, and read and execute permissions for the group and others, and print a message.

## rmdir
- rmdir stands for remove directory.
- It is used to delete empty directories from the file system.
- Syntax: `rmdir [options] directory_name`
- Options:
  - `-p`: remove directory and its empty parent directories.
  - `-v`: print a message for each removed directory.
- Examples:
  - `rmdir mydir`: remove a directory named mydir if it is empty.
  - `rmdir -p /home/user/mydir`: remove a directory named mydir and its empty parent directories.
  - `rmdir -v mydir`: remove a directory named mydir if it is empty and print a message.

## tar
- tar stands for tape archive.
- It is used to create or extract compressed archive files.
- Syntax: `tar [options] [archive_file] [file1 file2 ...]`
- Options:
  - `-c`: create a new archive file.
  - `-x`: extract files from an archive file.
  - `-v`: print the names of the files being processed.
  - `-f`: specify the name of the archive file.
  - `-z`: use gzip compression or decompression.
  - `-j`: use bzip2 compression or decompression.
- Examples:
  - `tar -cvzf myarchive.tar.gz file1 file2 file3`: create a gzip compressed archive file named myarchive.tar.gz containing file1, file2 and file3, and print the names of the files being processed.
  - `tar -xvzf myarchive.tar.gz`: extract files from a gzip compressed archive file named myarchive.tar.gz, and print the names of the files being extracted.
  - `tar -cjf myarchive.tar.bz2 file1 file2 file3`: create a bzip2 compressed archive file named myarchive.tar.bz2 containing file1, file2 and file3.
  - `tar -xjf myarchive.tar.bz2`: extract files from a bzip2 compressed archive file named myarchive.tar.bz2.

## gzip
- gzip stands for GNU zip.
- It is used to compress or decompress files using the Lempel-Ziv coding (LZ77) algorithm.
- Syntax: `gzip [options] [file1 file2 ...]`
- Options:
  - `-c`: write the compressed output to the standard output, and do not delete the original files.
  - `-d`: decompress the files, and do not delete the compressed files.
  - `-k`: keep the original files, and do not delete them after compression or decompression.
  - `-l`: list the compressed file name, compression ratio, uncompressed size, compressed size and uncompressed name for each file.
  - `-r`: recursively compress or decompress all files in the specified directories.
  - `-v`: print the name and percentage reduction for each file.
- Examples:
  - `gzip file1 file2 file3`: compress file1, file2 and file3, and replace them with file1.gz, file2.gz and file3.gz.
  - `gzip -d file1.gz file2.gz file3.gz`: decompress file1.gz, file2.gz and file3.gz, and replace them with file1, file2 and file3.
  - `gzip -c file1 > file1.gz`: compress file1 and write the output to file1.gz, and do not delete file1.
  - `gzip -l file1.gz`: list the compressed file name, compression ratio, uncompressed size, compressed size and uncompressed name for file1.gz.
  - `gzip -r mydir`: recursively compress all files in mydir and its subdirectories.

## cat
- cat stands for concatenate.
- It is used to read, write or append data to files, or to concatenate files.
- Syntax: `cat [options