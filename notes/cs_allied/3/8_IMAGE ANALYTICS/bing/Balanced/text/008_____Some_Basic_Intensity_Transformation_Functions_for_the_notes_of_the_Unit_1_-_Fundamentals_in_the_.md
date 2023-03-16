### Some Basic Intensity Transformation Functions

- Intensity transformation is a basic digital image processing technique, where the pixel intensity levels of an image are transformed to new values using a mathematical transformation function, so as to get a new output image.
- Intensity transformations are also called point processing techniques, because they depend only on the intensity at a point.
- Intensity transformations are performed in the spatial domain, i.e. they are performed directly on the pixels of the image, as opposed to being performed on the Fourier transform of the image.
- Some common intensity transformation functions are:

  - **Linear transformation**: This is a simple transformation that maps the input intensity range to the output intensity range using a linear function. For example, the function `g(x) = a * f(x) + b`, where `a` and `b` are constants, is a linear transformation. Linear transformations can be used for brightness and contrast adjustment.
  - **Logarithmic transformation**: This is a transformation that maps the input intensity range to the output intensity range using a logarithmic function. For example, the function `g(x) = c * log(1 + f(x))`, where `c` is a constant, is a logarithmic transformation. Logarithmic transformations can be used for enhancing the details of dark regions in an image.
  - **Power-law transformation**: This is a transformation that maps the input intensity range to the output intensity range using a power-law function. For example, the function `g(x) = c * f(x)^r`, where `c` and `r` are constants, is a power-law transformation. Power-law transformations can be used for enhancing the details of bright or dark regions in an image, depending on the value of `r`.
  - **Histogram equalization**: This is a transformation that maps the input intensity range to the output intensity range such that the histogram of the output image is approximately uniform. Histogram equalization can be used for improving the contrast of an image by spreading the pixels over as many gray levels as possible.
  - **Thresholding**: This is a transformation that maps the input intensity range to a binary output range, such that the pixels below a certain threshold are assigned to one value, and the pixels above the threshold are assigned to another value. Thresholding can be used for image segmentation, i.e. separating the foreground from the background.

- The following diagram shows some examples of intensity transformation functions and their effects on an image:

![Intensity transformation functions and their effects on an image](https://cs.appstate.edu/~rt/ImgProc/notes/chap3_pres_files/image002.jpg)