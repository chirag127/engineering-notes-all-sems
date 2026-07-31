# Regional Descriptors

- Regional descriptors are features that describe the properties of a region in an image, such as its shape, size, color, texture, etc.
- Regional descriptors can be classified into two types: external and internal.
- External descriptors are based on the boundary of the region, such as perimeter, compactness, orientation, convexity, etc.
- Internal descriptors are based on the pixels inside the region, such as area, mean value, standard deviation, moments, etc.
- Regional descriptors can be used for various purposes, such as image segmentation, object recognition, shape analysis, etc.

## Examples of Regional Descriptors

- Area: the number of pixels in the region. It can be computed by counting the pixels or by multiplying the pixel size by the number of pixels.
- Perimeter: the length of the boundary of the region. It can be computed by tracing the boundary and adding the distances between adjacent pixels.
- Compactness: the ratio of the area to the perimeter squared. It measures how close the region is to a circle. It can be computed by dividing the area by the perimeter squared and multiplying by 4π.
- Mean value: the average intensity of the pixels in the region. It can be computed by summing the pixel values and dividing by the area.
- Standard deviation: the measure of the variation of the pixel values in the region. It can be computed by taking the square root of the variance, which is the average of the squared differences between the pixel values and the mean value.
- Moments: the weighted averages of the pixel values in the region. They can be computed by multiplying the pixel values by some powers of their coordinates and summing them over the region. Moments can capture various aspects of the region, such as its centroid, orientation, eccentricity, etc.