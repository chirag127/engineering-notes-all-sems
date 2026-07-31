# How to switch on a relay at a given time using cron

- A relay is an electromechanical device that can be used to control a load (such as a light, a fan, a motor, etc.) with a low-power signal (such as from a microcontroller, a sensor, a timer, etc.).
- A relay has two main parts: a coil and a set of contacts. The coil is an electromagnet that can be energized by applying a voltage across its terminals. The contacts are metal pieces that can be either open (no electrical connection) or closed (electrical connection) depending on the state of the coil.
- A relay can have different types of contacts, such as normally open (NO), normally closed (NC), or changeover (CO). A NO contact is open when the coil is de-energized and closed when the coil is energized. A NC contact is closed when the coil is de-energized and open when the coil is energized. A CO contact can switch between NO and NC states depending on the coil state.
- To switch on a relay at a given time using cron, the following steps are required:

  1. Connect the relay's coil terminals to a suitable power source (such as a battery, a power supply, or a GPIO pin of a microcontroller) and a control signal (such as from a sensor, a timer, or a software program).
  2. Connect the relay's contact terminals to the load and another power source (such as the mains, a battery, or a power supply) that can provide the required voltage and current for the load.
  3. Write a cron job that can send the control signal to the relay's coil at the desired time. A cron job is a scheduled task that can run commands or scripts at specified intervals or times. For example, to switch on the relay every day at 8:00 AM, the cron job can be written as:

  ```
  0 8 * * * python relay_on.py
  ```

  where `relay_on.py` is a Python script that can send a high signal to the GPIO pin connected to the relay's coil.

  4. Save the cron job in the crontab file using the `crontab -e` command and exit the editor. The crontab file is a text file that stores the cron jobs for a user or a system. The cron daemon will read the crontab file and execute the cron jobs accordingly.
  5. Test the cron job by checking the relay and the load state at the specified time. If the relay is switched on, the load should also be switched on. If the relay is switched off, the load should also be switched off.