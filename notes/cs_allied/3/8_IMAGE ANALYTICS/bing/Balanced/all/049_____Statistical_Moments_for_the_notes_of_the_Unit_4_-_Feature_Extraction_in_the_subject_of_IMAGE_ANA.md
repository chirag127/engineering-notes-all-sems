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

μ<sub>ij</sub> = ∑<sub>x</sub> ∑<sub>y</sub> (x - x̅)<sup>i</sup> (y - y̅)<sup>j</sup> f(x,y)

where x̅ and y̅ are the mean or centroid of the image or the region of interest, given by:

x̅ = M<sub>10</sub> / M<sub>00</sub>

y̅ = M<sub>01</sub> / M<sub>00</sub>

- The order of a moment indicates the degree of variation of the pixel intensity values around the origin or the mean. Higher-order moments capture more details and complexity of the image or the region of interest, while lower-order moments capture more global and simple characteristics.
- Some common statistical moments that are used as features for image analysis are:

  - Zeroth-order moment (M<sub>00</sub> or μ<sub>00</sub>): This is the sum of all pixel intensity values, and it represents the area or the mass of the image or the region of interest.
  - First-order moment (M<sub>10</sub>, M<sub>01</sub>, μ<sub>10</sub>, μ<sub>01</sub>): These are the sums of the products of pixel intensity values and their coordinates, and they represent the location or the centroid of the image or the region of interest.
  - Second-order moment (M<sub>20</sub>, M<sub>02</sub>, M<sub>11</sub>, μ<sub>20</sub>, μ<sub>02</sub>, μ<sub>11</sub>): These are the sums of the squares or the products of pixel intensity values and their coordinates, and they represent the variance or the covariance of the image or the region of interest. They can also be used to calculate the orientation and the eccentricity of the image or the region of interest.
  - Third-order moment (M<sub>30</sub>, M<sub>03</sub>, M<sub>21</sub>, M<sub>12</sub>, μ<sub>30</sub>, μ<sub>03</sub>, μ<sub>21</sub>, μ<sub>12</sub>): These are the sums of the cubes or the products of pixel intensity values and their coordinates, and they represent the skewness or the asymmetry of the image or the region of interest.
  - Fourth-order moment (M<sub>40</sub>, M<sub>04</sub>, M<sub>31</sub>, M<sub>13</sub>, M<sub>22</sub>, μ<sub>40</sub>, μ<sub>04</sub>, μ<sub>31</sub>, μ<sub>13</sub>, μ<sub>22</sub>): These are the sums of the fourth powers or the products of pixel intensity values and their coordinates, and they represent the kurtosis or the peakedness of the image or the region of interest.

- Statistical moments can be normalized or scaled to make them invariant to translation, rotation, scaling, or other geometric transformations. One way to normalize the moments is to use the Hu's invariant