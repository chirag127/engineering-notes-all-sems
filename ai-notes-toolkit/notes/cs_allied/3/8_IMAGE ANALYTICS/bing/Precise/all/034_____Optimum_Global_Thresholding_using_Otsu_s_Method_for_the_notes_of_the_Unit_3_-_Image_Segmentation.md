# Optimum Global Thresholding using Otsu’s Method

Otsu’s method is a technique of performing global thresholding on a digital image. It is optimum in the sense that it maximizes the between-class variance . The basic crux of the method is that well-thresholded classes of pixels must be distinct with respect to the intensity levels of their pixels .

This threshold is determined by minimizing intra-class intensity variance, or equivalently, by maximizing inter-class variance . Otsu's method is a one-dimensional discrete analogue of Fisher's Discriminant Analysis, is related to Jenks optimization method, and is equivalent to a globally optimal k-means performed on the intensity histogram .

The optimum threshold value is the one where the within-class variance is minimum . OpenCV also provides a built-in function to calculate the threshold using this method. You just need to pass an extra flag, cv2.THRESH_OTSU in the cv2.threshold() function .

Otsu's method chooses a threshold that minimizes the intraclass variance of the thresholded black and white pixels . The global threshold T can be used with imbinarize to convert a grayscale image to a binary image .
