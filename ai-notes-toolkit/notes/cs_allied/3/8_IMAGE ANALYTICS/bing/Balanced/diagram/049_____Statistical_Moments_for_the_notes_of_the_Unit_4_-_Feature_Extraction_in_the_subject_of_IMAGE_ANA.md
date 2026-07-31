### Statistical Moments for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Statistical moments are a set of numerical values that describe the shape and characteristics of a probability distribution or an image .
- Statistical moments can be used to extract features from images, such as the mean, variance, skewness, and kurtosis of the pixel intensities or the shape and orientation of the objects in the image .
- The image moment M<sub>ij</sub> of order (i,j) for a greyscale image with pixel intensities I(x,y) is calculated as :

```
M_ij = sum_x sum_y x^i y^j I(x,y)
```

- The image moments can be normalized by dividing them by the zeroth-order moment M<sub>00</sub>, which is the sum of all pixel intensities . The normalized moments are denoted by mu<sub>ij</sub>:

```
mu_ij = M_ij / M_00
```

- The normalized moments are invariant to translation, scaling, and rotation of the image, which makes them useful for object recognition and classification .
- The first-order moments mu<sub>10</sub> and mu<sub>01</sub> are the coordinates of the centroid of the image, which is the center of mass of the pixel intensities :

```
x_bar = mu_10
y_bar = mu_01
```

- The second-order moments mu<sub>20</sub>, mu<sub>11</sub>, and mu<sub>02</sub> are related to the orientation and eccentricity of the image, which measure how much the image deviates from a circular shape . The orientation theta of the image is given by:

```
theta = 0.5 * arctan(2 * mu_11 / (mu_20 - mu_02))
```

- The eccentricity e of the image is given by:

```
e = sqrt(1 - 4 * mu_11^2 / ((mu_20 + mu_02)^2))
```

- The third-order moments mu<sub>30</sub>, mu<sub>21</sub>, mu<sub>12</sub>, and mu<sub>03</sub> are related to the skewness of the image, which measures the asymmetry of the pixel intensity distribution. The skewness S of the image is given by:

```
S = (mu_30 - 3 * mu_12)^2 + (3 * mu_21 - mu_03)^2
```

- The fourth-order moments mu<sub>40</sub>, mu<sub>31</sub>, mu<sub>22</sub>, mu<sub>13</sub>, and mu<sub>04</sub> are related to the kurtosis of the image, which measures the peakedness or flatness of the pixel intensity distribution. The kurtosis K of the image is given by:

```
K = (mu_40 - 3 * mu_22)^2 + (mu_04 - 3 * mu_13)^2
```

- Higher-order moments can also be computed, but they are more sensitive to noise and less interpretable.
- Statistical moments can be generalized to multivariate or multichannel images, such as color or hyperspectral images, by using tensor notation and multilinear algebra.