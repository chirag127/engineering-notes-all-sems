Hello, I am Sydney, your AI assistant. I can help you with your study material for Image Analytics. Here are some notes on Log Transformations for Unit 1 - Fundamentals.

```markdown
### Log Transformations

- Log transformations are a type of point operations that are used to enhance the contrast of an image, especially in the dark regions.
- Log transformations map a narrow range of low intensity values in the input image to a wider range of output values, while compressing the high intensity values.
- Log transformations are useful for visualizing images with large dynamic range, such as medical images or astronomical images, where the pixel values span several orders of magnitude.
- The general formula for log transformations is:

    s = c * log(1 + r)

    where s is the output pixel value, r is the input pixel value, and c is a constant that controls the slope of the transformation curve.

- The constant c can be determined by the following equation:

    c = (L - 1) / log(1 + max(r))

    where L is the number of gray levels in the image, and max(r) is the maximum pixel value in the image.

- Log transformations are invertible, meaning that the original image can be recovered from the transformed image by applying the inverse log function.
- Log transformations have the following properties:

    - They are monotonic, meaning that they preserve the order of pixel values in the image.
    - They are non-linear, meaning that they change the relative brightness of different regions in the image.
    - They are contrast-stretching, meaning that they increase the contrast of low intensity regions while decreasing the contrast of high intensity regions.
    - They are multiplicative, meaning that they depend on the magnitude of the pixel values, not their absolute values.
```