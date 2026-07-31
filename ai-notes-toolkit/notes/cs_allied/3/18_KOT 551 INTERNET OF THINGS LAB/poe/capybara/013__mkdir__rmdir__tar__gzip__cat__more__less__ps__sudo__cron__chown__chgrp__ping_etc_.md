#### mkdir, rmdir, tar, gzip, cat, more, less, ps, sudo, cron, chown, chgrp, ping etc.

Here is a brief overview of some of the most commonly used Linux commands:

1. **mkdir:** This command is used to create a new directory or folder. For example, if you want to create a directory named 'docs', you can type `mkdir docs`.

2. **rmdir:** This command is used to remove a directory. However, the directory must be empty before it can be removed. For example, if you want to remove the 'docs' directory created earlier, you can type `rmdir docs`.

3. **tar:** This command is used to create an archive of files and directories. It can also be used to extract files from an archive. For example, to create an archive of all the files in the 'docs' directory, you can type `tar -cvf docs.tar docs`.

4. **gzip:** This command is used to compress files. It is often used in conjunction with the tar command to create compressed archives. For example, to compress the 'docs' archive created earlier, you can type `gzip docs.tar`.

5. **cat:** This command is used to display the contents of a file. For example, to display the contents of a file named 'file.txt', you can type `cat file.txt`.

6. **more:** This command is used to display the contents of a file one page at a time. For example, to display the contents of a file named 'file.txt' one page at a time, you can type `more file.txt`.

7. **less:** This command is similar to the 'more' command, but it allows you to scroll through the file using the arrow keys. For example, to display the contents of a file named 'file.txt' using the less command, you can type `less file.txt`.

8. **ps:** This command is used to display information about the processes running on the system. For example, to display information about all the processes running on the system, you can type `ps -ef`.

9. **sudo:** This command is used to run commands with administrative privileges. For example, to run the 'mkdir' command with administrative privileges, you can type `sudo mkdir docs`.

10. **cron:** This command is used to schedule commands to run at specific times. For example, to schedule a command to run every day at 3am, you can edit the crontab file using the command `crontab -e` and add the line `0 3 * * * command`.

11. **chown:** This command is used to change the owner of a file or directory. For example, to change the owner of a file named 'file.txt' to user 'john', you can type `sudo chown john file.txt`.

12. **chgrp:** This command is used to change the group of a file or directory. For example, to change the group of a file named 'file.txt' to group 'users', you can type `sudo chgrp users file.txt`.

13. **ping:** This command is used to check the connectivity between two network devices. For example, to check the connectivity between your computer and a server with IP address '192.168.1.1', you can type `ping 192.168.1.1`.