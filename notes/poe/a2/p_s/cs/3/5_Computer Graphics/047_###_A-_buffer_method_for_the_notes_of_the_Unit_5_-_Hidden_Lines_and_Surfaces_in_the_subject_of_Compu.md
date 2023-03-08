 Here is the content in markdown format for the given topic:

### A-buffer method for Hidden Lines and Surfaces

The A-buffer method is a technique used to remove hidden lines and surfaces in 3D computer graphics. The key points about this method are:

1.  It stores two attributes for each pixel: depth (z-value) and flag (a-value). The a-value is set to 1 if the pixel is visible and 0 if hidden.
2.  Pixels are plotted in the frame buffer if the surface is visible i.e. a-value is 1. The a-value is updated based on the visibility of the current pixel with respect to the previously plotted pixels.
3.  The z-buffer stores the depth values to handle occlusion. The a-value is updated based on a comparison of current z-value with the stored z-value. If current z is smaller, pixel is visible else hidden.
4.  This method ensures only visible surfaces are drawn resulting in a proper 3D rendering of the scene. However, it requires additional memory to store a-values and more time for visibility determination leading to decreased performance.

Advantages: Proper 3D rendering of scenes with hidden line removal.
Disadvantages: Additional memory required and decreased performance.
Applications: 3D computer graphics, video games, etc.

[Detailed diagrams and codes can be added here to aid understanding]

The content is written in a formal tone with points presented for easy readability and to help learn and revise the topic for exams. Please let me know if you would like me to elaborate on any part or modify the content.