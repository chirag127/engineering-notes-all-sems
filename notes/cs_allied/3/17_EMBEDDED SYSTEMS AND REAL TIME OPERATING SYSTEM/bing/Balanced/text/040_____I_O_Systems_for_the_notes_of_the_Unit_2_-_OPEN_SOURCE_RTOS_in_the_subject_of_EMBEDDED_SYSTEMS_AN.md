### I/O Systems

- I/O systems are the components that enable an embedded system to interact with the external world, such as sensors, actuators, displays, keyboards, etc.
- I/O systems can be classified into two types: parallel and serial.
- Parallel I/O systems use multiple wires to transfer data simultaneously, while serial I/O systems use one or two wires to transfer data sequentially.
- Parallel I/O systems are faster but require more hardware resources, while serial I/O systems are slower but require less hardware resources.
- Some common serial I/O protocols are UART, SPI, I2C, USB, CAN, etc.
- I/O systems can also be classified into two modes: polling and interrupt.
- Polling mode is when the processor continuously checks the status of the I/O device to see if it is ready to send or receive data, while interrupt mode is when the processor is notified by the I/O device when it is ready to send or receive data.
- Polling mode is simpler but consumes more processor time, while interrupt mode is more complex but consumes less processor time.
- I/O systems are important for embedded systems and real time operating systems (RTOS) because they determine the responsiveness and performance of the system.
- RTOS is a type of operating system that guarantees to complete a task within a specified time limit, which is essential for applications that require high reliability and predictability.
- RTOS provides features such as task scheduling, synchronization, communication, memory management, etc. to manage the resources and activities of the embedded system.
- Some examples of RTOS are FreeRTOS, VxWorks, QNX, etc.