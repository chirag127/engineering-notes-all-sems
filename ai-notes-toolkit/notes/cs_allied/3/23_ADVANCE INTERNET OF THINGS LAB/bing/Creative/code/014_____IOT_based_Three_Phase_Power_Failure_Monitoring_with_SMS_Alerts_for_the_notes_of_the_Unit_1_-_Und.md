### IOT based Three Phase Power Failure Monitoring with SMS Alerts

- This is a system that monitors the power supply of a three-phase system and alerts the authorized person via SMS in case of any failure in one or more phases.
- A three-phase system is a type of electrical power distribution that uses three alternating currents of the same frequency and amplitude, but with a phase difference of 120 degrees between them.
- A phase loss or single phasing occurs when one of the phases gets disconnected or damaged due to various reasons, such as a blown fuse, thermal overload, broken wire, worn contact or mechanical failure.
- A phase loss can cause serious problems for the equipment and devices connected to the three-phase system, such as overheating, reduced efficiency, increased current, imbalance, vibration, noise, and damage.
- To prevent these problems, it is important to detect and report the phase loss as soon as possible, and take appropriate actions to restore the power supply or switch to an alternative source.
- The system consists of the following components:
  - A microcontroller unit (MCU) that controls the overall operation of the system and communicates with the other components.
  - A GSM module that sends and receives SMS messages to and from the authorized person's mobile phone.
  - A LCD display that shows the status of the three phases and the SMS messages.
  - Three voltage sensors that measure the voltage of each phase and send the data to the MCU.
  - Three relays that switch on or off the power supply of each phase according to the MCU's commands.
  - A buzzer that sounds an alarm when a phase loss is detected.
- The system works as follows:
  - The MCU initializes the GSM module and the LCD display, and waits for the configuration SMS from the authorized person's mobile phone. The configuration SMS contains the mobile number and the threshold voltage for each phase.
  - The MCU reads the voltage data from the sensors and compares them with the threshold values. If any of the phases has a voltage below the threshold, it indicates a phase loss. The MCU then sends an SMS to the authorized person's mobile phone, informing the phase number and the voltage value. The MCU also activates the buzzer and the corresponding relay to cut off the power supply of the faulty phase.
  - The authorized person can send an SMS to the MCU to check the status of the three phases, or to reset the system after the phase loss is resolved. The MCU replies with an SMS containing the voltage values of the three phases, and resets the buzzer and the relays if instructed.
  - The LCD display shows the voltage values of the three phases and the SMS messages received and sent by the MCU.