# 1. Start Raspberry Pi and try various Linux commands in command terminal window: ls, cd, touch, mv, rm, man

- Raspberry Pi is a small computer that can run Linux operating systems such as Raspbian, Ubuntu, or Debian.
- To start Raspberry Pi, you need to connect it to a power source, a monitor, a keyboard, and a mouse. You also need to insert a microSD card with a Linux operating system installed on it.
- Once Raspberry Pi boots up, you will see a desktop environment or a command line interface, depending on the operating system you are using.
- To open a command terminal window, you can either click on the terminal icon on the desktop or press Ctrl+Alt+T on the keyboard.
- In the command terminal window, you can type various Linux commands to perform different tasks. Here are some of the common commands and their functions:

  - `ls`: This command lists the files and directories in the current working directory. You can use options such as `-l` to show more details, `-a` to show hidden files, or `-h` to show human-readable sizes.
  - `cd`: This command changes the current working directory to the one specified. You can use `.` to refer to the current directory, `..` to refer to the parent directory, or `~` to refer to the home directory. For example, `cd ..` will move you one level up from the current directory.
  - `touch`: This command creates a new empty file with the name specified. For example, `touch hello.txt` will create a file named hello.txt in the current directory.
  - `mv`: This command moves or renames a file or directory. You need to specify the source and the destination. For example, `mv hello.txt goodbye.txt` will rename the file hello.txt to goodbye.txt. `mv hello.txt ~/Documents` will move the file hello.txt to the Documents directory in the home directory.
  - `rm`: This command removes or deletes a file or directory. You need to specify the name of the file or directory to be removed. For example, `rm hello.txt` will delete the file hello.txt. `rm -r Documents` will delete the Documents directory and all its contents. Be careful with this command as there is no undo option.
  - `man`: This command shows the manual page for a command or a topic. You can use it to learn more about the syntax, options, and examples of a command. For example, `man ls` will show the manual page for the ls command. You can use the arrow keys to scroll up and down, and press Q to quit.