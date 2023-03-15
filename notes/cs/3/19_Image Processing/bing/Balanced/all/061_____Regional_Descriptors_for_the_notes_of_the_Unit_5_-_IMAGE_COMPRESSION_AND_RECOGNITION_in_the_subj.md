# Regional Descriptors

- Regional descriptors are features that describe the properties of a region in an image, such as its shape, color, texture, etc.
- Regional descriptors can be classified into two types: external and internal.
  - External descriptors are based on the boundary or contour of a region, such as perimeter, compactness, orientation, etc.
  - Internal descriptors are based on the pixels inside a region, such as area, mean value, standard deviation, etc.
- Regional descriptors can be used for various purposes, such as image compression, image recognition, image segmentation, etc.
- Some examples of regional descriptors are  :
  - Area: the number of pixels in a region, optionally multiplied by the real area of each pixel.
  - Perimeter: the length of the boundary of a region, optionally weighted by the edge strength or orientation.
  - Compactness: the ratio of the area to the perimeter squared, indicating how close a region is to a circle.
  - Orientation: the angle of the major axis of the best-fitting ellipse to a region, indicating the direction of the region.
  - Mean value: the average intensity or color of the pixels in a region, indicating the brightness or hue of the region.
  - Standard deviation: the measure of the variation of the intensity or color of the pixels in a region, indicating the contrast or saturation of the region.
  - Moments: the weighted averages of the pixel coordinates or intensities in a region, which can be used to compute other descriptors such as centroid, eccentricity, etc.