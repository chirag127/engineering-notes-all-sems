Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of IMAGE ANALYTICS. Here is the content for the topic of Power-Law Transformations for the notes of the Unit 1 - Fundamentals:

### Power-Law Transformations

- Power-law transformations are a class of image enhancement techniques that can be used to adjust the contrast and brightness of an image.
- Power-law transformations are also known as **gamma corrections** or **gamma transformations**.
- Power-law transformations are defined by the following equation:

$$s = c r^\gamma$$

where $s$ and $r$ are the output and input pixel values, respectively, $c$ is a positive constant, and $\gamma$ is the exponent that controls the shape of the transformation curve.

- Power-law transformations can be classified into three types based on the value of $\gamma$:

  - **Linear transformation** ($\gamma = 1$): This is a simple scaling of the pixel values by the constant $c$. It does not change the contrast or brightness of the image, but only the dynamic range.
  - **Logarithmic transformation** ($\gamma < 1$): This is a compression of the pixel values, especially the high values. It increases the contrast of the dark regions and decreases the contrast of the bright regions. It can be used to enhance the details of dark images or images with a high dynamic range.
  - **Exponential transformation** ($\gamma > 1$): This is an expansion of the pixel values, especially the low values. It increases the contrast of the bright regions and decreases the contrast of the dark regions. It can be used to enhance the details of bright images or images with a low dynamic range.

- Power-law transformations can be applied to grayscale or color images. For color images, the transformation can be applied to each color channel separately or to the luminance channel only.
- Power-law transformations can be implemented using a look-up table (LUT) that maps the input pixel values to the output pixel values according to the equation. The LUT can be precomputed and stored in memory for fast processing.
- Power-law transformations can be visualized using a plot of the output pixel values versus the input pixel values. The plot shows the shape of the transformation curve and the effect of changing the parameters $c$ and $\gamma$.

- Here is an example of a power-law transformation applied to a grayscale image with $\gamma = 0.5$:

![Original image](https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Vd-Orig.png/320px-Vd-Orig.png)

![Transformed image](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Vd-Trans.png/320px-Vd-Trans.png)

- Here is the plot of the transformation curve:

![Transformation curve](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Gamma_correction.svg/320px-Gamma_correction.svg.png)