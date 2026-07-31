# Switch on a relay at a given time using cron

## Introduction
A relay is an electrically operated switch that can be controlled by an electronic circuit. It is commonly used in industrial and home automation systems to switch high power loads. In this tutorial, we will learn how to switch on a relay at a given time using cron, where the relay's contact terminals are connected to a load.

## Requirements
- A relay module with contact terminals
- A load to be switched on/off by the relay
- A Raspberry Pi or any other similar single-board computer
- A breadboard and jumper wires
- A 5V power supply for the relay module
- A text editor to edit the crontab file

## Steps
1. Connect the relay module to the Raspberry Pi using jumper wires. Connect the VCC pin of the relay module to the 5V pin of the Raspberry Pi, and the GND pin of the relay module to any GND pin of the Raspberry Pi.
2. Connect the contact terminals of the relay module to the load that needs to be switched on/off.
3. Open a terminal on the Raspberry Pi and type the following command to edit the crontab file:
   ```
   crontab -e
   ```
4. This will open the crontab file in the default editor. Add a new line to the file with the following format:
   ```
   * * * * * /path/to/relay_script.sh
   ```
   Replace `/path/to/relay_script.sh` with the actual path to the script that will switch on the relay.
5. Save the changes to the crontab file and exit the editor.
6. Create a new shell script with the following content:
   ```
   #!/bin/bash
   gpio mode <relay_pin> out
   gpio write <relay_pin> 1
   ```
   Replace `<relay_pin>` with the actual GPIO pin number that is connected to the relay module's signal pin.
7. Save the script with a suitable name and make it executable using the following command:
   ```
   chmod +x /path/to/relay_script.sh
   ```
8. Test the script by running it manually using the following command:
   ```
   /path/to/relay_script.sh
   ```
   This should switch on the relay and the load should be powered on.
9. Wait for the scheduled time for the relay to be switched on according to the crontab file. The relay should be switched on and the load should be powered on.

## Conclusion
In this tutorial, we have learned how to switch on a relay at a given time using cron, where the relay's contact terminals are connected to a load. This can be useful in various home automation and industrial control applications.