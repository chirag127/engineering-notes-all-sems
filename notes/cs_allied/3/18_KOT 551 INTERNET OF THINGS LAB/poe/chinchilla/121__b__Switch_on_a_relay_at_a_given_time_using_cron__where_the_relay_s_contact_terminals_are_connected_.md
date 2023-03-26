# Switch on a relay at a given time using cron

In order to switch on a relay at a specific time using cron, the following steps can be taken:

1. Connect the relay's contact terminals to the load that needs to be switched on at the specified time.

2. Set up a cron job on the system that will trigger the relay at the specified time. This can be done by using the following command in the terminal:

   `crontab -e`

   This will open the cron configuration file for the current user.

3. In the cron configuration file, add a new line with the following format:

   ```
   * * * * * /path/to/relay/script.sh
   ```

   Replace `/path/to/relay/script.sh` with the path to a script that will trigger the relay.

4. In the script, use a command to trigger the relay. This will depend on the specific hardware being used, but some common commands include:

   ```
   gpio write <pin> 1
   ```

   This command will set the GPIO pin connected to the relay to high, triggering the relay.

5. Save the script and make it executable using the following command:

   ```
   chmod +x /path/to/relay/script.sh
   ```

6. Test the script by running it manually and ensuring that the relay is triggered.

7. Wait for the specified time and check to see if the relay was triggered automatically by the cron job.

By following these steps, it is possible to switch on a relay at a specific time using cron, allowing for automated control of devices connected to the relay.