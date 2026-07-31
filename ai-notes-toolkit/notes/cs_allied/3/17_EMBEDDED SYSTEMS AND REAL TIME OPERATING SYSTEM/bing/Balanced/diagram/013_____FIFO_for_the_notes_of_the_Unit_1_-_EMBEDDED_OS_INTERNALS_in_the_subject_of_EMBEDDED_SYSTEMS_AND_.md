### FIFO

FIFO stands for First In First Out. It is a data structure that follows the principle of **queueing**. That means, the first element that enters the FIFO is the first one that leaves it. FIFOs are useful for **buffering** and **flow control** in embedded systems, where data may arrive or depart at different rates or times.

Some key points about FIFOs are:

- FIFOs can be implemented in **hardware** or **software**. Hardware FIFOs are faster and more reliable, but also more expensive and complex. Software FIFOs are more flexible and adaptable, but also more prone to errors and delays.
- FIFOs can be **exclusive read/write** or **concurrent read/write**. Exclusive read/write means that only one operation (read or write) can be performed at a time. Concurrent read/write means that both operations can be performed simultaneously, as long as the FIFO is not full or empty.
- FIFOs can have different **sizes** and **depths**. The size of a FIFO is the number of bits or bytes that each element occupies. The depth of a FIFO is the number of elements that it can store. The size and depth of a FIFO depend on the application and the hardware or software constraints.
- FIFOs can have different **modes** of operation. Some common modes are **blocking**, **non-blocking**, **interrupt-driven**, and **polling**. Blocking mode means that the read or write operation waits until the FIFO is ready. Non-blocking mode means that the read or write operation returns immediately, regardless of the FIFO status. Interrupt-driven mode means that the read or write operation triggers an interrupt when the FIFO is ready. Polling mode means that the read or write operation checks the FIFO status periodically.