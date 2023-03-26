#### Switch on a Relay at a Given Time Using Cron

Relays are electrically operated switches that allow a low voltage circuit to control a high voltage circuit. They are widely used in industrial automation, home automation, and other applications where electrical isolation is required. In this guide, we will learn how to switch on a relay at a given time using cron, where the relay's contact terminals are connected to a load.

Here are the steps to follow:

1. Identify the relay and the load: The first step is to identify the relay and the load that you want to control. The relay should have two contact terminals, one for the positive and one for the negative wire. The load can be any electrical device that you want to control, such as a light bulb or a motor.

2. Connect the relay to the load: Connect the positive wire of the load to one of the contact terminals of the relay, and the negative wire of the load to the other contact terminal of the relay. Make sure that the connections are tight and secure.

3. Connect the relay to a power source: Connect the positive wire of the power source to the positive contact terminal of the relay, and the negative wire of the power source to the negative contact terminal of the relay. Again, make sure that the connections are tight and secure.

4. Install and configure cron: Cron is a time-based job scheduler in Unix-like operating systems. It allows you to schedule commands or scripts to run automatically at a specific time or interval. To install cron, use the following command:

```
sudo apt-get install cron
```

Once cron is installed, you can configure it by editing the crontab file:

```
crontab -e
```

This will open the crontab file in the default text editor. Add the following line to the file to schedule the relay to switch on at a specific time:

```
* * * * * /path/to/relay/switch/on/script
```

Replace "/path/to/relay/switch/on/script" with the actual path to your script that switches on the relay. The five asterisks represent the time and date when the script will run. In this example, the script will run every minute.

5. Write the script to switch on the relay: Finally, write a script that switches on the relay at the specified time. Here is an example script:

```
#!/bin/bash
echo "Switching on relay"
echo "1" > /sys/class/gpio/gpio18/value
```

Replace "gpio18" with the actual GPIO pin number that is connected to the relay. Save the script and make it executable using the following command:

```
chmod +x /path/to/relay/switch/on/script
```

That's it! The relay will now switch on at the specified time, and the load will be powered on.