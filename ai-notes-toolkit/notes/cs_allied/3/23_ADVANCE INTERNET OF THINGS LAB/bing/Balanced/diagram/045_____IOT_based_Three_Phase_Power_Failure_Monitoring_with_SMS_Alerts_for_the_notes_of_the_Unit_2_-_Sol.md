### IOT based Three Phase Power Failure Monitoring with SMS Alerts

- This is a system that monitors the status of a three-phase power supply and alerts the authorized person via SMS in case of a phase loss or failure.
- A phase loss occurs when one of the three phases of a three-phase system gets disconnected or damaged, resulting in a single phasing condition. This can cause serious damage to the equipment and appliances connected to the power supply.
- The system consists of the following components:
  - A microcontroller that controls the logic and communication of the system.
  - A GSM module that sends and receives SMS messages to and from the authorized person.
  - A LCD display that shows the voltage values of the three phases and the status of the system.
  - A voltage sensor that measures the voltage of each phase and sends it to the microcontroller.
  - A relay that switches on and off the power supply to the load.
- The system works as follows:
  - The microcontroller initializes the GSM module and the LCD display and waits for the configuration SMS from the authorized person. The configuration SMS contains the phone number of the authorized person and the threshold voltage for each phase.
  - The voltage sensor continuously measures the voltage of each phase and sends it to the microcontroller. The microcontroller compares the voltage values with the threshold values and determines if there is a phase loss or failure.
  - If there is no phase loss or failure, the microcontroller displays the voltage values and the status of the system on the LCD display and keeps the relay on, allowing the power supply to the load.
  - If there is a phase loss or failure, the microcontroller displays the voltage values and the status of the system on the LCD display and switches off the relay, cutting off the power supply to the load. The microcontroller also sends an SMS alert to the authorized person, informing them about the phase loss or failure and the location of the system.
  - The authorized person can send an SMS command to the system to switch on or off the relay, or to change the threshold voltage for each phase. The system acknowledges the SMS command and performs the corresponding action.