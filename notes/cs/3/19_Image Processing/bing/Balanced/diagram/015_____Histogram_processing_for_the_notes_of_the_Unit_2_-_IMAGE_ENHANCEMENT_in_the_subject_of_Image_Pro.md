### Histogram processing for image enhancement

- Histogram processing is a technique for adjusting the contrast and brightness of an image by modifying its intensity distribution  .
- A histogram is a graphical representation of the frequency of occurrence of each intensity level in an image .
- Histogram processing can be used to enhance the image quality by improving the visibility of details, reducing noise, and highlighting features of interest   .
- Histogram processing can be classified into two categories: histogram equalization and histogram specification .
- Histogram equalization is a method that transforms the image such that its histogram is approximately uniform, i.e., all intensity levels have equal probability   .
- Histogram equalization can enhance the contrast of images with low dynamic range, i.e., images that have a narrow range of intensity levels   .
- Histogram equalization can be applied globally or locally to the whole image or to sub-regions of the image  .
- Histogram specification is a method that transforms the image such that its histogram matches a desired histogram, i.e., a histogram that represents a target image or a desired contrast distribution .
- Histogram specification can be used to modify the image appearance according to a specific criterion, such as enhancing certain features, improving the visual quality, or matching the characteristics of another image .
- Histogram specification can also be applied globally or locally to the whole image or to sub-regions of the image .

#### Example of histogram equalization

The following figure shows an example of histogram equalization applied to a grayscale image. The original image has a low contrast and a skewed histogram, while the equalized image has a higher contrast and a more uniform histogram.

![Original image and its histogram](https://www.mygreatlearning.com/blog/wp-content/uploads/2020/12/Original-image-and-its-histogram.png)

![Equalized image and its histogram](https://www.mygreatlearning.com/blog/wp-content/uploads/2020/12/Equalized-image-and-its-histogram.png)

#### Example of histogram specification

The following figure shows an example of histogram specification applied to a grayscale image. The original image has a low contrast and a bimodal histogram, while the specified image has a higher contrast and a histogram that matches the desired histogram.

![Original image and its histogram](https://media.springernature.com/original/springer-static/image/art%3A10.1007%2Fs11831-021-09587-6/MediaObjects/11831_2021_9587_Fig1_HTML.png)

![Desired histogram](https://media.springernature.com/original/springer-static/image/art%3A10.1007%2Fs11831-021-09587-6/MediaObjects/11831_2021_9587_Fig2_HTML.png)

![Specified image and its histogram](https://media.springernature.com/original/springer-static/image/art%3A10.1007%2Fs11831-021-09587-6/MediaObjects/11831_2021_9587_Fig3_HTML.png)