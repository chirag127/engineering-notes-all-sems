### Drivers for software tools in human computer interface

- A driver is a specialized software that provides a software interface to hardware devices, enabling operating systems and other computer programs to access hardware functions without needing to know precise details about the hardware being used .
- A driver communicates with the device through the computer bus or communications subsystem to which the hardware connects.
- A human interface device (HID) is a device class definition to replace PS/2-style connectors with a generic USB driver to support HID devices such as keyboards, mice, game controllers, and so on.
- HID devices can use the HidD_Xxx and HidP_Xxx routines to operate devices in the HIDClass device setup class.
- HID minidrivers are drivers that support a subset of HID device types and use the HidRegisterMinidriver routine to register with the HID class driver.
- Windows 8.1 introduced the new Windows.Devices.HumanInterfaceDevice API which lets you write Windows apps that access HID devices.
- To update the driver for your device’s human interface devices, you can use the Device Manager in Windows and select the appropriate device category and device name.