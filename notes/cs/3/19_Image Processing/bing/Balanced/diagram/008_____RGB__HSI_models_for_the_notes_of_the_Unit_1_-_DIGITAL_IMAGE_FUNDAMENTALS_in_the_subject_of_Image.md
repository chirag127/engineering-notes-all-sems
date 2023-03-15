### RGB, HSI models for the notes of the Unit 1 - DIGITAL IMAGE FUNDAMENTALS in the subject of Image Processing

- RGB and HSI are two common color models used in digital image processing.
- A color model is a way of representing colors using numerical values.
- RGB stands for red, green, and blue. It is an additive color model, which means that different colors are obtained by adding different proportions of red, green, and blue light.
- HSI stands for hue, saturation, and intensity. It is a perceptual color model, which means that it represents colors similarly to how the human eye senses them.
- Hue is the dominant wavelength of the color, or the attribute that distinguishes one color from another, such as red, yellow, or blue.
- Saturation is the purity of the color, or the amount of white light mixed with the hue. A saturated color is vivid and bright, while an unsaturated color is dull and grayish.
- Intensity is the brightness of the color, or the amount of light reflected or emitted by the color. A high-intensity color is light and bright, while a low-intensity color is dark and dim.

- RGB and HSI models have different advantages and disadvantages for different image processing applications.
- RGB model is simple and widely used, especially for displaying images on digital devices. However, it is not very intuitive for human perception and manipulation of colors, and it is sensitive to illumination changes.
- HSI model is more suitable for human perception and manipulation of colors, and it is more robust to illumination changes. However, it is more complex and computationally expensive to convert from and to RGB model, and it is not widely supported by digital devices.

- To convert from RGB to HSI, the following formulas can be used :

```math
H = \begin{cases}
\theta, & \text{if } B \leq G \\
360 - \theta, & \text{if } B > G
\end{cases}
```
where
```math
\theta = \cos^{-1}\left(\frac{(R-G)+(R-B)}{2\sqrt{(R-G)^2+(R-B)(G-B)}}\right)
```
```math
S = 1 - \frac{3}{R+G+B}\min(R,G,B)
```
```math
I = \frac{1}{3}(R+G+B)
```

- To convert from HSI to RGB, the following formulas can be used :

```math
R = \begin{cases}
I(1+S\cos H/\cos(60-H)), & \text{if } 0 \leq H < 120 \\
I(1+S(1-\cos(H-120)/\cos(180-H))), & \text{if } 120 \leq H < 240 \\
I(1-S), & \text{if } 240 \leq H < 360
\end{cases}
```
```math
G = \begin{cases}
I(1-S), & \text{if } 0 \leq H < 120 \\
I(1+S\cos(H-120)/\cos(180-H)), & \text{if } 120 \leq H < 240 \\
I(1+S(1-\cos(H-240)/\cos(300-H))), & \text{if } 240 \leq H < 360
\end{cases}
```
```math
B = \begin{cases}
I(1+S(1-\cos H/\cos(60-H))), & \text{if } 0 \leq H < 120 \\
I(1-S), & \text{if } 120 \leq H < 240 \\
I(1+S\cos(H-240)/\cos(300-H)), & \text{if } 240 \leq H < 360
\end{cases}
```

- Here is a diagram that illustrates the RGB and HSI color models :

![RGB and HSI color models](https://i.imgur.com/9ZjHl0n.png)
