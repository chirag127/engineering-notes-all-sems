#### Hive shell

- The Hive shell is a command-line interface (CLI) that allows users to interact with Hive and execute HiveQL commands.
- The Hive shell can be launched by typing `hive` in the terminal. It will display a prompt `hive>` where users can enter their queries.
- The Hive shell supports various options and commands to configure and control the Hive session. Some of the common options and commands are:

  - `-e "query"`: Executes the query and prints the output to the standard output.
  - `-f filename`: Executes the queries in the file and prints the output to the standard output.
  - `-i filename`: Executes the commands in the file before entering the interactive shell.
  - `-v`: Enables verbose mode, which prints more information about the execution process.
  - `-h`: Displays the help message and exits.
  - `set key=value;`: Sets a Hive configuration property for the current session.
  - `!command;`: Executes a shell command from the Hive shell.
  - `dfs command;`: Executes a Hadoop file system command from the Hive shell.
  - `quit;`: Exits the Hive shell.

- The Hive shell supports various features to enhance the user experience, such as:

  - Tab completion: Pressing the tab key will complete the current word or suggest possible completions based on the context.
  - History: Pressing the up and down arrow keys will navigate through the previous and next commands entered in the shell.
  - Editing: Pressing the left and right arrow keys will move the cursor within the current command. Pressing the backspace key will delete the character before the cursor. Pressing the delete key will delete the character after the cursor.
  - Multi-line commands: A command can span multiple lines by ending each line with a backslash (`\`) character. The shell will prompt with `>` for the continuation lines.