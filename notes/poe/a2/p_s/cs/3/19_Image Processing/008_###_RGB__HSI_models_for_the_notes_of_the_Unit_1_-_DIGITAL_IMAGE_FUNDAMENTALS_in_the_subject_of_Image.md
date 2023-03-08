 Here is the content in markdown format for the topic ### RGB, HSI models for the notes of the Unit 1 - DIGITAL IMAGE FUNDAMENTALS in the subject of Image Processing:

### RGB model
- RGB stands for Red, Green, Blue.
- In RGB model, a color image is represented by three color components: Red, Green and Blue.
- Each pixel in the image contains three values indicating the intensity of Red, Green and Blue color.
- Mixing different intensities of Red, Green and Blue colors can produce a wide variety of colors.
- Advantage: Matches the way displays work. Directly suitable for display on screens.
- Disadvantage: Not perceptually uniform. Equal changes in R, G, B values do not correspond to equal changes in perceived color.

Example: A blue color can be represented as (0, 0, 255) where 0 indicates no Red and Green but full Blue intensity.

Application: Used in displays, TVs, computers, etc.

### HSI model
- HSI stands for Hue, Saturation, Intensity.
- In HSI model, a color is represented using three components:
- Hue - indicates the color type (such as red, blue, green). Usually represented as an angle from 0-360 degrees.
- Saturation - indicates the amount/intensity of the color. Ranges from 0 to 1. 0 indicates grayscale and 1 indicates full color.
- Intensity - indicates the brightness. Also ranges from 0 to 1. 0 is black and 1 is white.
- Advantage: Perceptually uniform. Equal changes in H, S, I correspond to approximately equal changes in perceived color.
- Disadvantage: Does not match the way displays work. Additional conversion is required to display HSI images.

Application: Used in image processing and computer vision for tasks such as segmentation and feature extraction.