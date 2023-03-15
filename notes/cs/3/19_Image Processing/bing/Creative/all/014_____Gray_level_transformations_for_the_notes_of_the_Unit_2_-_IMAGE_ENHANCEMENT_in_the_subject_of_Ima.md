# Gray level transformations

Gray level transformations are image enhancement techniques that operate directly on the pixels of an image. They can be used to modify the contrast, brightness, or dynamic range of an image. Gray level transformations can be classified into three types: linear, logarithmic, and power-law.

## Linear transformations

Linear transformations are the simplest type of gray level transformations. They involve a linear mapping of the input gray level r to the output gray level s, such as s = ar + b, where a and b are constants. Linear transformations can be used to perform identity, negative, or contrast stretching operations.

- Identity transformation: s = r. This transformation does not change the image at all.
- Negative transformation: s = L - 1 - r, where L is the number of gray levels in the image. This transformation reverses the gray levels of the image, making dark areas light and vice versa. It can be used to enhance details in dark regions of the image.
- Contrast stretching transformation: s = (r - r_min) * (L - 1) / (r_max - r_min), where r_min and r_max are the minimum and maximum gray levels in the image. This transformation expands the range of gray levels in the image, making it more contrasted. It can be used to improve the visibility of low-contrast images.

## Logarithmic transformations

Logarithmic transformations are based on the logarithmic function s = c * log(1 + r), where c is a constant. Logarithmic transformations can be used to compress the dynamic range of an image, making the dark regions brighter and the bright regions darker. This can be useful for enhancing details in images with a high dynamic range, such as astronomical or medical images.

## Power-law transformations

Power-law transformations are based on the power-law function s = c * r^gamma, where c and gamma are constants. Power-law transformations can be used to perform gamma correction, which is a process of adjusting the brightness of an image to match the characteristics of the display device. Gamma correction can improve the perceptual quality of an image by making it more natural and realistic. Power-law transformations can also be used to perform contrast modification, by changing the value of gamma. A gamma value greater than 1 increases the contrast in the dark regions of the image, while a gamma value less than 1 increases the contrast in the bright regions of the image.