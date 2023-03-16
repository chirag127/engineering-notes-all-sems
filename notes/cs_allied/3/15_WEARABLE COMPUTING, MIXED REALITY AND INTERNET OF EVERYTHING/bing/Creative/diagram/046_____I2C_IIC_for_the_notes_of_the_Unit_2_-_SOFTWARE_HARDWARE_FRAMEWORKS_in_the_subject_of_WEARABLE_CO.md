Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of I2C/IIC protocol for the unit 2 of the subject of wearable computing, mixed reality and internet of everything.

### I2C/IIC Protocol

- I2C or IIC stands for **Inter-Integrated Circuit**, a serial communication protocol made by Philips Semiconductor (now NXP Semiconductor) in 1982 .
- It is intended for communication between chips that reside on the same printed circuit board (PCB) or within a short distance .
- It is a **synchronous**, **multi-master/multi-slave**, **packet switched**, **single-ended**, **serial communication bus**.
- It uses only **two wires** to transmit and receive data: a **serial data line (SDA)** and a **serial clock line (SCL)**  .
- The clock signal is always controlled by the **master** device, which initiates and terminates the data transfer .
- The data line is **bidirectional**, meaning that data can flow in both directions on the same wire.
- The data transfer is based on **8-bit packets**, each followed by an **acknowledgment bit** from the receiver .
- The data packets have a **7-bit or 10-bit address** field, which identifies the **slave** device that the master wants to communicate with .
- The data packets also have a **read/write bit**, which indicates whether the master wants to read from or write to the slave device .
- The data transfer can be **interrupted** by another master device, which can take over the bus after the current transfer is completed .
- The data transfer can also be **arbitrated** by the devices, which can detect and resolve conflicts on the bus when multiple masters try to access the same slave device at the same time .
- The data transfer rate can vary from **100 kbit/s** (standard mode) to **5 Mbit/s** (ultra-fast mode), depending on the bus capacitance and the pull-up resistors .
- The I2C protocol is widely used for connecting **low-speed peripherals** such as sensors, EEPROMs, LCDs, ADCs, DACs, etc. to microcontrollers, microprocessors, or other devices  .
- The I2C protocol is also compatible with other protocols such as **SMBus** (System Management Bus) and **PMBus** (Power Management Bus), which are derived from I2C and have additional features.