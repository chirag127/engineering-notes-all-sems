# mkdir, rmdir, tar, g

- mkdir is a command that creates (or makes) a directory. You supply the name of the directory as an argument   .
- rmdir is a command that removes (or deletes) a directory, but only if it is empty (i.e., contains no files or subdirectories)  .
- tar is a command that creates or extracts compressed archive files, which are also known as tarballs. Tarballs are often used to store and distribute files on Linux systems.
- g is not a command, but a common suffix for gzip-compressed files, such as .tar.gz or .tgz. Gzip is a program that compresses and decompresses files using the Lempel-Ziv algorithm.

## Examples

- To create a single directory named newDir, you can use the command:

`mkdir newDir`

- To create multiple directories named newDir1, newDir2, and newDir3, you can use the command:

`mkdir newDir1 newDir2 newDir3`

- To remove an empty directory named oldDir, you can use the command:

`rmdir oldDir`

- To create a compressed archive file named backup.tar.gz from the files in the current directory, you can use the command:

`tar czvf backup.tar.gz .`

- To extract the files from the compressed archive file named backup.tar.gz to a new directory named backup, you can use the commands:

`mkdir backup`

`tar xzvf backup.tar.gz -C backup`