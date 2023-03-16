# Inter-Integrated Circuit

- Inter-Integrated Circuit (I2C) is a **serial communication bus** that connects low-speed peripherals to a motherboard, mobile phone, embedded system or other electronic devices    .
- I2C was invented in 1982 by **Philips Semiconductor** (now NXP Semiconductors) and is also known as a **two-wire interface**   .
- I2C requires only **two wires**: a **serial data line** (SDA) and a **serial clock line** (SCL)    .
- I2C can support up to **1008 slave devices** for synchronous serial communication. Unlike SPI, I2C can support **multi-master, multi-slave** bus  .
- I2C uses **7-bit or 10-bit addressing** to identify the devices on the bus  . Each device has a unique address that is either fixed by the manufacturer or configurable by software .
- I2C transfers data in **packets** that consist of a **start condition**, an **address byte**, one or more **data bytes**, an **acknowledge bit**, and a **stop condition**  .
- I2C has a **standard mode** that operates at 100 kbit/s, a **fast mode** that operates at 400 kbit/s, a **fast mode plus** that operates at 1 Mbit/s, and a **high-speed mode** that operates at 3.4 Mbit/s  .
- I2C is widely used in applications where low costs and ease-of-implementation take priority over lightning-quick speed. Some examples of I2C devices are EEPROMs, sensors, LCDs, touchscreens, and audio codecs .