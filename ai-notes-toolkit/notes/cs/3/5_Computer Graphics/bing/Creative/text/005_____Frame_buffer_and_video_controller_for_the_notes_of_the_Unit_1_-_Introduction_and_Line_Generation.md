### Frame buffer and video controller

- A frame buffer is a portion of random-access memory (RAM) containing a bitmap that drives a video display.
- It is a memory buffer containing data representing all the pixels in a complete video frame.
- A video controller is a device that passes the contents of the frame buffer to the monitor.
- It controls the timing and synchronization of the display signals.
- A video controller may also perform additional functions, such as graphics acceleration, video decoding, or cursor generation.

Some points to note about frame buffer and video controller are:

- The frame buffer is the size of the maximum image that can be displayed, and it may be a separate memory bank on the graphics card, GPU or a reserved part of regular memory.
- The frame buffer can store different types of information, such as color, depth, alpha, or stencil values.
- The frame buffer can be accessed by the CPU or the GPU, depending on the system architecture and the graphics API.
- The video controller can have different modes of operation, such as text mode, graphics mode, or overlay mode.
- The video controller can support different types of monitors, such as CRT, LCD, or OLED.