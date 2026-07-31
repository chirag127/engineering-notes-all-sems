# 1. Start Raspberry Pi and try various Linux commands in command terminal window: ls, cd, touch, mv, rm, man

- Raspberry Pi is a small, low-cost computer that can run Linux and other operating systems. It can be used for various projects, such as robotics, gaming, web servers, etc.
- To start Raspberry Pi, you need to connect it to a power source, a monitor, a keyboard, and a mouse. You also need to insert a microSD card with a Linux operating system installed on it. The Raspberry Pi will boot up and display a graphical user interface (GUI) or a command line interface (CLI), depending on the operating system you chose.
- To access the command terminal window, you can either use a keyboard shortcut (Ctrl+Alt+T) or click on the terminal icon on the GUI. The command terminal window is where you can type and execute Linux commands to perform various tasks on your Raspberry Pi.
- Linux commands are case-sensitive and follow a specific syntax. The general format of a Linux command is:

  `command [options] [arguments]`

  - `command` is the name of the command you want to execute, such as `ls`, `cd`, `touch`, etc.
  - `[options]` are optional parameters that modify the behavior of the command, such as `-a`, `-l`, `-r`, etc. They usually start with a hyphen (-) and can be combined together, such as `-al`.
  - `[arguments]` are optional inputs that the command operates on, such as file names, directory names, etc.

- Some of the most common and useful Linux commands are:

  - `ls`: This command lists the contents of a directory. By default, it lists the contents of the current working directory, which is the directory you are currently in. You can also specify a different directory as an argument, such as `ls /home/pi`. Some of the options you can use with `ls` are:

    - `-a`: This option shows all files and directories, including hidden ones that start with a dot (.).
    - `-l`: This option shows the long format of the listing, which includes more information, such as permissions, ownership, size, date, etc.
    - `-r`: This option reverses the order of the listing, which is usually alphabetical.
    - `-t`: This option sorts the listing by modification time, with the newest first.

  - `cd`: This command changes the current working directory to a different one. You can specify the new directory as an argument, such as `cd /home/pi/Documents`. You can also use some special symbols to navigate the directory structure, such as:

    - `.`: This symbol represents the current working directory.
    - `..`: This symbol represents the parent directory of the current working directory.
    - `~`: This symbol represents the home directory of the current user, which is usually `/home/pi` on Raspberry Pi.
    - `-`: This symbol represents the previous working directory.

  - `touch`: This command creates a new, empty file with the name specified as an argument, such as `touch hello.txt`. If the file already exists, it updates its modification time to the current time. You can also use some options with `touch`, such as:

    - `-a`: This option changes only the access time of the file, which is the last time the file was read.
    - `-m`: This option changes only the modification time of the file, which is the last time the file was written.
    - `-t`: This option sets the access and modification times of the file to a specific date and time, which you can specify in the format `[[CC]YY]MMDDhhmm[.ss]`, where CC is the century, YY is the year, MM is the month, DD is the day, hh is the hour, mm is the minute, and ss is the second.

  - `mv`: This command moves or renames a file or a directory. You need to specify the source and the destination as arguments, such as `mv hello.txt goodbye.txt` or `mv hello.txt /home/pi/Documents`. Some of the options you can use with `mv` are:

    - `-i`: This option prompts you before overwriting an existing file or directory with the same name as the destination.
    - `-n`: This option prevents overwriting an existing file or directory with the same name as the destination.
    - `-f`: This option forces overwriting an existing file or directory with the same name as the destination, without prompting you.

  - `rm`: This command removes or deletes a file or a directory. You need to specify the file or directory