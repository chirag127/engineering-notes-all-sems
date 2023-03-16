# Statistical Moments for Feature Extraction in Image Analytics

- Statistical moments are numerical values that describe the shape and distribution of an image or a region of interest.
- Statistical moments can be used as features for image analysis tasks such as recognition, classification, segmentation, retrieval, etc.
- Statistical moments can be calculated from the pixel intensity values, the histogram, the frequency domain, or the wavelet transform of an image or a region of interest.
- Statistical moments can be classified into two types: ordinary moments and central moments.
- Ordinary moments are calculated with respect to the origin of the coordinate system, while central moments are calculated with respect to the mean or centroid of the image or the region of interest.
- Ordinary moments are denoted by M<sub>ij</sub>, where i and j are the orders of the moments, and are defined as:

  M<sub>ij</sub> = ∑<sub>x</sub> ∑<sub>y</sub> x<sup>i</sup> y<sup>j</sup> f(x,y)

  where f(x,y) is the pixel intensity value at (x,y).

- Central moments are denoted by μ<sub>ij</sub>, where i and j are the orders of the moments, and are defined as:

  μ<sub>ij</sub> = ∑<sub>x</sub> ∑<sub>y</sub> (x - x̄)<sup>i</sup> (y - ȳ)<sup>j</sup> f(x,y)

  where x̄ and ȳ are the mean or centroid of the image or the region of interest, given by:

  x̄ = M<sub>10</sub> / M<sub>00</sub>

  ȳ = M<sub>01</sub> / M<sub>00</sub>

- The lower-order moments (i.e., i + j ≤ 2) have simple interpretations:

  - M<sub>00</sub> is the area or the sum of pixel intensity values of the image or the region of interest.
  - M<sub>10</sub> and M<sub>01</sub> are related to the position or the centroid of the image or the region of interest.
  - M<sub>11</sub> is related to the orientation or the direction of the image or the region of interest.
  - M<sub>20</sub> and M<sub>02</sub> are related to the variance or the spread of the image or the region of interest along the x and y axes, respectively.
  - M<sub>21</sub>, M<sub>12</sub>, M<sub>30</sub>, and M<sub>03</sub> are related to the skewness or the asymmetry of the image or the region of interest along the x and y axes, respectively.

- The higher-order moments (i.e., i + j > 2) capture more complex and subtle features of the image or the region of interest, such as curvature, kurtosis, etc.
- Statistical moments can be normalized or scaled to make them invariant to translation, rotation, scaling, and other geometric transformations.
- One way to normalize the moments is to use the Hu moments, which are seven invariant moments derived from the central moments up to the third order.
- Another way to normalize the moments is to use the Zernike moments, which are orthogonal moments derived from the Zernike polynomials on a unit circle.
- Statistical moments can also be calculated from the frequency domain or the wavelet transform of an image or a region of interest, which capture the spectral and texture features of the image or the region of interest, respectively.
- Statistical moments can be calculated efficiently using integral images, which are cumulative sums of pixel intensity values over rectangular regions of an image or a region of interest.
- Statistical moments can be combined with other features, such as color, shape, edge, etc., to form a more comprehensive and robust feature vector for image analysis tasks.