# Gray level transformations

Gray level transformations are image enhancement techniques that operate directly on the pixels of an image. They can be used to modify the contrast, brightness, or dynamic range of an image. They can also be used to create negative images, threshold images, or inverse-logarithmic images.

There are three basic types of gray level transformations:

- Linear transformations
- Logarithmic transformations
- Power-law transformations

## Linear transformations

Linear transformations are the simplest form of gray level transformations. They map the input gray level, r, to the output gray level, s, using a linear function of the form:

s = ar + b

where a and b are constants. The slope, a, determines the contrast of the output image, and the intercept, b, determines the brightness. If a = 1 and b = 0, the output image is identical to the input image. If a = -1 and b = 255, the output image is the negative of the input image.

Linear transformations can be used to adjust the contrast and brightness of an image by changing the range of gray levels. For example, if the input image has gray levels in the range [0, 100], and the output image has gray levels in the range [50, 200], the linear transformation is:

s = 1.5r + 50

This transformation increases the contrast and brightness of the image by stretching the gray level histogram.

## Logarithmic transformations

Logarithmic transformations are nonlinear transformations that map the input gray level, r, to the output gray level, s, using a logarithmic function of the form:

s = c log(1 + r)

where c is a constant. The logarithmic function compresses the high gray levels and expands the low gray levels. This can be useful for enhancing the details in dark regions of an image, such as X-ray images or astronomical images.

Logarithmic transformations can also be used to create inverse-logarithmic images, which are the negative of the logarithmic images. This can be done by subtracting the logarithmic image from the maximum gray level, 255. The inverse-logarithmic image has the opposite effect of the logarithmic image: it compresses the low gray levels and expands the high gray levels. This can be useful for enhancing the details in bright regions of an image, such as infrared images or thermal images.

## Power-law transformations

Power-law transformations are nonlinear transformations that map the input gray level, r, to the output gray level, s, using a power function of the form:

s = cr^γ

where c and γ are constants. The exponent, γ, determines the shape of the curve. If γ > 1, the curve is convex and the output image is darker than the input image. If γ < 1, the curve is concave and the output image is brighter than the input image. If γ = 1, the curve is linear and the output image is identical to the input image.

Power-law transformations can be used to correct the gamma of an image, which is the relation between the input intensity and the output brightness. Different devices, such as cameras, monitors, or printers, may have different gamma values, which can affect the appearance of an image. By applying a power-law transformation with the inverse gamma value, the image can be restored to its original brightness.

Power-law transformations can also be used to create threshold images, which are binary images that have only two gray levels: 0 or 255. This can be done by setting γ to a very large value, such as 10. This makes the curve very steep and the output image very sensitive to the input gray level. If the input gray level is above a certain threshold, the output gray level is 255; otherwise, it is 0. Threshold images can be useful for segmentation, edge detection, or object recognition.