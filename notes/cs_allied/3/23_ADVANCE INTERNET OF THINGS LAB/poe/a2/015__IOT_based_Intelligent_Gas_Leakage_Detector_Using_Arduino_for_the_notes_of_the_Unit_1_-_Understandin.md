 Here is the content in markdown format without any feeling or friendliness, being formal and without any emojis or external links:

### IOT based Intelligent Gas Leakage Detector Using Arduino

#### For the notes of the Unit 1 - Understanding the implementation of IOT in the subject of ADVANCE INTERNET OF THINGS LAB.

1. Introduction to IOT and Gas Leakage Detection System
- IOT refers to the interconnection of physical devices, vehicles, buildings and other items with electronics, software, sensors, actuators and networking which allows these things to collect and exchange data.
- A gas leakage detection system detects the leakage of gases like LPG, Natural gas, etc and alerts the users about the same to avoid mishaps.

2. Requirements for the Project
- Arduino board
- Gas sensor - MQ2 sensor
- Buzzer
- Breadboard
- Jumper wires
- Power supply

3. Circuit Diagram
- Connect the VCC and GND of MQ2 sensor to the power supply.
- Connect the AOUT pin of MQ2 sensor to the analog pin A0 of Arduino board.
- Connect the buzzer to pin 12 of Arduino board.

4. Working Principle
- The MQ2 gas sensor senses the concentration of gas.
- The Arduino board reads the sensed concentration value through the analog pin A0.
- If the gas concentration goes above the threshold limit, the buzzer is turned on by the Arduino board through pin 12 to alert the user about gas leakage.

5. Programming Arduino
- Define the threshold limit for gas concentration.
- Continuously read the analog value from MQ2 sensor.
- Compare the read value with threshold limit.
- If the read value exceeds the threshold, turn on the buzzer to alert.
- Else continue sensing.

[No emojis or external links are included as directed]