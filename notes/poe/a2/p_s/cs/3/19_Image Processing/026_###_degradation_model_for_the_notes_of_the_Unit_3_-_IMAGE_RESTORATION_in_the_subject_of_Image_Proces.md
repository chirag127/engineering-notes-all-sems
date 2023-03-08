 Here is the content in markdown format for the given topic:

### Degradation Model

The degradation model assumes that the observed (distorted/blurred/noisy) image `g(x,y)` is related to the original image `f(x,y)` via a degradation function `h(x,y)` such that

`g(x,y) = h(x,y) * f(x,y)`     (1)

Where `*` represents the convolution operation. The degradation function `h(x,y)` accounts for blurring and noise addition that corrupts the original image.

The goal of image restoration is to estimate the original image `f(x,y)` from the observed degraded image `g(x,y)` and the degradation function `h(x,y)`.

***Some key points about the degradation model are:***

1. It assumes a linear model for the degradation which may not always hold true. More complex non-linear models can also be used.
2. The degradation function `h(x,y)` models the overall effect of blur and noise but does not distinguish between the two. Separate blur and noise models can also be used.
3. The observed image `g(x,y)` is considered to be a corrupted version of the original image `f(x,y)`. The restoration process tries to undo the corruption and estimate the original image.
4. The performance of any restoration method depends on how well the degradation model approximates the actual degradation process. An inaccurate model will result in a poor restoration.

[Diagrams/Images/Codes/Examples/Applications can be added here if required]

The content here summarizes the key points regarding the degradation model used in image restoration. The degradation model assumes a linear blurring and noise addition model to relate the original and observed images. The performance of restoration depends on how well this model approximates the actual degradation. More complex models can also be used as suited for different scenarios.