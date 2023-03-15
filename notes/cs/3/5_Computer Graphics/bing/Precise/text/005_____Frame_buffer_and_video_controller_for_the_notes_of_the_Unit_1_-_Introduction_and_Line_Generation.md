### Frame buffer and video controller

- A **frame buffer** is a portion of random-access memory (RAM) containing a bitmap that drives a video display. It is a memory buffer containing data representing all the pixels in a complete video frame.
- The frame buffer is the size of the maximum image that can be displayed, and it may be a separate memory bank on the graphics card (display adapter), GPU or a reserved part of regular memory.
- A **display controller** or **video controller** is a simple interface that passes the contents of the frame buffer to the monitor .
- Inside the frame buffer, the image is stored as a pattern of binary digital numbers, which represent a rectangular array of picture elements, or pixels. The pixel is the smallest addressable screen element.
- In the simplest case where we wish to store only black and white images, we can represent black pixels by 0's in the frame buffer and white pixels by 1's. The display controller simply reads each successive byte of data from the frame buffer and converts each 0 and 1 to the corresponding video signal. This signal is then fed to the monitor.
- If we wish to change the displayed picture, all we need to do is to change or modify the frame buffer contents to represent the new pattern of pixels.
