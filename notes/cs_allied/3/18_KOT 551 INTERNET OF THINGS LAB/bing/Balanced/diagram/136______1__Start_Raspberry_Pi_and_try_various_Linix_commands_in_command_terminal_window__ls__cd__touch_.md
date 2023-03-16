#### 1. Start Raspberry Pi and try various Linux commands in command terminal window: ls, cd, touch, mv, rm, man

- Raspberry Pi is a small computer that runs on Linux, a free and open source operating system.
- To start Raspberry Pi, you need to connect it to a power source, a monitor, a keyboard, and a mouse. You also need to insert a microSD card with the Raspberry Pi OS installed on it.
- Once Raspberry Pi boots up, you will see a desktop environment with icons and menus. You can use the mouse and keyboard to interact with the graphical user interface (GUI).
- However, you can also use the command terminal window to execute commands and perform tasks using text. The command terminal window is a program that lets you access the Linux shell, which is a program that interprets your commands and communicates with the operating system.
- To open the command terminal window, you can either click on the terminal icon on the taskbar, or press Ctrl+Alt+T on the keyboard.
- In the command terminal window, you will see a prompt that looks something like this:

```bash
pi@raspberrypi:~ $
```

- This prompt tells you the username (`pi`), the hostname (`raspberrypi`), and the current working directory (`~`, which is a shortcut for `/home/pi`).
- You can type commands after the prompt and press Enter to execute them. The commands are case-sensitive, so make sure you type them correctly.
- Here are some basic Linux commands that you can try in the command terminal window:

  - `ls`: This command lists the files and directories in the current working directory. You can use the `-l` option to see more details, such as the size, permissions, owner, and modification date of each file and directory. You can also use the `-a` option to see hidden files and directories, which start with a dot (`.`). For example:

  ```bash
  pi@raspberrypi:~ $ ls -la
  total 36
  drwxr-xr-x  5 pi   pi   4096 Mar 16 06:04 .
  drwxr-xr-x  3 root root 4096 Jan  1  1970 ..
  -rw-------  1 pi   pi    119 Mar 16 06:04 .bash_history
  -rw-r--r--  1 pi   pi    220 Jan  1  1970 .bash_logout
  -rw-r--r--  1 pi   pi   3523 Jan  1  1970 .bashrc
  drwxr-xr-x  2 pi   pi   4096 Mar 16 06:04 Desktop
  drwxr-xr-x  2 pi   pi   4096 Mar 16 06:04 Documents
  drwxr-xr-x  2 pi   pi   4096 Mar 16 06:04 Downloads
  -rw-r--r--  1 pi   pi    807 Jan  1  1970 .profile
  ```

  - `cd`: This command changes the current working directory to the one specified as an argument. You can use a relative path or an absolute path to specify the directory. A relative path starts from the current working directory, while an absolute path starts from the root directory (`/`). You can use `..` to refer to the parent directory, and `.` to refer to the current directory. For example:

  ```bash
  pi@raspberrypi:~ $ cd Documents
  pi@raspberrypi:~/Documents $ cd ..
  pi@raspberrypi:~ $ cd /usr/bin
  pi@raspberrypi:/usr/bin $ cd .
  pi@raspberrypi:/usr/bin $
  ```

  - `touch`: This command creates an empty file with the name specified as an argument. If the file already exists, it updates its modification date. You can use this command to create new files or to test if you have write permission in a directory. For example:

  ```bash
  pi@raspberrypi:~ $ touch test.txt
  pi@raspberrypi:~ $ ls -l test.txt
  -rw-r--r-- 1 pi pi 0 Mar 16 06:04 test.txt
  ```

  - `mv`: This command moves or renames a file or directory. You need to specify the source and the destination as arguments. If the destination is a directory, the source will be moved into that directory