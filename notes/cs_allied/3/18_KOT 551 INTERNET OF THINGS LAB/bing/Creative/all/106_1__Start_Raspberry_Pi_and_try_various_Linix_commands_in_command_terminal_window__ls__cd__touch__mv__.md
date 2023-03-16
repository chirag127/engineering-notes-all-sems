# 1. Start Raspberry Pi and try various Linux commands in command terminal window: ls, cd, touch, mv, rm, man

- Raspberry Pi is a small, low-cost computer that can run Linux, a free and open-source operating system.
- To start Raspberry Pi, you need to connect it to a power source, a monitor, a keyboard, and a mouse. You also need to insert a microSD card with a Linux operating system installed on it.
- Once Raspberry Pi boots up, you will see a graphical user interface (GUI) with icons and menus. You can use the mouse and keyboard to interact with the GUI.
- To open a command terminal window, you can either click on the terminal icon on the desktop or the menu bar, or press Ctrl+Alt+T on the keyboard.
- A command terminal window is a text-based interface that allows you to enter commands and see the output. You can use the terminal to perform various tasks on Raspberry Pi, such as creating, moving, deleting, and viewing files and folders.
- Linux commands are case-sensitive, meaning that uppercase and lowercase letters are treated differently. For example, `ls` and `LS` are not the same command.
- Linux commands can have options and arguments. Options are preceded by a dash (-) and modify the behavior of the command. Arguments are the values or names that the command operates on. For example, `ls -l /home/pi` is a command that lists the files and folders in the `/home/pi` directory in a long format.
- Some of the most common and useful Linux commands are:

  - `ls`: lists the files and folders in the current directory or a specified directory. For example, `ls /home/pi` lists the files and folders in the `/home/pi` directory.
  - `cd`: changes the current directory to a specified directory. For example, `cd /home/pi` changes the current directory to `/home/pi`.
  - `touch`: creates a new, empty file with a specified name. For example, `touch test.txt` creates a new file named `test.txt` in the current directory.
  - `mv`: moves or renames a file or folder. For example, `mv test.txt test2.txt` renames the file `test.txt` to `test2.txt`. `mv test.txt /home/pi/Documents` moves the file `test.txt` from the current directory to the `/home/pi/Documents` directory.
  - `rm`: removes or deletes a file or folder. For example, `rm test.txt` deletes the file `test.txt` from the current directory. `rm -r test` deletes the folder `test` and all its contents from the current directory.
  - `man`: displays the manual page for a command or a topic. For example, `man ls` displays the manual page for the `ls` command. `man man` displays the manual page for the `man` command. You can use the arrow keys, Page Up, Page Down, Home, End, and Q keys to navigate and exit the manual page.