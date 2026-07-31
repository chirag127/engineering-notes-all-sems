# Start Raspberry Pi and try various Linux commands in command terminal window: ls, cd, touch, mv, rm, man

- Raspberry Pi is a small computer that runs on Linux, a free and open-source operating system.
- To start Raspberry Pi, you need to connect it to a power source, a monitor, a keyboard, and a mouse. You also need to insert a microSD card with the operating system installed on it.
- Once Raspberry Pi boots up, you will see a desktop environment with icons and menus. You can use the mouse and keyboard to interact with the graphical user interface (GUI).
- To open a command terminal window, you can either click on the terminal icon on the taskbar, or press Ctrl+Alt+T on the keyboard. A command terminal window is a text-based interface that allows you to enter commands and see the output.
- Linux commands are case-sensitive, meaning that uppercase and lowercase letters matter. For example, `ls` and `LS` are different commands.
- Linux commands can have options and arguments. Options are preceded by a dash (-) and modify the behavior of the command. Arguments are the input or output of the command. For example, `ls -l /home/pi` is a command that lists the files and directories in the /home/pi directory in a long format.
- Some of the most common and useful Linux commands are:

  - `ls`: lists the files and directories in the current directory or the specified directory. Some of the options are:
    - `-a`: shows all files and directories, including hidden ones that start with a dot (.).
    - `-l`: shows the file and directory attributes, such as size, owner, permissions, and modification date.
    - `-h`: shows the file sizes in a human-readable format, such as KB, MB, GB, etc.
  - `cd`: changes the current directory to the specified directory. Some of the special directories are:
    - `.`: the current directory.
    - `..`: the parent directory of the current directory.
    - `~`: the home directory of the current user.
    - `/`: the root directory of the file system.
  - `touch`: creates a new empty file with the specified name, or updates the modification date of an existing file. For example, `touch test.txt` creates a new file named test.txt in the current directory, or updates its modification date if it already exists.
  - `mv`: moves or renames a file or directory. The syntax is `mv source destination`, where source is the file or directory to be moved or renamed, and destination is the new location or name. For example, `mv test.txt Documents` moves the file test.txt from the current directory to the Documents directory, and `mv test.txt new.txt` renames the file test.txt to new.txt in the current directory.
  - `rm`: removes or deletes a file or directory. The syntax is `rm file` or `rm -r directory`, where file is the file to be removed, and directory is the directory to be removed recursively, meaning that all its contents will be deleted as well. For example, `rm test.txt` deletes the file test.txt from the current directory, and `rm -r Documents` deletes the Documents directory and all its contents from the current directory. Be careful with this command, as there is no undo option.
  - `man`: shows the manual page for a command or a topic. The manual page contains the description, syntax, options, arguments, examples, and other information about the command or topic. The syntax is `man command` or `man topic`, where command is the command to be looked up, and topic is the topic to be looked up. For example, `man ls` shows the manual page for the ls command, and `man intro` shows the introduction to Linux commands. To exit the manual page, press Q on the keyboard.