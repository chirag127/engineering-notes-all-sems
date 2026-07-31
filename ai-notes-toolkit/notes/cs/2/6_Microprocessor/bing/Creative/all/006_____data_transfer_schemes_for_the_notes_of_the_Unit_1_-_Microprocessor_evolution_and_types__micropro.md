# Data Transfer Schemes

Data transfer schemes are the methods through which data can be transferred between the units of a microprocessor system, such as the CPU, memory, and I/O devices. Data transfer schemes are important for the efficient and smooth operation of the system. There are three main types of data transfer schemes:

- Programmed I/O Data Transfer
- Interrupt Driven Data Transfer
- Direct Memory Access (DMA) Data Transfer

## Programmed I/O Data Transfer

- Programmed I/O Data Transfer scheme of microprocessor is a simple parallel data transfer scheme. This method of data transfer is generally used in the simple microprocessor systems. It is obvious that where speed is unimportant.
- In this scheme, data transfer takes place under the control of a program residing in the main memory of the microcomputer system. So microprocessor executes a program to perform all data transfers between the memory and i/o device via register.
- The program consists of a sequence of instructions that check the status of the I/O device, read or write data to or from the device, and loop back until the data transfer is complete.
- The advantage of this scheme is that it is simple and easy to implement. The disadvantage is that it consumes a lot of CPU time and slows down the system performance.

## Interrupt Driven Data Transfer

- Interrupt Driven Data Transfer scheme of microprocessor is a more efficient parallel data transfer scheme. This method of data transfer is generally used in the microprocessor systems that require faster data transfer and multitasking.
- In this scheme, data transfer takes place between the CPU and I/O device with the help of an interrupt signal. An interrupt signal is a special signal that informs the CPU that an I/O device needs its attention.
- When the CPU receives an interrupt signal, it temporarily suspends its current program and saves its context. Then it executes a special program called an interrupt service routine (ISR) that handles the data transfer with the I/O device. After the data transfer is complete, the CPU resumes its original program and restores its context.
- The advantage of this scheme is that it frees the CPU from constantly polling the I/O device and allows it to perform other tasks. The disadvantage is that it requires additional hardware and software to handle the interrupt signals and the ISR.

## Direct Memory Access (DMA) Data Transfer

- Direct Memory Access (DMA) Data Transfer scheme of microprocessor is the most efficient parallel data transfer scheme. This method of data transfer is generally used in the microprocessor systems that require bulk data transfer and high speed.
- In this scheme, data is directly transferred from the memory to the I/O device or vice versa without going through the microprocessor. This scheme is used when there is a requirement to send bulk data. Transferring bulk data using a microprocessor consumes more time. Therefore, the microprocessor performs the initialization of the data transfer and then delegates the task to a special hardware device called a DMA controller.
- The DMA controller takes over the control of the system bus and transfers the data between the memory and the I/O device. The microprocessor is notified when the data transfer is complete by an interrupt signal. The microprocessor then resumes its normal operation.
- The advantage of this scheme is that it reduces the CPU involvement and increases the system throughput. The disadvantage is that it requires a complex hardware device and a dedicated system bus.