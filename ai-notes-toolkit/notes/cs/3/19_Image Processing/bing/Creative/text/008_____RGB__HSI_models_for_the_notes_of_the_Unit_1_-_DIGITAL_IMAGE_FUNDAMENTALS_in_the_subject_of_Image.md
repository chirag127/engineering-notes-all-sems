### RGB, HSI models for the notes of the Unit 1 - DIGITAL IMAGE FUNDAMENTALS in the subject of Image Processing

- RGB and HSI are two color models used in digital image processing to represent colors in images.
- RGB stands for red, green, and blue, which are the primary colors of light. The RGB color model is additive, meaning that different combinations of red, green, and blue light can produce a wide range of colors .
- HSI stands for hue, saturation, and intensity, which are the attributes of color perception. The HSI color model is based on how the human eye senses colors. Hue is the dominant wavelength of light, saturation is the purity of color, and intensity is the brightness of color .
- The RGB color model is more suitable for hardware devices, such as monitors, scanners, and cameras, that use light to display or capture colors. The HSI color model is more suitable for software applications, such as image editing, enhancement, and segmentation, that use color information to process images .
- The RGB color model is based on a Cartesian coordinate system, where each color is represented by a point in a three-dimensional space. The HSI color model is based on a cylindrical coordinate system, where each color is represented by an angle, a radius, and a height in a cylinder .
- The RGB color model can be converted to the HSI color model using the following formulas :

  - Let R, G, and B be the red, green, and blue components of a pixel in the RGB color model, normalized to the range [0, 1].
  - Let H, S, and I be the hue, saturation, and intensity components of the same pixel in the HSI color model, normalized to the range [0, 1].
  - Then,

    - I = (R + G + B) / 3
    - S = 1 - (min(R, G, B) / I), if I > 0, else S = 0
    - H = cos^-1 ((0.5 * ((R - G) + (R - B))) / sqrt(((R - G)^2) + ((R - B) * (G - B)))), if B <= G, else H = 2 * pi - cos^-1 ((0.5 * ((R - G) + (R - B))) / sqrt(((R - G)^2) + ((R - B) * (G - B))))

- The HSI color model can be converted to the RGB color model using the following formulas :

  - Let H, S, and I be the hue, saturation, and intensity components of a pixel in the HSI color model, normalized to the range [0, 1].
  - Let R, G, and B be the red, green, and blue components of the same pixel in the RGB color model, normalized to the range [0, 1].
  - Then,

    - If H is in the range [0, 2 * pi / 3], then

      - B = I * (1 - S)
      - R = I * (1 + (S * cos(H)) / cos(pi / 3 - H))
      - G = 3 * I - (R + B)

    - If H is in the range [2 * pi / 3, 4 * pi / 3], then

      - H = H - 2 * pi / 3
      - R = I * (1 - S)
      - G = I * (1 + (S * cos(H)) / cos(pi / 3 - H))
      - B = 3 * I - (R + G)

    - If H is in the range [4 * pi / 3, 2 * pi], then

      - H = H - 4 * pi / 3
      - G = I * (1 - S)
      - B = I * (1 + (S * cos(H)) / cos(pi / 3 - H))
      - R = 3 * I - (G + B)