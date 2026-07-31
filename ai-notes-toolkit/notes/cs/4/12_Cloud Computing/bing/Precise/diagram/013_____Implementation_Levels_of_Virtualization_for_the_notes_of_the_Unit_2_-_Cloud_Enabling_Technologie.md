### Implementation Levels of Virtualization

Virtualization is a computer architecture technology by which multiple virtual machines (VMs) are multiplexed in the same hardware machine. The idea of VMs can be dated back to the 1960s . There are five levels of implementing virtualization:

1. **Instruction Set Architecture Level (ISA)**: In ISA, virtualization works through an ISA emulation. This is helpful to run software on hardware that it was not designed for  .
2. **Hardware Abstraction Level (HAL)**: As the name suggests, this level helps perform virtualization at the hardware level  .
3. **Operating System Level**: At the operating system level, the virtualization model creates an abstract layer between the applications and the OS .
4. **Library Level** .
5. **Application Level** .

After virtualization, different user applications managed by their own operating systems (guest OS) can run on the same hardware, independent of the host OS  .