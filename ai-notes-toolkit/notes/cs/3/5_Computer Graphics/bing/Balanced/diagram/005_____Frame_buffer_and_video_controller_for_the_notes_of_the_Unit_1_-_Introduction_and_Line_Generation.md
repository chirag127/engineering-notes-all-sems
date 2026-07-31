### Frame buffer and video controller

- A frame buffer is a portion of random-access memory (RAM) containing a bitmap that drives a video display.
- It is a memory buffer containing data representing all the pixels in a complete video frame.
- A video controller is a device that passes the contents of the frame buffer to the monitor.
- It controls the timing and synchronization of the display signals.
- A video controller may also perform additional functions, such as graphics acceleration, video decoding, or cursor generation.

#### Diagram

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Frame buffer   |---->|  Video          |---->|  Monitor        |
|                 |     |  controller     |     |                 |
+-----------------+     +-----------------+     +-----------------+
```