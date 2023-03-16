### Smoothing Spatial Filters

- Smoothing spatial filters are used for blurring and for noise reduction in digital image processing.
- Blurring is used to remove small details, bridge small gaps, or reduce the effect of noise in an image.
- Noise reduction is used to improve the quality or enhance the features of an image.
- Smoothing spatial filters operate in the spatial domain, which means they use the pixel values and their locations in the image to perform filtering.
- Smoothing spatial filters can be classified into two types: linear and non-linear.
- Linear smoothing filters use a weighted average of the pixels in a neighborhood to compute the output pixel value .
- Non-linear smoothing filters use a statistical measure of the pixels in a neighborhood, such as the median, the minimum, or the maximum, to compute the output pixel value.
- Commonly used linear smoothing filters include average smoothing and Gaussian smoothing .
- Commonly used non-linear smoothing filters include median smoothing and adaptive smoothing .
- Smoothing spatial filters can be implemented using convolution, which is a mathematical operation that combines two functions to produce a third function .
- Convolution can be represented by the symbol * and is defined as follows :

$$
(f * g)(x, y) = \sum_{s=-a}^{a} \sum_{t=-b}^{b} f(s, t) g(x-s, y-t)
$$

- In image processing, convolution involves sliding a filter mask (also called a kernel or a window) over the input image and multiplying the corresponding pixel values to produce the output image .
- The filter mask can have different sizes and shapes, depending on the desired effect of the filter .
- The filter mask can also have different values, depending on the type and the strength of the filter .
- The following diagram illustrates the convolution process for a 3x3 filter mask:

![Convolution diagram](https://www.dynamsoft.com/blog/wp-content/uploads/2019/08/convolution.png)

- The following table shows some examples of filter masks and their effects :

| Filter mask | Type | Effect |
|-------------|------|--------|
| ![Average filter mask](https://www.dynamsoft.com/blog/wp-content/uploads/2019/08/average-filter.png) | Linear | Blurs the image by taking the average of the neighboring pixels |
| ![Gaussian filter mask](https://www.dynamsoft.com/blog/wp-content/uploads/2019/08/gaussian-filter.png) | Linear | Blurs the image by taking the weighted average of the neighboring pixels, giving more weight to the center pixel |
| ![Median filter mask](https://www.dynamsoft.com/blog/wp-content/uploads/2019/08/median-filter.png) | Non-linear | Reduces the noise in the image by taking the median of the neighboring pixels, which is more robust to outliers |
| ![Adaptive filter mask](https://www.dynamsoft.com/blog/wp-content/uploads/2019/08/adaptive-filter.png) | Non-linear | Adjusts the filter mask according to the local characteristics of the image, such as the variance or the mean, to preserve edges and details |

- Smoothing spatial filters can be applied to grayscale or color images, but the filter mask should be applied to each color channel separately .
- Smoothing spatial filters can improve the appearance or the performance of an image, but they also have some drawbacks, such as loss of detail, blurring of edges, or introduction of artifacts .