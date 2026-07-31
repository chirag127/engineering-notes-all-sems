### Frame buffer and video controller

- A frame buffer is a portion of random-access memory (RAM) containing a bitmap that drives a video display.
- It is a memory buffer containing data representing all the pixels in a complete video frame.
- A video controller is a device that passes the contents of the frame buffer to the monitor.
- It controls the timing and synchronization of the display signals.
- The frame buffer and video controller are essential components of computer graphics systems, as they enable the display of graphical output on the screen.
- The size and resolution of the frame buffer determine the quality and complexity of the images that can be displayed.
- The frame buffer can be implemented as a separate memory bank on the graphics card, or as a reserved part of regular memory.
- The video controller can be integrated with the graphics card, or as a separate chip on the motherboard.
- The frame buffer and video controller can be classified into different types, such as:
  - Monochrome frame buffer: It has one bit per pixel, and can display only black and white images.
  - Color frame buffer: It has multiple bits per pixel, and can display images with different colors.
  - Single-buffered frame buffer: It has one memory area for storing the current frame.
  - Double-buffered frame buffer: It has two memory areas for storing the current and the next frame, and can switch between them to avoid flickering.
  - Overlay frame buffer: It has multiple memory areas for storing different layers of images, and can combine them to create complex scenes.