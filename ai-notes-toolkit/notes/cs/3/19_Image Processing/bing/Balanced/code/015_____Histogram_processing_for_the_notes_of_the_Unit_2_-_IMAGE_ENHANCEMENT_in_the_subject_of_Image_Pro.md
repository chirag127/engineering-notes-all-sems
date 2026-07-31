### Histogram processing for the notes of the Unit 2 - IMAGE ENHANCEMENT in the subject of Image Processing

- Image enhancement is the process of adjusting digital images so that the results are more suitable for display or further image analysis  .
- Histogram processing is a widely used technique for image enhancement that modifies the dynamic range and contrast of an image by altering its intensity histogram  .
- An intensity histogram is a graphical representation of the distribution of pixel values in an image. It shows how many pixels have a certain intensity value, ranging from 0 (black) to 255 (white) for an 8-bit grayscale image.
- Histogram processing can be divided into two categories: histogram equalization and histogram specification.
- Histogram equalization is a technique that transforms the image such that its intensity histogram is approximately uniform, i.e., all intensity values have equal frequencies. This enhances the contrast of the image by spreading out the intensity values over the entire range  .
- Histogram specification is a technique that transforms the image such that its intensity histogram matches a desired histogram, which can be specified by the user or derived from another image. This allows the user to control the contrast and brightness of the image by choosing an appropriate histogram shape.
- Histogram processing can be applied to grayscale or color images. For color images, the histogram can be computed for each color channel separately or for a single luminance channel that represents the brightness of the image.
- Histogram processing can be implemented using the following steps:
  - Compute the histogram of the input image, i.e., count the number of pixels for each intensity value.
  - Compute the cumulative histogram of the input image, i.e., sum the frequencies of all intensity values up to a given value.
  - Normalize the cumulative histogram by dividing each value by the total number of pixels in the image. This gives the probability distribution function (PDF) of the input image.
  - If histogram equalization is desired, use the normalized cumulative histogram as the transformation function that maps each input intensity value to a new output intensity value. This ensures that the output image has a uniform histogram.
  - If histogram specification is desired, compute the normalized cumulative histogram of the desired histogram, which gives the PDF of the desired image. Then, find the inverse transformation function that maps each output intensity value to an input intensity value that has the same PDF. This ensures that the output image has the desired histogram.
  - Apply the transformation function to each pixel of the input image to obtain the output image.
  - Compute the histogram of the output image to verify the result.