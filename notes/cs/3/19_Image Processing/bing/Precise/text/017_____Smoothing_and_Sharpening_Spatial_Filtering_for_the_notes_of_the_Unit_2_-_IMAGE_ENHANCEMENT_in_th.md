### Smoothing and Sharpening Spatial Filtering

Smoothing and sharpening are two common techniques used in image enhancement. These techniques are used to improve the visual quality of an image by removing noise, blurring, or enhancing edges and details.

1. **Smoothing Spatial Filtering:** Smoothing is a technique used to reduce noise and other small variations in an image. This is achieved by replacing each pixel value with the average value of its neighboring pixels. This process is also known as low-pass filtering, as it allows low-frequency components of the image to pass through while attenuating high-frequency components.

2. **Sharpening Spatial Filtering:** Sharpening is a technique used to enhance the edges and details of an image. This is achieved by accentuating the high-frequency components of the image. One common method of sharpening is to subtract a smoothed version of the image from the original image, which enhances the high-frequency components while leaving the low-frequency components unchanged.

Both smoothing and sharpening can be achieved using various spatial filters, which are applied to the image using a process known as convolution. The choice of filter and its parameters will depend on the specific requirements of the image enhancement task.