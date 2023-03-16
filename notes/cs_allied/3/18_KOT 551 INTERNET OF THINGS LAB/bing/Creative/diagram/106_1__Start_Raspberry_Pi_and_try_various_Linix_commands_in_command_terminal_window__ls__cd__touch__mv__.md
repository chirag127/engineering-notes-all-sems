# Start Raspberry Pi and try various Linux commands in command terminal window: ls, cd, touch, mv, rm, man

- Raspberry Pi is a small, low-cost computer that can run Linux operating system and various applications.
- To start Raspberry Pi, you need to connect it to a power source, a monitor, a keyboard, and a mouse. You also need to insert a microSD card with a pre-installed operating system image into the slot on the board.
- Once the Raspberry Pi boots up, you will see a graphical user interface (GUI) on the monitor. You can use the mouse and the keyboard to interact with the GUI and launch different programs.
- To access the command terminal window, you can either click on the terminal icon on the desktop or press Ctrl+Alt+T on the keyboard. The command terminal window is a text-based interface that allows you to enter commands and execute them.
- Linux commands are case-sensitive and follow a specific syntax. The general format of a Linux command is:

```bash
command [options] [arguments]
```

- The command is the name of the program or function that you want to run. The options are optional flags that modify the behavior of the command. The arguments are the inputs or parameters that the command operates on.
- Some of the common Linux commands that you can try in the command terminal window are:

  - `ls`: This command lists the files and directories in the current working directory or in a specified directory. Some of the options that you can use with `ls` are:

    - `-a`: This option shows all files and directories, including the hidden ones that start with a dot (.)
    - `-l`: This option shows the long listing format, which includes the file permissions, owner, group, size, date, and name.
    - `-h`: This option shows the file sizes in a human-readable format, such as KB, MB, GB, etc.

    For example, `ls -alh` will show all files and directories in the current working directory in the long listing format with human-readable sizes.

  - `cd`: This command changes the current working directory to a specified directory. You can use either an absolute path or a relative path to specify the directory. An absolute path starts with a slash (/) and specifies the location of the directory from the root of the file system. A relative path specifies the location of the directory from the current working directory. Some of the special characters that you can use with `cd` are:

    - `.`: This character represents the current working directory.
    - `..`: This character represents the parent directory of the current working directory.
    - `~`: This character represents the home directory of the current user.

    For example, `cd /home/pi` will change the current working directory to the home directory of the user pi. `cd ..` will change the current working directory to the parent directory of the current working directory. `cd ~` will change the current working directory to the home directory of the current user.

  - `touch`: This command creates a new empty file or updates the access and modification times of an existing file. You can specify one or more file names as arguments. For example, `touch file1 file2` will create two new empty files named file1 and file2 in the current working directory. If the files already exist, their access and modification times will be updated to the current time.

  - `mv`: This command moves or renames a file or a directory. You can specify the source file or directory and the destination file or directory as arguments. If the destination is an existing directory, the source file or directory will be moved into that directory. If the destination is an existing file, the source file will overwrite that file. If the destination does not exist, the source file or directory will be renamed to that name. For example, `mv file1 file2` will rename the file file1 to file2. `mv file1 dir1` will move the file file1 into the directory dir1. `mv dir1 dir2` will rename the directory dir1 to dir2.

  - `rm`: This command removes or deletes a file or a directory. You can specify one or more file or directory names as arguments. Some of the options that you can use with `rm` are:

    - `-i`: This option prompts for confirmation before deleting each file or directory.
    - `-r`: This option recursively deletes all files and directories inside a directory.
    - `-f`: This option forces the deletion of files and directories without prompting or showing errors.

    For example, `rm -i file1` will ask for confirmation before deleting the file file1. `rm -r dir1