### Data Reduction – Sampling

- Data reduction is a technique used in data mining to reduce the size of a dataset while still preserving the most important information.
- Data sampling is a data reduction technique that involves selecting a subset of the data to work with, rather than using the entire dataset .
- Data sampling can be useful for reducing the size of a dataset while still preserving the overall trends and patterns in the data .
- There are four types of sampling data reduction methods:
  - Simple random sample without replacement: This method selects a sample of size n from a dataset of size N without putting back the selected tuples. This ensures that each tuple has an equal probability of being selected and that no tuple is selected more than once.
  - Simple random sample with replacement: This method selects a sample of size n from a dataset of size N with putting back the selected tuples. This means that each tuple has an equal probability of being selected and that some tuples may be selected more than once.
  - Cluster sample: This method divides the dataset into clusters based on some criteria, such as geographic location, and then selects one or more clusters to form the sample. This can reduce the variability within the sample and increase the efficiency of the sampling process.
  - Stratified sample: This method divides the dataset into strata based on some attribute, such as gender, and then selects a proportional or equal number of tuples from each stratum to form the sample. This can ensure that the sample is representative of the population and that each stratum is adequately represented.