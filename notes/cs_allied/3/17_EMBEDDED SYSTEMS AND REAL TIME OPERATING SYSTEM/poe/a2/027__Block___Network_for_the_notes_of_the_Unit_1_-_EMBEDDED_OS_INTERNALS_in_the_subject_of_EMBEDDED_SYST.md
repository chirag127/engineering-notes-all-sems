 Here are the notes for the topic **Block & Network** for the Unit 1 - **Embedded OS Internals** in the subject of **Embedded Systems and Real Time Operating System**:

### Block Devices

- Block devices are addressed as arrays of blocks, each block of a fixed size.
- Examples: Hard disks, flash memories, etc.
- The OS views the storage as an array of blocks and interacts with the block device by reading/writing blocks.
- The block size is a characteristic of the device and is typically 512 bytes or a multiple thereof.
- The block device manages the addressing of blocks and performs the actual read/write operations.
- The OS is shielded from the physical characteristics of the device.

### Character Devices

- Character devices transfer data as a stream of characters (bytes).
- Examples: Terminals, serial communication ports, etc.
- The OS interacts with the device by reading/writing characters (bytes) sequentially.
- There is no block structure or block address notion.
- The OS has to deal with the specific characteristics of the device to handle the data properly (e.g. line discipline for terminals).

### Network Devices

- Network devices provide access to communication networks (e.g. Ethernet).
- They move packets of data between the device and the network.
- The OS interacts with the network device by transmitting and receiving network packets.
- It has to implement network protocols to communicate with other hosts on the network.

The notes are written in points and in a formal tone without any emojis or external links as per the given instructions. The content is written inside headers for the given topic. Please let me know if you would like me to modify or expand the notes.