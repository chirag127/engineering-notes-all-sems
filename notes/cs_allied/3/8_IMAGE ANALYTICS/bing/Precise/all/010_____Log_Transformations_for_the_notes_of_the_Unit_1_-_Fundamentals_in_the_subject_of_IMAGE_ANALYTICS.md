# Unit 1 - Fundamentals: Log Transformations

Log transformations are a type of mathematical operation that can be applied to an image to enhance its contrast. This is particularly useful for images with low contrast, where the pixel values are clustered in a narrow range.

Here are some key points to remember about log transformations:

1. The basic formula for a log transformation is `s = c * log(1 + r)`, where `s` is the output pixel value, `r` is the input pixel value, and `c` is a constant.
2. The constant `c` is chosen to scale the output pixel values to the desired range. For example, if the output image is to be an 8-bit image with pixel values ranging from 0 to 255, then `c` can be chosen as `c = 255 / log(1 + max(r))`, where `max(r)` is the maximum pixel value in the input image.
3. Log transformations are particularly useful for enhancing the contrast of images with a large dynamic range, where the pixel values span a wide range.
4. Log transformations are a type of non-linear transformation, meaning that the relationship between the input and output pixel values is not a straight line.
5. Log transformations can also be used to compress the dynamic range of an image, making it easier to display or store.
