#### Framing in link layer in Computer Networks

Framing is the process of dividing a stream of bits into manageable units or frames. The Link Layer of the OSI model is responsible for data framing. The data link layer takes packets from the network layer and encapsulates them into frames. The primary task of the data link layer is to provide reliable data transfer across the physical link.

##### Process of Framing

The following steps are involved in the framing process:

1. **Frame Delimiting:** The first step in framing is to identify where a frame starts and ends. This is done by adding a special bit pattern called a frame delimiter to the beginning and end of each frame.

2. **Byte Stuffing:** If the data to be transmitted already contains the frame delimiter, bit stuffing is used to ensure that the frame delimiter is not confused with actual data. In this process, additional bits are added to the data to differentiate the delimiter from the actual data.

3. **CRC Calculation:** A Cyclic Redundancy Check (CRC) is used to check for errors in the frame. The sender calculates a CRC value from the data in the frame and appends it to the end of the frame. The receiver then calculates the CRC value from the received frame and compares it with the CRC value received from the sender. If the two values match, the frame is considered error-free.

4. **Framing Control:** The framing control field contains information about the type of frame being transmitted. This information is used by the receiver to determine how to interpret the data in the frame.

##### Advantages of Framing

1. **Efficient Data Transfer:** Framing helps in efficient data transfer by dividing the data into smaller chunks or frames.

2. **Reliable Data Transfer:** The CRC calculation ensures that the data transfer is reliable, and any errors are detected and corrected.

3. **Easy Error Detection:** The framing process makes it easy to detect errors during data transmission.

##### Disadvantages of Framing

1. **Overhead:** The framing process adds additional bits to the data, which increases the overhead.

2. **Complexity:** The framing process is complex and requires additional hardware and software to implement.

##### Mnemonics and Learning Tricks

One common mnemonic for remembering the framing process is "FDBCF," which stands for Frame Delimiting, Byte Stuffing, CRC Calculation, and Framing Control. Another trick is to remember the acronym "BBC FC," which stands for Byte Stuffing, Bit Stuffing, and CRC Calculation, which are the three primary processes involved in framing.