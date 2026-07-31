# 1. Start Raspberry Pi and try various Linux commands in command terminal window: ls, cd, touch, mv, rm, man

- Raspberry Pi is a small, low-cost computer that can run Linux and other operating systems. It can be used for various projects, such as robotics, gaming, web servers, etc.
- To start Raspberry Pi, you need to connect it to a power source, a monitor, a keyboard, and a mouse. You also need to insert a microSD card with a Linux operating system installed on it. The Raspberry Pi will boot up and display a graphical user interface (GUI) or a command line interface (CLI) depending on the operating system.
- To access the command terminal window, you can either use a keyboard shortcut (Ctrl+Alt+T) or click on the terminal icon on the GUI. The command terminal window is where you can type and execute Linux commands to perform various tasks on the Raspberry Pi.
- Linux commands are case-sensitive and follow a specific syntax. The general format of a Linux command is:

  `command [options] [arguments]`

  - `command` is the name of the command you want to execute, such as `ls`, `cd`, `touch`, etc.
  - `[options]` are optional parameters that modify the behavior of the command, such as `-a`, `-l`, `-r`, etc. They usually start with a hyphen (-) and can be combined together, such as `-al`.
  - `[arguments]` are optional inputs that the command operates on, such as file names, directory names, etc.

- Some of the common Linux commands that you can try on the Raspberry Pi are:

  - `ls`: This command lists the files and directories in the current working directory or in a specified directory. Some of the options you can use with this command are:

    - `-a`: This option shows all the files and directories, including the hidden ones that start with a dot (.).
    - `-l`: This option shows the long listing format, which includes the file permissions, owner, group, size, date, and time of each file and directory.
    - `-r`: This option reverses the order of the listing, which is normally alphabetical.
    - `-t`: This option sorts the listing by the modification time of each file and directory, from the newest to the oldest.

    For example, `ls -alrt` will list all the files and directories in the current working directory in the long listing format, sorted by the modification time in reverse order.

  - `cd`: This command changes the current working directory to a specified directory. If no directory is specified, it changes to the home directory of the current user. Some of the arguments you can use with this command are:

    - `.`: This argument represents the current working directory.
    - `..`: This argument represents the parent directory of the current working directory.
    - `~`: This argument represents the home directory of the current user.
    - `/`: This argument represents the root directory of the file system.

    For example, `cd ..` will change the current working directory to the parent directory of the current working directory.

  - `touch`: This command creates a new empty file or updates the modification time of an existing file. The argument for this command is the name of the file you want to create or update. If the file does not exist, it will be created. If the file exists, its modification time will be updated to the current time.

    For example, `touch test.txt` will create a new empty file named test.txt or update its modification time if it already exists.

  - `mv`: This command moves or renames a file or a directory. The arguments for this command are the source file or directory and the destination file or directory. If the destination is a directory, the source file or directory will be moved into that directory. If the destination is a file, the source file or directory will be renamed to that file name.

    For example, `mv test.txt test2.txt` will rename the file test.txt to test2.txt. `mv test.txt Documents` will move the file test.txt to the Documents directory.

  - `rm`: This command removes or deletes a file or a directory. The argument for this command is the name of the file or directory you want to remove or delete. Some of the options you can use with this command are:

    - `-i`: This option prompts you for confirmation before removing or deleting each file or directory.
    - `-r`: This option recursively removes or deletes a directory and all its contents, including subdirectories and files.
    - `-f`: This option forces the removal or deletion of a file or directory without prompting