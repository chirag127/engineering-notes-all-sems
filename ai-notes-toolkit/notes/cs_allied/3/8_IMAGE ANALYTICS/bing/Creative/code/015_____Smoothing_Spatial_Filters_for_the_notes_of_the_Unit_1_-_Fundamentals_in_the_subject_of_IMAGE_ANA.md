### Smoothing Spatial Filters

- Smoothing spatial filters are used for blurring and for noise reduction in digital image processing.
- Blurring is used to remove small details, bridge small gaps, or reduce the effect of noise in an image.
- Noise reduction is used to improve the quality or enhance the features of an image.
- Smoothing spatial filters operate in the spatial domain, which means they use the pixel values and their locations in the image to perform filtering.
- Smoothing spatial filters can be classified into two types: linear and non-linear.

#### Linear Smoothing Filters

- Linear smoothing filters use a weighted average of the pixels in a neighborhood to compute the output pixel value.
- The weights are specified by a filter mask or kernel, which is a small matrix that slides over the image.
- The output pixel value is the sum of the products of the filter mask coefficients and the corresponding input pixel values.
- Linear smoothing filters are also called convolution filters, because they perform a convolution operation between the filter mask and the image.
- Common linear smoothing filters include average smoothing and Gaussian smoothing .

##### Average Smoothing

- Average smoothing uses a filter mask with equal coefficients that add up to one.
- The output pixel value is the arithmetic mean of the input pixel values in the neighborhood.
- Average smoothing is simple and fast, but it may cause blurring of edges and loss of fine details.
- Example of average smoothing filter mask:

| 1/9 | 1/9 | 1/9 |
| --- | --- | --- |
| 1/9 | 1/9 | 1/9 |
| 1/9 | 1/9 | 1/9 |

##### Gaussian Smoothing

- Gaussian smoothing uses a filter mask with coefficients that follow a Gaussian distribution.
- The output pixel value is the weighted mean of the input pixel values in the neighborhood, where the weights are higher for the central pixels and lower for the peripheral pixels.
- Gaussian smoothing preserves edges and fine details better than average smoothing, but it is more computationally expensive.
- Example of Gaussian smoothing filter mask:

| 1/16 | 2/16 | 1/16 |
| ---- | ---- | ---- |
| 2/16 | 4/16 | 2/16 |
| 1/16 | 2/16 | 1/16 |

#### Non-linear Smoothing Filters

- Non-linear smoothing filters use a non-linear function of the pixels in a neighborhood to compute the output pixel value.
- The function can be based on the order, the median, the mode, or the range of the pixel values in the neighborhood.
- Non-linear smoothing filters are also called order-statistics filters, because they use the rank or position of the pixel values in the neighborhood.
- Common non-linear smoothing filters include median smoothing and adaptive smoothing .

##### Median Smoothing

- Median smoothing uses a filter mask with any coefficients that add up to one.
- The output pixel value is the median of the input pixel values in the neighborhood.
- Median smoothing is effective for removing salt-and-pepper noise or impulse noise, which are random white or black pixels in the image.
- Median smoothing preserves edges and fine details better than linear smoothing filters, but it may cause some distortion or loss of contrast.
- Example of median smoothing filter mask:

| 1/9 | 1/9 | 1/9 |
| --- | --- | --- |
| 1/9 | 1/9 | 1/9 |
| 1/9 | 1/9 | 1/9 |

##### Adaptive Smoothing

- Adaptive smoothing uses a filter mask with variable coefficients that depend on the local characteristics of the image.
- The output pixel value is the weighted mean of the input pixel values in the neighborhood, where the weights are higher for the pixels that are similar to the central pixel and lower for the pixels that are different from the central pixel.
- Adaptive smoothing is effective for removing Gaussian noise or random variations in pixel values in the image.
- Adaptive smoothing preserves edges and fine details better than linear smoothing filters, but it is more computationally complex.
- Example of adaptive smoothing filter mask: