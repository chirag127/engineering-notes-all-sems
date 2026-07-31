# Histogram processing for the notes of the Unit 2 - IMAGE ENHANCEMENT in the subject of Image Processing

- Histogram processing is a technique for adjusting the contrast and brightness of an image by modifying its intensity distribution  .
- A histogram is a graphical representation of the frequency of occurrence of each intensity level in an image .
- Histogram processing can be used to enhance the image quality by improving the visibility of details, reducing noise, and highlighting features of interest   .
- Histogram processing can be classified into two categories: histogram equalization and histogram specification  .

## Histogram equalization
- Histogram equalization is a method that transforms an image such that its histogram is approximately uniform, i.e., all intensity levels have equal probability   .
- Histogram equalization can enhance the contrast of an image by spreading out the intensity values over the entire range   .
- Histogram equalization can be performed by using the cumulative distribution function (CDF) of the original image as a mapping function to assign new intensity values to each pixel   .
- Histogram equalization can be applied to grayscale or color images, but it may affect the color balance and saturation of color images .
- Histogram equalization can be extended to adaptive histogram equalization, which divides the image into sub-regions and performs local histogram equalization on each sub-region .
- Histogram equalization can also be modified to contrast-limited adaptive histogram equalization, which limits the contrast enhancement in each sub-region to avoid amplifying noise .

## Histogram specification
- Histogram specification is a method that transforms an image such that its histogram matches a desired histogram, i.e., a specified probability distribution  .
- Histogram specification can be used to modify the contrast and brightness of an image by adjusting its intensity distribution to a desired shape  .
- Histogram specification can be performed by using the inverse CDF of the desired histogram and the CDF of the original image as mapping functions to assign new intensity values to each pixel  .
- Histogram specification can be applied to grayscale or color images, but it may affect the color balance and saturation of color images .
- Histogram specification can be used to perform histogram matching, which is a technique for aligning the histograms of two images for comparison or fusion  .
- Histogram specification can also be used to perform histogram stretching, which is a technique for increasing the dynamic range of an image by mapping its intensity values to the full range  .

## Examples of histogram processing
- The following figure shows an example of histogram equalization applied to a grayscale image:

![Histogram equalization example](https://www.mygreatlearning.com/blog/wp-content/uploads/2021/12/Histogram-Equalization-Example.png)

- The following figure shows an example of histogram specification applied to a color image:

![Histogram specification example](https://media.springernature.com/original/springer-static/image/art%3A10.1007%2Fs11831-021-09587-6/MediaObjects/11831_2021_9587_Fig1_HTML.png)