# Contactless IOT Doorbell

- A contactless IOT doorbell is a device that uses internet of things (IOT) technology to alert the house owner about the arrival of a visitor without requiring physical contact.
- A contactless IOT doorbell can also perform other functions such as scanning the temperature of the visitor, recognizing the face of the visitor, capturing the image of the visitor, and sending notifications to the house owner's smartphone or computer.
- A contactless IOT doorbell can enhance the security and convenience of the house owner, as well as reduce the risk of spreading infectious diseases such as Covid-19.

## Problem Analysis

- The problem that a contactless IOT doorbell aims to solve is the lack of a safe and smart way to communicate with visitors at the door, especially during the pandemic situation.
- The existing solutions, such as traditional doorbells, intercoms, or peepholes, are either outdated, unreliable, or require physical contact, which can expose the house owner and the visitor to potential health hazards.
- The stakeholders of the problem are the house owners, the visitors, and the IOT device manufacturers.
- The requirements of the problem are:
  - The contactless IOT doorbell should be able to detect the presence of a visitor at the door and alert the house owner with a sound or a message.
  - The contactless IOT doorbell should be able to measure the temperature of the visitor and display it on a screen or send it to the house owner's device.
  - The contactless IOT doorbell should be able to recognize the face of the visitor and compare it with a database of known or authorized people.
  - The contactless IOT doorbell should be able to capture the image of the visitor and store it in a cloud server or send it to the house owner's device.
  - The contactless IOT doorbell should be able to communicate with the house owner and the visitor through a voice or a text interface.
  - The contactless IOT doorbell should be able to connect to the internet and send notifications to the house owner's device or a web portal.
  - The contactless IOT doorbell should be able to operate on battery or solar power and have a low power consumption.
  - The contactless IOT doorbell should be easy to install, use, and maintain.

## Designing a Solution

- The design of a contactless IOT doorbell can be divided into four main components: hardware, software, communication, and user interface.
- The hardware component consists of the following elements:
  - A microcontroller, such as NodeMCU, Arduino, or Raspberry Pi, that acts as the brain of the device and controls the other components.
  - A non-contact infrared temperature sensor, such as MLX90614, that measures the temperature of the visitor and sends it to the microcontroller.
  - A camera module, such as Pi Camera or OV7670, that captures the image of the visitor and sends it to the microcontroller.
  - A face recognition module, such as OpenCV or TensorFlow, that analyzes the image of the visitor and compares it with a database of known or authorized people.
  - A speaker module, such as PAM8403 or LM386, that produces a sound or a voice message to alert the house owner or communicate with the visitor.
  - A display module, such as LCD or OLED, that shows the temperature or other information to the visitor or the house owner.
  - A power module, such as battery or solar panel, that provides the energy to the device and regulates the voltage and current.
- The software component consists of the following elements:
  - A programming language, such as C, Python, or Java, that defines the logic and functionality of the device and interacts with the hardware components.
  - A cloud platform, such as Firebase, AWS, or Azure, that stores the data and images of the visitors and provides the online access and notifications to the house owner.
  - A mobile app or a web portal, such as Blynk, MIT App Inventor, or HTML, that allows the house owner to view the data and images of the visitors and control the device remotely.
- The communication component consists of the following elements:
  - A wireless protocol, such as Wi-Fi, Bluetooth, or Zigbee, that enables the device to connect to the internet and communicate with the house owner's device or the cloud platform.
  - A wired protocol, such as I2C, SPI, or UART, that enables the device to communicate with the hardware components.
- The user