# Frame buffer and video controller

- A frame buffer is a portion of random-access memory (RAM) containing a bitmap that drives a video display .
- It is a memory buffer containing data representing all the pixels in a complete video frame .
- The frame buffer is the size of the maximum image that can be displayed, and it may be a separate memory bank on the graphics card (display adapter), GPU or a reserved part of regular memory.
- A video controller or display controller is a device that passes the contents of the frame buffer to the monitor .
- It controls the operation of the display device and provides the interface between the frame buffer and the monitor.
- It may also perform additional functions such as generating the timing signals, providing a cursor, or performing basic graphics operations.