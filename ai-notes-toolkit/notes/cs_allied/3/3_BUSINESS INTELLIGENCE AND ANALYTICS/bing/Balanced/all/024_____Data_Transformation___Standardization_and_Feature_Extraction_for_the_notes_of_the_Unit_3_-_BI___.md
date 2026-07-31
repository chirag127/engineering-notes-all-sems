# Data Transformation – Standardization and Feature Extraction

## Data Transformation
- Data transformation is the process of modifying the data to make it more suitable for analysis and modeling.
- Data transformation can involve various operations, such as:
  - Cleaning: removing or correcting invalid, missing, or inconsistent data values.
  - Formatting: changing the data type, structure, or representation of the data.
  - Scaling: adjusting the range or distribution of the data values.
  - Encoding: converting categorical or textual data into numerical data.
  - Aggregating: summarizing or grouping the data by certain attributes or functions.
  - Filtering: selecting or excluding the data based on certain criteria or conditions.
  - Deriving: creating new data attributes from existing ones using mathematical or logical operations.
  - Combining: merging or joining data from different sources or tables.

## Standardization
- Standardization is a type of scaling that transforms the data values to have a mean of zero and a standard deviation of one.
- Standardization is also known as z-score normalization or standard score.
- Standardization can help to reduce the effect of outliers and different scales or units of measurement on the data.
- Standardization can also improve the performance of some machine learning algorithms, such as linear regression, logistic regression, k-means clustering, and support vector machines, that assume or prefer the data to be normally distributed and have similar variance.
- Standardization can be applied to a single data attribute or to a whole data set.
- Standardization can be performed using the following formula:

  - z = (x - mu) / sigma

  - where x is the original data value, mu is the mean of the data, sigma is the standard deviation of the data, and z is the standardized data value.

## Feature Extraction
- Feature extraction is the process of creating new data attributes from the original data that capture the essential information or characteristics of the data.
- Feature extraction can help to reduce the dimensionality, complexity, and redundancy of the data, and enhance the interpretability and predictive power of the data.
- Feature extraction can involve various techniques, such as:
  - Principal component analysis (PCA): a statistical method that transforms the data into a set of orthogonal and uncorrelated components that explain the maximum variance of the data.
  - Linear discriminant analysis (LDA): a supervised method that transforms the data into a set of linear combinations that maximize the separation between different classes or categories of the data.
  - Factor analysis (FA): a statistical method that models the data as a linear combination of a set of latent or hidden factors that account for the common variance or correlation of the data.
  - Independent component analysis (ICA): a statistical method that transforms the data into a set of independent and non-Gaussian components that capture the higher-order statistics of the data.
  - Kernel methods: a class of methods that apply a nonlinear transformation or function to the data, called a kernel, that maps the data into a higher-dimensional or feature space, where the data becomes more linearly separable or easier to analyze.