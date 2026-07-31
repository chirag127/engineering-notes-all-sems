#### 1. Start Raspberry Pi and try various Linux commands in command terminal window: ls, cd, touch, mv, rm, man

- Raspberry Pi is a small, low-cost computer that can run Linux, a free and open-source operating system.
- To start Raspberry Pi, you need to connect it to a power source, a monitor, a keyboard, and a mouse. You also need to insert a microSD card with a Linux operating system installed on it.
- Once Raspberry Pi boots up, you will see a graphical user interface (GUI) with icons and menus. You can use the mouse and keyboard to interact with the GUI.
- To open a command terminal window, you can either click on the terminal icon on the desktop or the menu bar, or press Ctrl+Alt+T on the keyboard.
- A command terminal window is a text-based interface that allows you to enter commands and see the output. You can use the keyboard to type commands and press Enter to execute them.
- Linux commands are case-sensitive, meaning that uppercase and lowercase letters are different. For example, `ls` and `LS` are not the same command.
- Linux commands can have options and arguments. Options are preceded by a dash (-) and modify the behavior of the command. Arguments are the input or output of the command. For example, `ls -l /home/pi` is a command that lists the files and directories in the /home/pi directory in a long format.
- Some of the most common and useful Linux commands are:

  - `ls`: lists the files and directories in the current directory or a specified directory. Some of the options are:
    - `-a`: shows all files and directories, including hidden ones that start with a dot (.).
    - `-l`: shows the files and directories in a long format, with details such as permissions, owner, size, and modification date.
    - `-h`: shows the file sizes in a human-readable format, such as KB, MB, or GB.
  - `cd`: changes the current directory to a specified directory. For example, `cd /home/pi` changes the current directory to /home/pi. Some of the special directories are:
    - `.`: the current directory.
    - `..`: the parent directory of the current directory.
    - `~`: the home directory of the current user.
    - `/`: the root directory of the file system.
  - `touch`: creates a new, empty file with a specified name. For example, `touch hello.txt` creates a file named hello.txt in the current directory.
  - `mv`: moves or renames a file or directory. For example, `mv hello.txt goodbye.txt` renames the file hello.txt to goodbye.txt. `mv hello.txt /home/pi/Documents` moves the file hello.txt to the /home/pi/Documents directory.
  - `rm`: removes or deletes a file or directory. For example, `rm hello.txt` deletes the file hello.txt. `rm -r /home/pi/Documents` deletes the /home/pi/Documents directory and all its contents. Be careful with this command, as there is no undo option.
  - `man`: shows the manual page for a command or a topic. For example, `man ls` shows the manual page for the ls command. `man -k keyword` shows the manual pages that contain the keyword. To exit the manual page, press Q.