### Variable Thresholding for the notes of the Unit 3 - Image Segmentation in the subject of IMAGE ANALYTICS

- Image segmentation is the process of dividing an image into meaningful regions or segments based on some criteria, such as pixel intensity, color, texture, etc. 
- Image thresholding is one of the simplest and most common techniques of image segmentation, which converts a grayscale image into a binary image by assigning pixels to either foreground or background based on a threshold value.  
- Variable thresholding is a type of image thresholding that uses different threshold values for different regions of the image, instead of a single global value for the whole image. 
- Variable thresholding is useful when the image has uneven illumination or contrast, and a global threshold cannot separate the foreground and background effectively. 
- Variable thresholding can be classified into two categories: adaptive thresholding and local thresholding. 
- Adaptive thresholding is a method that determines the optimal threshold value for each pixel based on its local neighborhood, such as the mean or median intensity, standard deviation, entropy, etc.  
- Local thresholding is a method that divides the image into smaller regions or windows, and applies a global thresholding algorithm to each region separately, using either a fixed or a variable threshold value for each region.  
- Some examples of adaptive thresholding algorithms are Otsu's method, Sauvola's method, Bradley's method, etc. 
- Some examples of local thresholding algorithms are Niblack's method, Bernsen's method, Phansalkar's method, etc. 
- Image thresholding segmentation based on weighted Parzen-window estimation is a recent bi-level thresholding approach that uses a non-parametric density estimation technique to model the histogram of the image and find the optimal threshold value.