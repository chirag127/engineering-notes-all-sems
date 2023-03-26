##### 5. a) Flash an LED based on cron output (acts as an alarm)

To flash an LED based on cron output, you can follow the below steps:

1. Connect an LED to your Raspberry Pi board. Make sure to connect the positive leg of the LED to a GPIO pin and the negative leg to a ground pin.
2. Open the terminal and type the following command to create a new cron job: 
```
$ crontab -e
```
3. In the cron file, add the following line of code to run the script every minute:
```
* * * * * /path/to/script.sh
```
4. Create a new script file named `script.sh` using the following command:
```
$ sudo nano /path/to/script.sh
```
5. In the `script.sh` file, write the following code to check if the current minute is even or odd:
```bash
#!/bin/bash
if [ $(( $(date +%s) / 60 % 2 )) -eq 0 ]
then
    gpio -g write 4 1
    sleep 0.5
    gpio -g write 4 0
else
    gpio -g write 4 0
fi
```
6. Save and exit the file by pressing `Ctrl+X`, followed by `Y` and `Enter`.
7. Make the `script.sh` file executable by running the following command:
```
$ chmod +x /path/to/script.sh
```
8. Run the `gpio` command to set the GPIO mode to `out` and to turn off the LED:
```
$ gpio -g mode 4 out
$ gpio -g write 4 0
```
9. Wait for the cron job to run and check if the LED is flashing every minute. If everything is working correctly, the LED should flash for every even minute.

In conclusion, by following the above steps, you can easily flash an LED based on cron output and use it as an alarm. This can be useful for various applications, such as reminding you of an upcoming event or notifying you of a system error.