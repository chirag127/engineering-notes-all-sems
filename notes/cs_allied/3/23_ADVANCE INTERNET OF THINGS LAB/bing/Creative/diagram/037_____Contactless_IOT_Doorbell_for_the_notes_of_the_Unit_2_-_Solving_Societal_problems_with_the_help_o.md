### Contactless IOT Doorbell

- A contactless IOT doorbell is a device that uses internet of things (IOT) technology to alert the house owner about the arrival of a visitor without requiring any physical contact.
- A contactless IOT doorbell can also perform additional functions such as scanning the temperature of the visitor, recognizing the face of the visitor, and sending online notifications to the house owner's mobile or desktop device.
- A contactless IOT doorbell can help prevent the spread of infectious diseases such as Covid-19 by reducing the risk of transmission through touching the doorbell button or handle.
- A contactless IOT doorbell can also enhance the security and convenience of the house owner by allowing them to monitor the activity outside the house at any time and sound an alarm at a remote location if needed.

#### Components of a contactless IOT doorbell

- A contactless IOT doorbell typically consists of the following components:
  - A microcontroller such as NodeMCU or Raspberry Pi that acts as the brain of the device and controls the communication between the sensors, the speaker, the camera, and the internet.
  - A non-contact infrared temperature sensor such as MLX90614 that measures the temperature of the visitor from a distance and sends the data to the microcontroller.
  - A camera module that captures the image of the visitor and sends it to the microcontroller for face recognition or online streaming.
  - A speaker that plays a voice message or a sound to greet the visitor or alert the house owner.
  - A wireless module such as Wi-Fi or Bluetooth that connects the device to the internet and enables the data transmission to the online database or the house owner's device.
  - A power supply such as a battery or a solar panel that provides the necessary voltage and current to the device.
  - A casing or a frame that encloses the device and protects it from environmental factors such as dust, rain, or sunlight.

#### Working of a contactless IOT doorbell

- The working of a contactless IOT doorbell can be summarized as follows:
  - The device is installed outside the house near the door and connected to the internet via the wireless module.
  - When a visitor approaches the door, the temperature sensor detects the presence of a human body and measures the temperature of the visitor.
  - The camera module also captures the image of the visitor and sends it to the microcontroller for face recognition or online streaming.
  - The microcontroller processes the data from the sensors and the camera and compares it with the predefined thresholds or the stored faces.
  - If the temperature of the visitor is above the normal range or the face of the visitor is not recognized, the microcontroller sends an alert to the house owner's device via the internet and plays a warning message or a sound through the speaker.
  - If the temperature of the visitor is within the normal range and the face of the visitor is recognized, the microcontroller sends a notification to the house owner's device via the internet and plays a greeting message or a sound through the speaker.
  - The house owner can view the temperature and the image of the visitor on their device and decide whether to open the door or not.
  - The microcontroller also logs all the readings of the device to an online database such as Firebase for future reference or analysis.