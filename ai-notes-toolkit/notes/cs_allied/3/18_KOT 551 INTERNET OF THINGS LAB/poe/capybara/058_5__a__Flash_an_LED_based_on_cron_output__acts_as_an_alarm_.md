##### 5. a) Flash an LED based on cron output (acts as an alarm)

To flash an LED based on cron output, we can use a simple bash script that runs at a scheduled time using cron. Here are the steps to follow:

1. Create a bash script:
   - Open a terminal window and type: `nano led_flash.sh`
   - Enter the following code in the file:
  
     ```
     #!/bin/bash
     gpio -g mode 17 out
     gpio -g write 17 1
     sleep 1
     gpio -g write 17 0
     ```

   - Save and exit the file by pressing `Ctrl + X`, then `Y`, and then `Enter`.

2. Make the script executable:
   - Type the following command in the terminal: `chmod +x led_flash.sh`

3. Test the script:
   - Run the script by typing: `./led_flash.sh`
   - If the LED connected to GPIO 17 flashes for 1 second, the script is working correctly.

4. Set up a cron job:
   - Type the following command in the terminal: `crontab -e`
   - Add the following line to the end of the file:
  
     ```
     * * * * * /path/to/led_flash.sh
     ```
  
     Replace `/path/to` with the actual path to the `led_flash.sh` file.
   - Save and exit the file by pressing `Ctrl + X`, then `Y`, and then `Enter`.

5. Test the cron job:
   - Wait for the cron job to run at the scheduled time (every minute in this case).
   - Check if the LED connected to GPIO 17 flashes for 1 second.
   
By following these steps, we can create a simple alarm system using a Raspberry Pi and a LED. This can be useful for various applications such as reminding us of an important task or event.