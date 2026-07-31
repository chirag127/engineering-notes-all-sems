#### 1. Start Raspberry Pi and try various Linix commands in command terminal window: ls, cd, touch, mv, rm, man

- Raspberry Pi is a small, low-cost computer that can run Linux operating system and various applications.
- To start Raspberry Pi, you need to connect it to a power source, a monitor, a keyboard and a mouse. You also need to insert a microSD card with a pre-installed operating system image into the slot on the board.
- Once Raspberry Pi boots up, you will see a graphical user interface (GUI) on the monitor. You can use the mouse and the keyboard to interact with the GUI and launch different applications.
- To access the command terminal window, you can either click on the terminal icon on the desktop or press Ctrl+Alt+T on the keyboard. The command terminal window is a text-based interface that allows you to enter and execute Linux commands.
- Linux commands are case-sensitive and follow a specific syntax. The general format of a Linux command is:

  `command [options] [arguments]`

  - `command` is the name of the command that you want to execute, such as `ls`, `cd`, `touch`, etc.
  - `[options]` are optional parameters that modify the behavior of the command, such as `-a`, `-l`, `-r`, etc. They are usually preceded by a dash (-) or two dashes (--).
  - `[arguments]` are the inputs or targets of the command, such as file names, directory names, etc. They are usually separated by spaces.

- Some of the common Linux commands that you can try in the command terminal window are:

  - `ls`: This command lists the files and directories in the current working directory. You can use options such as `-a` to show hidden files, `-l` to show detailed information, `-r` to reverse the order, etc. You can also specify a different directory as an argument to list its contents, such as `ls /home/pi`.
  - `cd`: This command changes the current working directory to the one specified as an argument. For example, `cd /home/pi/Documents` will change the working directory to `/home/pi/Documents`. You can also use `.` to refer to the current directory and `..` to refer to the parent directory. For example, `cd ..` will move one level up in the directory hierarchy.
  - `touch`: This command creates a new, empty file with the name specified as an argument. For example, `touch test.txt` will create a file named `test.txt` in the current working directory. You can also use options such as `-a` to change the access time, `-m` to change the modification time, `-t` to specify a custom time, etc.
  - `mv`: This command moves or renames a file or directory. The first argument is the source file or directory and the second argument is the destination file or directory. For example, `mv test.txt new.txt` will rename the file `test.txt` to `new.txt`. You can also use options such as `-i` to prompt before overwriting, `-n` to not overwrite, `-f` to force overwrite, etc.
  - `rm`: This command removes or deletes a file or directory. The argument is the file or directory that you want to remove. For example, `rm test.txt` will delete the file `test.txt`. You can also use options such as `-i` to prompt before deleting, `-f` to force delete, `-r` to delete recursively, etc.
  - `man`: This command displays the manual page for a given command. The argument is the name of the command that you want to learn more about. For example, `man ls` will show the manual page for the `ls` command. You can use the arrow keys, the Page Up and Page Down keys, or the space bar to scroll through the manual page. You can press `q` to quit the manual page.