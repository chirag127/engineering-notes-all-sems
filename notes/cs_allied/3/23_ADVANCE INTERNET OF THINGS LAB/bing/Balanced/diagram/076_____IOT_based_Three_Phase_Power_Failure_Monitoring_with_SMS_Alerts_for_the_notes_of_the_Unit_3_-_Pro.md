Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of IOT based Three Phase Power Failure Monitoring with SMS Alerts for the notes of the Unit 3 - Problem Analysis and Designing a Solution in the subject of ADVANCE INTERNET OF THINGS LAB.

### IOT based Three Phase Power Failure Monitoring with SMS Alerts

- This is an advanced system that monitors power failure in a three-phase system.
- A three-phase system is a type of electrical power distribution that uses three alternating currents of the same frequency and amplitude, but with a phase difference of 120 degrees.
- When one phase of a three-phase system gets lost, a phase loss occurs. This is referred as a ‘single phasing’, this failure generally caused by a blown fuse, thermal overload, broken wire, worn contact or mechanical failure .
- A phase loss can damage the equipment connected to the three-phase system, such as motors, pumps, compressors, etc. It can also cause overheating, vibration, and reduced efficiency.
- To prevent such damages, it is important to detect and alert the phase loss as soon as possible. This is where the IOT based system comes in handy.
- The IOT based system consists of the following components:
  - A voltage sensor for each phase to measure the voltage level and detect the phase loss.
  - An Arduino Uno microcontroller to process the sensor data and send it to the cloud server via Wi-Fi module.
  - A cloud server to store and display the sensor data on a web page and send SMS alerts to the authorized person using a GSM module.
  - An LCD display to show the voltage level and the status of each phase on the local system.
- The working of the system is as follows:
  - The voltage sensors measure the voltage level of each phase and send it to the Arduino Uno.
  - The Arduino Uno compares the voltage level with a threshold value and determines if there is a phase loss or not.
  - If there is a phase loss, the Arduino Uno sends a message to the cloud server with the details of the phase loss.
  - The cloud server receives the message and displays it on the web page. It also sends an SMS alert to the authorized person using the GSM module.
  - The LCD display shows the voltage level and the status of each phase on the local system.
- The advantages of the IOT based system are:
  - It can monitor the three-phase system remotely and in real-time using the cloud server and the web page.
  - It can alert the authorized person quickly and efficiently using the SMS service.
  - It can prevent the damage and loss of the equipment connected to the three-phase system by detecting the phase loss early.
  - It can reduce the maintenance cost and increase the reliability of the three-phase system.