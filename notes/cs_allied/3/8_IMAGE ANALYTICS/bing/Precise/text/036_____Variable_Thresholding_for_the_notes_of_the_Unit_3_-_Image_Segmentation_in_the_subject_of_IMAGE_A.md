### Variable Thresholding

Variable thresholding is a technique used in image segmentation to generate a binary image from a given grayscale image by separating it into two regions based on a threshold value. This threshold value can be set based on the pixel intensity of the original image .

- **Thresholding**: Thresholding is one of the segmentation techniques that generates a binary image (a binary image is one whose pixels have only two values – 0 and 1 and thus requires only one bit to store pixel intensity) from a given grayscale image by separating it into two regions based on a threshold value.

- **Image thresholding segmentation**: Image thresholding segmentation is a simple form of image segmentation. It is a way to create a binary or multi-color image based on setting a threshold value on the pixel intensity of the original image. In this thresholding process, we will consider the intensity histogram of all the pixels in the image.

- **Different image thresholding techniques**: Image thresholding is a sub-module of image segmentation where certain pixel values are altered according to a particular threshold value where the pixel value of 0 is considered black and the pixel value of 255 is considered white.

- **Local thresholding**: Many global thresholding methods can be adapted to work in a local way, but there are also methods developed specifically for local thresholding, such as the Niblack or the Bernsen algorithms. Software such as ImageJ propose a wide range of automatic threshold methods, both global and local.