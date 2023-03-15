# RGB, HSI models for the notes of the Unit 1 - DIGITAL IMAGE FUNDAMENTALS in the subject of Image Processing

- RGB and HSI are two color models used in digital image processing to represent colors in images.
- RGB stands for red, green, and blue, which are the primary colors of light. The RGB color model is additive, meaning that different colors are obtained by adding different proportions of red, green, and blue light.
- HSI stands for hue, saturation, and intensity, which are the three components of color perception by the human eye. The HSI color model is more intuitive and natural than the RGB model, as it separates the color information (hue and saturation) from the brightness information (intensity).
- The RGB color model is commonly used in digital devices, such as cameras, scanners, monitors, and printers, as it is easy to implement and manipulate. However, the RGB model has some drawbacks, such as:
  - It is device-dependent, meaning that different devices may produce different colors for the same RGB values.
  - It is not perceptually uniform, meaning that equal changes in RGB values do not correspond to equal changes in color perception.
  - It is not suitable for some image processing applications, such as color segmentation, enhancement, and compression, as it mixes the color and brightness information in each channel.
- The HSI color model is more suitable for some image processing applications, as it mimics the human color perception and separates the color and brightness information. However, the HSI model has some drawbacks, such as:
  - It is more complex and computationally expensive to implement and manipulate than the RGB model.
  - It is not standardized, meaning that different definitions and formulas may exist for the HSI components.
  - It is not compatible with most digital devices, which use the RGB model for input and output.
- The conversion between the RGB and HSI models can be done mathematically, using the following formulas :
  - To convert from RGB to HSI, given the RGB values R, G, and B in the range [0, 1], the HSI values H, S, and I are computed as follows:

    - I = (R + G + B) / 3
    - S = 1 - min(R, G, B) / I, if I > 0, else S = 0
    - H = arccos((R - 0.5 * G - 0.5 * B) / sqrt((R - G)^2 + (R - B) * (G - B))), if B <= G, else H = 2 * pi - arccos((R - 0.5 * G - 0.5 * B) / sqrt((R - G)^2 + (R - B) * (G - B))), if B > G

  - To convert from HSI to RGB, given the HSI values H, S, and I in the range [0, 1], the RGB values R, G, and B are computed as follows:

    - If H is in [0, 2 * pi / 3], then R = I * (1 + S * cos(H) / cos(pi / 3 - H)), G = I * (1 - S), and B = 3 * I - (R + G)
    - If H is in [2 * pi / 3, 4 * pi / 3], then R = I * (1 - S), G = I * (1 + S * cos(H - 2 * pi / 3) / cos(pi - H)), and B = 3 * I - (R + G)
    - If H is in [4 * pi / 3, 2 * pi], then R = 3 * I - (G + B), G = I * (1 - S), and B = I * (1 + S * cos(H - 4 * pi / 3) / cos(5 * pi / 3 - H))

- The following diagram illustrates the RGB and HSI color models :

![RGB and HSI color models](https://i.imgur.com/6y8gWnT.png)

- The following table summarizes the main differences between the RGB and HSI color models    :

| RGB | HSI |
| --- | ---