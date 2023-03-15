# RGB, HSI models for the notes of the Unit 1 - DIGITAL IMAGE FUNDAMENTALS in the subject of Image Processing

- RGB and HSI are two color models used in digital image processing to represent colors in images.
- RGB stands for red, green, and blue, which are the primary colors of light. The RGB color model is additive, meaning that different combinations of red, green, and blue light can produce a wide range of colors. The RGB color model is based on a Cartesian coordinate system, where each color is represented by a point in a three-dimensional space. The origin (0,0,0) corresponds to black, and the point (255,255,255) corresponds to white. The RGB color model is commonly used in computer graphics, display devices, and digital cameras .
- HSI stands for hue, saturation, and intensity, which are the three components of color perception by the human eye. The HSI color model is based on a cylindrical coordinate system, where each color is represented by an angle (hue), a distance from the center (saturation), and a height (intensity). The hue component specifies the dominant wavelength of the color, ranging from 0 to 360 degrees. The saturation component specifies the purity of the color, ranging from 0 (gray) to 1 (full color). The intensity component specifies the brightness of the color, ranging from 0 (black) to 1 (white). The HSI color model is useful for image processing applications that require color manipulation, such as segmentation, enhancement, and compression .
- The RGB and HSI color models are related by the following mathematical formulas :

  - To convert from RGB to HSI, let R, G, and B be the red, green, and blue components of a pixel, normalized to the range [0,1]. Then, the hue H, the saturation S, and the intensity I are given by:

    - H = arctan((sqrt(3) * (G - B)) / (2 * R - G - B)), if R >= G >= B or B >= G >= R
    - H = arctan((sqrt(3) * (G - B)) / (2 * R - G - B)) + 120, if G >= R >= B or B >= R >= G
    - H = arctan((sqrt(3) * (G - B)) / (2 * R - G - B)) + 240, if G >= B >= R or R >= B >= G
    - S = 1 - (3 / (R + G + B)) * min(R, G, B)
    - I = (R + G + B) / 3

  - To convert from HSI to RGB, let H, S, and I be the hue, saturation, and intensity components of a pixel, normalized to the range [0,1]. Then, the red R, the green G, and the blue B are given by:

    - R = I * (1 + (S * cos(H)) / (cos(60 - H)))
    - G = I * (1 + (S * (1 - cos(H) / cos(60 - H))))
    - B = I * (1 - S), if 0 <= H < 120
    - R = I * (1 - S)
    - G = I * (1 + (S * cos(H - 120)) / (cos(180 - H)))
    - B = I * (1 + (S * (1 - cos(H - 120)) / (cos(180 - H)))), if 120 <= H < 240
    - R = I * (1 + (S * (1 - cos(H - 240)) / (cos(300 - H))))
    - G = I * (1 - S)
    - B = I * (1 + (S * cos(H - 240)) / (cos(300 - H))), if 240 <= H < 360