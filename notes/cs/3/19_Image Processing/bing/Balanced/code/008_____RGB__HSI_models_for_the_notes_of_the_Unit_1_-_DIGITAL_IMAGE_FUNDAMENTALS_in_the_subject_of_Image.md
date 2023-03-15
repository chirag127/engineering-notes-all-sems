### RGB, HSI models for the notes of the Unit 1 - DIGITAL IMAGE FUNDAMENTALS in the subject of Image Processing

- RGB and HSI are two color models used in digital image processing to represent colors in images.
- RGB stands for red, green, blue. It is an additive color model, meaning that red, green, and blue light are added together in varying proportions to produce an extensive range of colors.
- HSI stands for hue, saturation, intensity. It is a color model that represents colors similarly how the human eye senses colors. Hue is the dominant wavelength of the color, saturation is the purity of the color, and intensity is the brightness of the color.
- The RGB color model is based on a Cartesian coordinate system, where each color is represented by a point in a 3D space. The origin (0,0,0) corresponds to black, and the point (255,255,255) corresponds to white. The three axes correspond to the red, green, and blue components of the color.
- The HSI color model is based on a cylindrical coordinate system, where each color is represented by an angle (hue), a distance from the origin (saturation), and a height (intensity). The hue ranges from 0 to 360 degrees, the saturation ranges from 0 to 1, and the intensity ranges from 0 to 255.
- The RGB color model is more suitable for hardware devices, such as monitors, scanners, and cameras, that use red, green, and blue light sources or sensors. The HSI color model is more suitable for image processing applications, such as color enhancement, segmentation, and recognition, that require human perception of colors .
- To convert an RGB pixel to an HSI pixel, the following formulas can be used:

  - Hue: H = arccos((0.5 * ((R - G) + (R - B))) / sqrt(((R - G)^2) + ((R - B) * (G - B))))
  - Saturation: S = 1 - (3 / (R + G + B)) * min(R, G, B)
  - Intensity: I = (1 / 3) * (R + G + B)

- To convert an HSI pixel to an RGB pixel, the following formulas can be used:

  - If 0 <= H < 120 degrees, then R = I * (1 + (S * cos(H)) / cos(60 - H)), G = I * (1 - S), B = I * (1 - (S * cos(H + 60)) / cos(180 - H))
  - If 120 <= H < 240 degrees, then R = I * (1 - S), G = I * (1 + (S * cos(H - 120)) / cos(180 - H)), B = I * (1 - (S * cos(H - 60)) / cos(300 - H))
  - If 240 <= H < 360 degrees, then R = I * (1 - (S * cos(H - 240)) / cos(300 - H)), G = I * (1 - (S * cos(H - 180)) / cos(420 - H)), B = I * (1 + (S * cos(H - 300)) / cos(60 - H))