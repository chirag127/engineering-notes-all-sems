### Adaptive Filters for Image Restoration

Adaptive filters are commonly used in image processing to enhance or restore data by removing noise without significantly blurring the structures in the image. The adaptive filtering literature is vast and cannot adequately be summarized in a short chapter. However, a large part of the literature concerns one-dimensional (1D) signals .

Generally, adaptive filters are used to restore image pixels by removing noise without suggestively blurring the existing structures in the image. By contrasting every pixels present in the image and its surrounding neighbor pixels, the adaptive filter characterizes those pixels as noise. The neighborhood size is adaptable .

One example of an adaptive filter is the adaptive median filter, which works very well for noise intensity beyond 20%. The benefit of an adaptive filter over a median filter is that it does not erode away edges or small details in the image .