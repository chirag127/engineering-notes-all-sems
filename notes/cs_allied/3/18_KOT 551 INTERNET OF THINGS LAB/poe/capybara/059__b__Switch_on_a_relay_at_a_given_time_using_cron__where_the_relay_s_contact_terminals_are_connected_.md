## Switch on a Relay at a Given Time Using Cron

Cron is a Linux utility that enables scheduling of commands or scripts on a server or computer. It is a very useful tool in automation as it allows you to schedule tasks at specific times without any manual intervention. In this guide, we will learn how to switch on a relay at a given time using cron, where the relay's contact terminals are connected to a load.

### Prerequisites

Before we proceed, there are some prerequisites that need to be met. These include:

- A Linux-based operating system installed on your computer or server.
- A relay module with contact terminals connected to a load.
- Basic knowledge of the terminal and Linux commands.

### Steps

1. Connect the relay module to your computer or server. Make sure to connect the contact terminals to the load that you want to switch on at a given time.

2. Find out the GPIO (General Purpose Input/Output) pins that are available on your computer or server. You can do this by running the following command on your terminal:

   ```
   gpio readall
   ```

   This will display a table with all the available GPIO pins on your computer or server.

3. Choose a GPIO pin that you want to use to control the relay module. For example, if you want to use GPIO pin 17, you can set it up by running the following command:

   ```
   gpio mode 17 out
   ```

4. Write a script that will switch on the relay at a given time. For example, if you want to switch on the relay at 6:00 AM every day, you can create a script called `relay_on.sh` with the following contents:

   ```
   #!/bin/bash
   gpio write 17 1
   ```

   This script will switch on the relay by setting the GPIO pin 17 to high (1).

5. Make the script executable by running the following command:

   ```
   chmod +x relay_on.sh
   ```

6. Edit the crontab file by running the following command:

   ```
   crontab -e
   ```

   This will open the crontab file in your default editor.

7. Add the following line to the crontab file:

   ```
   0 6 * * * /path/to/relay_on.sh
   ```

   This line specifies that the `relay_on.sh` script should be run at 6:00 AM every day. Make sure to replace `/path/to/relay_on.sh` with the actual path to the script on your computer or server.

8. Save and close the crontab file.

That's it! The relay module will now switch on at 6:00 AM every day, as specified in the crontab file. You can modify the script and the crontab file to suit your specific requirements.