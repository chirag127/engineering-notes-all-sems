### Using libraries for the notes of the Unit 5 - Programming the Arduino in the subject of Internet of Things

- Libraries are collections of code that provide extra functionality for use in sketches, such as working with hardware or manipulating data.
- Libraries can be installed from the Arduino IDE, using the Library Manager or by downloading them from the Internet and adding them manually.
- Libraries can be imported into a sketch by selecting them from Sketch > Import Library or by using the #include directive at the top of the code.
- Libraries can be used to access radio modules on different IoT boards, such as Wi-Fi, Bluetooth, LoRa, GSM, NB-IoT, Sigfox, etc.
- Libraries can also be used to access embedded sensors on various Nano boards, such as gesture, color, humidity, temperature, IMU, barometer, etc.
- Some examples of official Arduino libraries are:

  - Servo - for controlling servo motors.
  - Stepper - for controlling stepper motors.
  - SPI - for communicating with devices using the Serial Peripheral Interface (SPI) Bus.
  - Wire - for sending and receiving data over a net of devices or sensors using the Two Wire Interface (TWI/I2C).
  - SoftwareSerial - for serial communication on any digital pins.
  - ArduinoIoTCloud - for connecting to the Arduino IoT Cloud service.
  - ArduinoBLE - for using the Bluetooth Low Energy on a selection of boards.
  - Ethernet - for connecting to the Internet via Ethernet.
  - GSM - for connecting to a GSM/GPRS network with the GSM shield.
  - MKRWAN - for connecting to LoRaWAN networks with the MKR WAN 1300/1310 boards.
  - WiFi - for connecting to the Internet via Wi-Fi with the WiFi shield.
  - WiFi101 - for connecting to the Internet via Wi-Fi with the MKR 1000 WiFi and WiFi101 shield.
  - WiFiNINA - for connecting to the Internet via Wi-Fi with boards with a Wi-Fi NINA module.
  - ArduinoAPDS9960 - for using the gesture sensor APDS9960 on the Nano 33 BLE Sense board.
  - Arduino_LSM6DS3 - for using the LSM6DS3 6 axis IMU on the Nano 33 IoT and the UNO WiFi Rev. 2 boards.
  - Arduino_LSM9DS1 - for using the LSM9DS1 9 axis IMU on the Nano 33 BLE and the Nano 33 BLE Sense boards.
  - Arduino_LSM6DSOX - for using the LSM6DSOX 6 axis IMU on the Nano RP2040 Connect board.
  - ArduinoLPS22HB - for using the barometer and temperature sensor LPS22 on the Nano 33 BLE Sense board.
  - ArduinoHTS221 - for using the HTS221 relative humidity and temperature sensor on the Nano 33 BLE Sense board.

- Some mnemonics and learning tricks for using libraries are:

  - To remember the order of the parameters for the Servo.write() function, think of the acronym APM: Angle, Pin, Microseconds.
  - To remember the difference between SPI and I2C, think of the number of wires: SPI uses 4 wires (MISO, MOSI, SCK, SS), while I2C uses 2 wires (SDA, SCL).
  - To remember the difference between WiFi and WiFiNINA, think of the letter N: WiFiNINA has an N in its name and uses a NINA module, while WiFi does not.
  - To remember the difference between Arduino_LSM6DS3 and Arduino_LSM9DS1, think of the number of axes: Arduino_LSM6DS3 has 6 axes (3 for accelerometer, 3 for gyroscope), while Arduino_LSM9DS1 has 9 axes (3 for accelerometer, 3 for gyroscope, 3 for magnetometer).
  - To remember the difference between ArduinoAPDS9960 and ArduinoHTS221, think of the first letter: ArduinoAPDS9960 starts with A and senses gesture, color, ambience illumination and proximity, while ArduinoHTS221 starts with H and senses humidity and temperature.