 Here is the content in Markdown format:

### Shift codes for the notes of the Unit 5 - IMAGE COMPRESSION AND RECOGNITION in the subject of Image Processing

- Shift codes are a type of lossless compression technique used for image compression.
- In this technique, the pixel values are shifted by a certain amount (either left shift or right shift) to get a lower range of pixel values. This reduced range of pixel values can be represented using fewer bits, thereby achieving compression.
- For example, if the original image has 8-bit pixel values ranging from 0 to 255, right shifting the pixels by 2 bits will give a range of 0 to 63 which can be represented using 6 bits instead of 8 bits. This reduces the number of bits required to represent the image and hence achieves compression.
- The amount of shift (number of bits to shift) can be varied to achieve different compression ratios. Higher shift will give higher compression but can result in loss of image quality.
- Shift codes are a simple and fast technique but the compression ratio achieved is not very high. It is suitable for images with a small range of pixel values.
- Advantages: Lossless, Simple, Fast. Disadvantages: Achieves low to moderate compression ratio. Applications: Used as a preprocessing step before applying other lossless compression techniques.

#### Function Oriented Design in Software Design

- In function oriented design, the software system is designed in terms of function modules that transform inputs to outputs.
- The system is viewed as a collection of functions/modules and the focus is on decomposing the system into interconnecting functions.
- Each function performs a well-defined task and interacts with other functions through arguments and return values.
- This style of design leads to loosely-coupled and highly cohesive components/functions which makes the system more modular, flexible, reusable and maintainable.
- However, function oriented design may not be suitable for complex systems and may lead to an overabundance of small functions that are difficult to manage. It also does not explicitly represent the data and control flows in the system.
- Examples: Mathematical functions, Device drivers. Advantages: Modular, Flexible, Reusable. Disadvantages: May not scale well for large systems, Control and data flows are implicit.