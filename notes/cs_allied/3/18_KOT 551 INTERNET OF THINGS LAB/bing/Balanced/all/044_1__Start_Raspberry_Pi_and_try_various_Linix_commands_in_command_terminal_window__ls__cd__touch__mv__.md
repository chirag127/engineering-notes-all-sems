# 1. Start Raspberry Pi and try various Linux commands in command terminal window: ls, cd, touch, mv, rm, man

- Raspberry Pi is a small computer that runs on Linux, a free and open-source operating system.
- To start Raspberry Pi, you need to connect it to a power source, a monitor, a keyboard, and a mouse. You also need to insert a microSD card with the Raspberry Pi OS installed on it.
- Once Raspberry Pi boots up, you will see a desktop environment with icons and menus. You can use the mouse and keyboard to interact with the graphical user interface (GUI).
- However, you can also use the command terminal window to execute commands and control the system. The command terminal window is a text-based interface that allows you to type commands and see the output.
- To open the command terminal window, you can either click on the terminal icon on the top left corner of the screen, or press Ctrl+Alt+T on the keyboard.
- The command terminal window will show a prompt that looks something like this:

```bash
pi@raspberrypi:~ $
```

- This means that you are logged in as the user `pi` on the computer `raspberrypi`, and you are in the home directory `~`.
- You can type commands after the prompt and press Enter to execute them. You can also use the arrow keys to navigate through the command history, and the Tab key to autocomplete the commands or filenames.
- Some of the basic Linux commands that you can try in the command terminal window are:

  - `ls`: This command lists the files and directories in the current directory. You can use the `-l` option to see more details, such as the size, permissions, owner, and modification date of each file or directory. You can also use the `-a` option to see the hidden files and directories, which start with a dot `.`. For example:

  ```bash
  pi@raspberrypi:~ $ ls -la
  total 40
  drwxr-xr-x  6 pi   pi   4096 Mar 16 04:13 .
  drwxr-xr-x  3 root root 4096 Mar 16 04:13 ..
  -rw-------  1 pi   pi     38 Mar 16 04:13 .bash_history
  -rw-r--r--  1 pi   pi    220 Mar 16 04:13 .bash_logout
  -rw-r--r--  1 pi   pi   3526 Mar 16 04:13 .bashrc
  drwx------  3 pi   pi   4096 Mar 16 04:13 .cache
  drwxr-xr-x  3 pi   pi   4096 Mar 16 04:13 Desktop
  drwxr-xr-x  2 pi   pi   4096 Mar 16 04:13 Documents
  drwxr-xr-x  2 pi   pi   4096 Mar 16 04:13 Downloads
  -rw-r--r--  1 pi   pi    807 Mar 16 04:13 .profile
  ```

  - `cd`: This command changes the current directory to the one specified as an argument. You can use `..` to go up one level, or `.` to stay in the same directory. You can also use `~` to go to the home directory, or `/` to go to the root directory. For example:

  ```bash
  pi@raspberrypi:~ $ cd Documents
  pi@raspberrypi:~/Documents $ cd ..
  pi@raspberrypi:~ $ cd /
  pi@raspberrypi:/ $ cd ~
  pi@raspberrypi:~ $
  ```

  - `touch`: This command creates a new empty file with the name specified as an argument. If the file already exists, it updates its modification date. For example:

  ```bash
  pi@raspberrypi:~ $ touch test.txt
  pi@raspberrypi:~ $ ls -l test.txt
  -rw-r--r-- 1 pi pi 0 Mar 16 04:13 test.txt
  ```

  - `mv`: This command moves or renames a file or directory. You need to specify the source and the destination as arguments. If the destination is a directory, the source will be moved into that directory. If the destination is a file, the source will be renamed to that file. For example:

  ```bash

```
