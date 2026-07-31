# Histogram processing for image enhancement

- Histogram processing is a technique for adjusting the contrast and brightness of an image by modifying its intensity distribution  .
- A histogram is a graphical representation of the frequency of occurrence of each intensity level in an image .
- Histogram processing can be used to enhance the appearance or usefulness of an image for display or further analysis  .
- Histogram processing can be divided into two categories: histogram equalization and histogram specification .

## Histogram equalization
- Histogram equalization is a method that transforms an image such that its intensity histogram is approximately uniform   .
- Histogram equalization can improve the contrast and dynamic range of an image by spreading out the intensity values over the entire range   .
- Histogram equalization can be performed by computing the cumulative distribution function (CDF) of the original image and mapping each intensity level to a new level based on the CDF   .
- Histogram equalization can be applied to grayscale or color images, but the latter requires special care to preserve the color balance .

## Histogram specification
- Histogram specification is a method that transforms an image such that its intensity histogram matches a desired histogram .
- Histogram specification can be used to modify the contrast and brightness of an image according to a predefined or user-specified criterion .
- Histogram specification can be performed by computing the CDF of the original image and the desired histogram, and mapping each intensity level to a new level based on the inverse CDF of the desired histogram .
- Histogram specification can be applied to grayscale or color images, but the latter requires special care to preserve the color balance .

## Examples
- The following images show the original image, its histogram, and the results of histogram equalization and histogram specification .

![Original image](https://www.mygreatlearning.com/blog/wp-content/uploads/2020/12/Original-Image.png)

![Original histogram](https://www.mygreatlearning.com/blog/wp-content/uploads/2020/12/Original-Histogram.png)

![Histogram equalized image](https://www.mygreatlearning.com/blog/wp-content/uploads/2020/12/Histogram-Equalized-Image.png)

![Histogram equalized histogram](https://www.mygreatlearning.com/blog/wp-content/uploads/2020/12/Histogram-Equalized-Histogram.png)

![Histogram specified image](https://github.com/iamvishalprasad/Enhancement-of-Image-using-Histogram-Manipulation/blob/main/Output%20Images/Output%20Image%20-%20Histogram%20Specification.png?raw=true)
